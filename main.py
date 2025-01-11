import pika


def enqueue_messages(messages):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    for message in messages:
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        print(f" [x] Wysłano '{message}'")

    connection.close()


messages = ["xd", "chuj", "kurwa", "wiadomosc nr cipka"]
enqueue_messages(messages)
