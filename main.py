import pika
import os
import json

INPUT_FOLDER = "input_images"
QUEUE_NAME = "image_queue"


def publish_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    for filename in os.listdir(INPUT_FOLDER):
        filepath = os.path.join(INPUT_FOLDER, filename)
        if os.path.isfile(filepath):
            channel.basic_publish(exchange='',
                                  routing_key=QUEUE_NAME,
                                  body=json.dumps({"image_path": filepath}))
            print(f"Zakolejkowano: {filename}")

    connection.close()


if __name__ == "__main__":
    publish_messages()
