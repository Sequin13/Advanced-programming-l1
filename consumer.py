import pika
import time


def process_message(ch, method, properties, body):
    print(f" [x] Odbieram {body.decode()}")
    time.sleep(10)
    print(f" [x] Zakończono przetwarzanie {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consumers(num_consumers=3):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_qos(prefetch_count=1)

    for _ in range(num_consumers):
        channel.basic_consume(queue='task_queue', on_message_callback=process_message)

    print(' [*] Czekam na wiadomości. Aby zakończyć, naciśnij CTRL+C')
    channel.start_consuming()


start_consumers(3)
