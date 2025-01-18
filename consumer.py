import cv2
import pika
import json
import os

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
QUEUE_NAME = "image_queue"
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

task_status = {}
STATUS_FILE = "task_status.json"


def load_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_status():
    with open(STATUS_FILE, "w") as f:
        json.dump(task_status, f, indent=4)


def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return 0

    if image.shape[1] < 400 or image.shape[0] < 400:
        image = cv2.resize(image, (image.shape[1] * 2, image.shape[0] * 2))

    (regions, _) = hog.detectMultiScale(
        image,
        winStride=(8, 8),
        padding=(16, 16),
        scale=1.1
    )

    for (x, y, w, h) in regions:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    output_path = os.path.join(
        OUTPUT_FOLDER,
        os.path.basename(image_path)
    )
    cv2.imwrite(output_path, image)
    print(f"Processed: {os.path.basename(image_path)}")

    return len(regions)


def consume_messages():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        try:
            data = json.loads(body)
            message_id = data.get("id", "unknown")
            image_path = data.get("image_path", "unknown")
            status = data.get("status", "unknown")

            print(f"Processing message: ID={message_id}, Path={image_path}, Status={status}")

            task_status[message_id] = {"status": "processing", "image_path": image_path}

            num_people = process_image(image_path)

            task_status[message_id] = {
                "status": "completed",
                "image_path": image_path,
                "people_detected": num_people
            }
            print(f"Message ID={message_id} processed. Detected {num_people} people.")

        except Exception as e:
            print(f"Error processing message: {e}")
            task_status[message_id] = {"status": "failed", "image_path": image_path}
            print(f"Message ID={message_id} status updated to 'failed'.")

        finally:
            ch.basic_ack(delivery_tag=method.delivery_tag)

        save_status()

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback,
        auto_ack=False
    )

    print("Running consumer...")
    channel.start_consuming()


if __name__ == "__main__":
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    task_status = load_status()
    consume_messages()
