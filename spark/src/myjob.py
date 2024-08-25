from pyspark.sql import SparkSession
import time

# Crie uma SparkSession
spark = SparkSession.builder \
    .appName("Soma Valor Custo Transferencia") \
    .getOrCreate()

# Carregue o arquivo CSV em um DataFrame
df = spark.read.csv("/opt/spark/data/br_me_sic_transferencia.csv", header=True, inferSchema=True)

# Registre o DataFrame como uma tabela temporária
df.createOrReplaceTempView("transferencias")

# Use Spark SQL para somar a coluna 'valor_custo_transferencia'
resultado = spark.sql("SELECT SUM(valor_custo_transferencia) AS total_custo_transferencia FROM transferencias")

# Exiba o resultado
resultado.show()

# Feche a SparkSession
spark.stop()
