import os
import pika
import time
from tabulate import tabulate

# Retrieve RabbitMQ host and credentials from environment variables
rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
rabbitmq_user = os.getenv("RABBITMQ_USER", "user")
rabbitmq_password = os.getenv("RABBITMQ_PASSWORD", "A5DGzuG3HeX48hwS")

# Store them in a list of lists for tabulation
env_variables = [
    ["RABBITMQ_HOST", rabbitmq_host],
    ["RABBITMQ_USER", rabbitmq_user],
    ["RABBITMQ_PASSWORD", rabbitmq_password],
]

# logging.info(tabulate(env_variables, headers=["Key", "Value"], tablefmt="grid"))
# Print the environment variables in a beautiful table format
print(tabulate(env_variables, headers=["Key", "Value"], tablefmt="grid"))

try:
    print("Connect to rabbitmq")
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=rabbitmq_host,
        port=5672,
        credentials=pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    ))
    channel = connection.channel()

    # Declare the same queue to ensure it exists
    channel.queue_declare(queue='hello')

    # Define a callback function to process received messages
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        time.sleep(10)  # Wait 10 seconds before processing the next message
        ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message

    # Tell RabbitMQ that this consumer should receive messages from the 'hello' queue
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
except Exception as e:
    print("Error happened")
    print(e.message)
