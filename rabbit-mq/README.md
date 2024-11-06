
## Installation with Helm

### RabbitMQ Operator

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```
```bash
helm install rabbitmq-operator bitnami/rabbitmq-cluster-operator -n rabbitmq
```
```bash
helm show values bitnami/rabbitmq-cluster-operator > values-operator.yaml
```
```bash
helm uninstall rabbitmq -n rabbitmq
```

### RabbitMQ

```bash
helm install rabbitmq bitnami/rabbitmq -n rabbitmq 
```
```bash
helm show values rabbitmq bitnami/rabbitmq > values-rabbitmq.yaml
```

kubectl port-forward service/rabbitmq 15672:15672 -n rabbitmq

kubectl port-forward service/rabbitmq 5672:5672 -n rabbitmq

kubectl port-forward service/node-publisher-api-service 3000:3000 -n rabbit-mq-applications