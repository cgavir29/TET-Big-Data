#!/usr/bin/env python
# coding: utf-8

# Import SparkSession
from pyspark.sql.types import StringType, DoubleType, IntegerType
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession


# Create Spark session object
spark = SparkSession.builder.appName('data_processing').getOrCreate()

# Load csv dataset
df = spark.read.csv('s3://tet-bd/datasets/spark/Casos_positivos_de_COVID-19_en_Colombia.csv',
                    inferSchema=True, header=True)

# Borrar columna 'Codigo DIVIPOLA' y 'FIS'
df.drop('Codigo DIVIPOLA')
df.drop('FIS')

# Crear columna donde se almacena el calculo de dias transcurridos entre 'Fecha diagnostico'
# y 'fecha reporte web'

# Filtrar aquellos con 'Edad' < 50 y 'Sexo' = M
df.filter((df['Edad'] < 50) & (df['Sexo'] == 'M')).show()

# Agrupar por 'Estado' y contar
df.groupBy('Estado').count().orderBy('count', ascending=False).show()
