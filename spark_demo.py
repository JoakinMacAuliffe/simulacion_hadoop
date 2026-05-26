from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, explode, split, col

# Inicialización de la sesión de Spark
spark = SparkSession.builder \
    .appName("SparkDemo") \
    .master("local[*]") \
    .getOrCreate()

# Crear datos de prueba
data = [("User1", "Comentario de prueba hola hola hola"),
        ("User2", "Hay que utilizar otras palabras para que sea realista"),
        ("User3", "Por lo que no puedo utilizar el mismo comentario siempre"),
        ("User4", "No sé que más poner ayuda")]

# Crear DataFrame
df = spark.createDataFrame(data, ["usuario", "comentario"])

# Aplicar transformaciones (Aquí es donde Spark construye el DAG)
# Se pasan los comentarios a minúsculas, se dividen por palabras y se filtran las palabras cortas
palabras_df = df.select(explode(split(lower(col("comentario")), " ")).alias("palabra"))
resultado = palabras_df.filter(palabras_df.palabra.rlike("^[a-z]{3,15}$")) \
                       .groupBy("palabra") \
                       .count() \
                       .orderBy(col("count").desc())

# Acción (Spark ejecuta el plan generado en el DAG)
resultado.show()    

# Dejar el programa corriendo para poder acceder a interfaz web
input()

spark.stop()