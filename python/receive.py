# receive.py
import pika

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials('user', 'A5DGzuG3HeX48hwS')
))
channel = connection.channel()

# Declare the same queue to ensure it exists
channel.queue_declare(queue='hello')

# Define a callback function to process received messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Tell RabbitMQ that this consumer should receive messages from the 'hello' queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
