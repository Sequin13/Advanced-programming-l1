import pika
import os
import json
import requests

INPUT_FOLDER = "input_images"
QUEUE_NAME = "image_queue"
COUNTER_FILE = "message_counter.txt"


def get_next_id():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            counter = int(f.read())
    else:
        counter = 0

    counter += 1
    with open(COUNTER_FILE, "w") as f:
        f.write(str(counter))

    return counter


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    return False


def publish_messages():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    for filename in os.listdir(INPUT_FOLDER):
        filepath = os.path.join(INPUT_FOLDER, filename)
        if os.path.isfile(filepath):
            message_id = get_next_id()
            message = {
                "id": message_id,
                "image_path": filepath,
                "status": "pending"
            }

            channel.basic_publish(
                exchange='',
                routing_key=QUEUE_NAME,
                body=json.dumps(message)
            )
            print(f"Enqueued: {message}")

    connection.close()


def publish_url_image(url):
    message_id = get_next_id()
    image_path = os.path.join(INPUT_FOLDER, f"image_{message_id}.jpg")
    if download_image(url, image_path):
        message = {
            "id": message_id,
            "image_path": image_path,
            "status": "pending"
        }

        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME)

        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(message)
        )
        print(f"Enqueued image from URL: {url}")
        connection.close()

        return message_id

    return None


def publish_uploaded_image(image_path):
    message_id = get_next_id()
    message = {
        "id": message_id,
        "image_path": image_path,
        "status": "pending"
    }

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME)

        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(message)
        )
        print(f"Enqueued uploaded image: {image_path}")
        connection.close()
        return message_id
    except Exception as e:
        print(f"Failed to publish message: {e}")
        return None


def publish_image_multiple_times(image_path, count):

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    for _ in range(count):
        message_id = get_next_id()
        message = {
            "id": message_id,
            "image_path": image_path,
            "status": "pending"
        }
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(message)
        )
        print(f"Enqueued image {image_path} multiple times: ID={message_id}")

    connection.close()



if __name__ == "__main__":
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    publish_messages()
