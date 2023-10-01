import pika

class MessageBroker:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()

    def declareQueue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def publish(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    def consume(self, queue_name, callback):
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        print(f'Waiting for messages on {queue_name}')
        self.channel.start_consuming()

