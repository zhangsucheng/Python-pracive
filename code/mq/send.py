import pika
from datetime import datetime
import time


def send():
    credentials = pika.PlainCredentials('admin', 'suziyoudian')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('114.215.151.210', 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='test.topic', routing_key='test.*', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

def timer(n):
    while True:
        print(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        send()
        time.sleep(n)


if __name__ == "__main__":
    timer(5)
