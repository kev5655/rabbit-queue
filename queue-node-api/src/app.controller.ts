import { Controller, Get } from '@nestjs/common';
import * as amqp from 'amqplib';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async getHello(): Promise<string> {
    await this.sendMessage('Hello from NestJS!');
    return 'Message sent to RabbitMQ!';
  }

  async sendMessage(msg: string) {
    try {
      // Connect to RabbitMQ server
      const connection = await amqp.connect({
        hostname: process.env.RABBITMQ_HOST || 'localhost',
        port: Number(process.env.RABBITMQ_PORT) || 5672,
        username: process.env.RABBITMQ_USER || 'guest',
        password: process.env.RABBITMQ_PASSWORD || 'guest',
      });
      const channel = await connection.createChannel();

      // Declare a queue to send to (it will be created if it doesn't exist)
      const queue = 'hello';
      await channel.assertQueue(queue, { durable: false });

      // Send message to the queue
      channel.sendToQueue(queue, Buffer.from(msg));
      console.log(` [x] Sent '${msg}'`);

      // Close the connection
      setTimeout(() => {
        channel.close();
        connection.close();
      }, 500);
    } catch (error) {
      console.error('Error sending message to RabbitMQ', error);
    }
  }
}
