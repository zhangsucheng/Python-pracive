import pika


def send():
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='114.215.151.210'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='test.topic', routing_key='test.*', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

if __name__ == "__main__":
    send()