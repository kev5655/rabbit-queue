
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