from pyspark.sql import SparkSession

# Cria a sessão Spark
spark = SparkSession.builder.appName("NetworkFlowAnalysis").getOrCreate()

# Carrega o CSV
df = spark.read.csv("/opt/spark/data/unbalaced_20_80_dataset.csv", header=True, inferSchema=True)

# Cria uma tabela temporária para executar SQL
df.createOrReplaceTempView("network_flows")

# 1. Contagem do número de ocorrências de cada protocolo
protocol_count = spark.sql("""
    SELECT
        Protocol,
        COUNT(*) as Occurrences
    FROM
        network_flows
    GROUP BY
        Protocol
    ORDER BY
        Occurrences DESC
""")
protocol_count.show()

# 2. Cálculo da média e do desvio padrão da duração do fluxo por protocolo
flow_duration_stats = spark.sql("""
    SELECT
        Protocol,
        AVG(`Flow Duration`) as Avg_Flow_Duration,
        STDDEV(`Flow Duration`) as StdDev_Flow_Duration
    FROM
        network_flows
    GROUP BY
        Protocol
""")
flow_duration_stats.show()

# 3. Identificação dos endereços IP de origem e destino mais comuns
common_ips = spark.sql("""
    SELECT
        `Src IP`,
        `Dst IP`,
        COUNT(*) as Occurrences
    FROM
        network_flows
    GROUP BY
        `Src IP`, `Dst IP`
    ORDER BY
        Occurrences DESC
    LIMIT 10
""")
common_ips.show()

# Finaliza a sessão Spark
spark.stop()
