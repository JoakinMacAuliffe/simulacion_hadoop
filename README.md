1. Levantar contenedores utilizando

docker compose up -d

2. Copiar dataset desde el host al contenedor

docker cp ventas_grandes.csv namenode:/ventas_grandes.csv

3. Subir dataset a HDFS

docker exec -it namenode hdfs dfs -put /ventas_grandes.csv /ventas_grandes.csv

4. Consulta base en Spark

df = spark.read.csv("hdfs://namenode:9000/ventas_grandes.csv", header=True)
import time
start = time.time()
print(f"Total filas: {df.count()}")
print(f"Tiempo: {time.time() - start} segundos")