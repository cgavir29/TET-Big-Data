# Laboratorio Spark

## 1. Notebook Data Processing

Estos fueron los pasos seguidos y resultados que se obtuvieron el ejecutar el Jupyter Notebook proveído. Éste se encuentra en [data_processing.ipynb](data_processing.ipynb) con las variables correspondientes del bucket de S3.

1. Teniendo un cluster EMR en estado _Waiting_ creamos un Notebook. ![SPARK-1](images/SPARK/Img-1.png) ![SPARK-2](images/SPARK/Img-2.png) ![SPARK-3](images/SPARK/Img-3.png) ![SPARK-4](images/SPARK/Img-4.png)
2. Subimos el `.ipynb` con el que trabajaremos. ![SPARK-5](images/SPARK/Img-5.png) ![SPARK-6](images/SPARK/Img-6.png)
3. Seleccionamos el kernel _PySpark_. ![SPARK-7](images/SPARK/Img-7.png)
4. Ejecutamos el código. ![SPARK-8](images/SPARK/Img-8.png) ![SPARK-9](images/SPARK/Img-9.png) ![SPARK-10](images/SPARK/Img-10.png) ![SPARK-11](images/SPARK/Img-11.png) ![SPARK-12](images/SPARK/Img-12.png) ![SPARK-13](images/SPARK/Img-13.png) ![SPARK-14](images/SPARK/Img-14.png) ![SPARK-15](images/SPARK/Img-15.png) ![SPARK-16](images/SPARK/Img-16.png)

## 2. Notebook COVID-19 Colombia

Se obtuvieron los resultados que se observan a continuación al correr el Jupyter Notebook [pyspark_covid.ipynb](pyspark_covid.ipynb). Lastimosamente parquet no funcionó puesto que la base de datos en formato csv realizada por el gobierno colombiano es pauperrima.

1. Creamos un nuevo `.ipynb` dando click al lado del _Upload_ que se observa en el punto 2 del numeral 1.
2. Se desarrolla el taller y se ejecuta. El texto que se encuentra en rojo es debido una de las tantas inconsistencias y errores en la estructura que tiene el dataset que provee el estado colombiano. ![SPARK-17](images/SPARK/Img-17.png) ![SPARK-18](images/SPARK/Img-18.png) ![SPARK-19](images/SPARK/Img-19.png) ![SPARK-20](images/SPARK/Img-20.png) ![SPARK-21](images/SPARK/Img-21.png)
