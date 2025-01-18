import cv2
import pika
import json
import os

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
QUEUE_NAME = "image_queue"
hog = cv2.HOGDescriptor()

def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None

    (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    output_path = os.path.join(OUTPUT_FOLDER, os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    print(f"Processed: {os.path.basename(image_path)}")
    return len(regions)

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    def callback(body):
        data = json.loads(body)
        image_path = data["image_path"]
        num_people = process_image(image_path)
        print(f"Wykryto {num_people} osób na zdjęciu {os.path.basename(image_path)}")

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    print("Konsument uruchomiony...")
    channel.start_consuming()

if __name__ == "__main__":
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    consume_messages()
