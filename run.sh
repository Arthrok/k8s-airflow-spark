kind create cluster --config kubernetes/kind-config.yaml

helm install spark-operator spark-operator/spark-operator --namespace spark-operator --create-namespace

kubectl apply -f kubernetes/SparkApplication.yaml