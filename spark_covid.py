# Import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import datediff

# Create Spark session object
spark = SparkSession.builder.appName('data_processing').getOrCreate()

# Load csv dataset
df = spark.read.csv('s3://tet-bd/datasets/spark/Casos_positivos_de_COVID-19_en_Colombia.csv', inferSchema=True, header=True)

# Borrar columna 'Codigo DIVIPOLA' y 'FIS'
df = df.drop('Codigo DIVIPOLA', 'FIS')

# Crear columna donde se almacena el calculo de dias transcurridos entre 'Fecha diagnostico'
# y 'fecha reporte web'
df = df.withColumn('dias_hasta_reporte', datediff(df['fecha reporte web'], df['Fecha diagnostico']))
df.filter(df['dias_hasta_reporte'] > 0).show()

# Filtrar aquellos con 'Edad' < 50 y 'Sexo' = M
df.filter(df['Edad'] < 50).filter(df['Sexo'] == 'M').show()

# Agrupar por 'Estado' y contar
df.groupBy('Estado').count().orderBy('count', ascending=False).show()

# Guardar los resultados en el bucket de S3
write_uri = 's3://tet-bd/datasets/spark/resultados'

df.coalesce(1).write.format('csv').option('header', 'true').save(write_uri)
 
