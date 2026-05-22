1. Levantar contenedores

docker compose up -d

2. Copiar el dataset al contenedor de Hadoop

docker cp ventas_grandes.csv namenode:/ventas_grandes.csv

3. Subir el archivo a HDFS

docker exec -it namenode hdfs dfs -put /ventas_grandes.csv /ventas_grandes.csv

docker exec -it namenode hdfs dfs -setrep -w 1 /ventas_grandes.csv

docker exec -it namenode hdfs dfs -setrep 3 /ventas_grandes.csv

4. Ejecutar consultas desde Spark

docker exec -it spark-master /spark/bin/pyspark --master spark://spark-master:7077

5. Una vez en la consola de Spark, ejecutar consultas en PySpark

df = spark.read.csv("hdfs://namenode:9000/ventas_grandes.csv", header=True)
import time
start = time.time()
print(f"Total filas: {df.count()}")
print(f"Tiempo: {time.time() - start} segundos")
input()


df = spark.read.csv("hdfs://namenode:9000/ventas_grandes.csv", header=True)
from pyspark.sql import functions as F
ventas_por_categoria = df.groupBy("categoria").count().orderBy("count", ascending=False)
ventas_por_categoria.show()
input()