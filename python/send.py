# send.py
import pika

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials('user', 'A5DGzuG3HeX48hwS')
))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Send a message to the 'hello' queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello, World!')
print(" [x] Sent 'Hello, World!'")

# Close the connection
connection.close()
