FROM bitnami/spark:3.5

USER root

RUN apt-get update -y && apt-get install -y openssl

WORKDIR /opt/spark

COPY . .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --user -r requirements.txt