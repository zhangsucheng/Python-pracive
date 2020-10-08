import pika,sys,os


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


def main():
    credentials = pika.PlainCredentials('admin', 'suziyoudian')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('114.215.151.210', 5672, '/', credentials))
    channel = connection.channel()
    channel.basic_consume("hello",callback,auto_ack=True)

    print("waiting for messages ")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)