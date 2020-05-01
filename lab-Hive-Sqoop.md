# Laboratorio Hive & Sqoop

## 1. Conexión Hive via Hue

1. Vamos a los detalles del cluster y copiamos la dirección que parace subrayada. ![HUE-1](images/HUE/Img-1.png)
2. Ahora, en un buscador ingresamos esa dirección poniendo al final `:8888` y veremos la siguiente vista. ![HUE-2](images/HUE/Img-2.png) Si es la primera vez, debe crear una cuenta siguiendo las instrucciones que allí aparecerán.

## 2. Archivos de Trabajo

1. Vamos a la sección de _Files_ como se observa en la siguiente imagen. ![HUE-7](images/HUE/Img-7.png)
2. Una vez allí nos aseguramos de tener los siguientes archivos con los que trabajaremos más adelante. ![HIVE-SQOOP-1](images/HIVE-SQOOP/Img-1.png)

## 3. Gestión (DDL) y Consultas (DQL)

En el menú desplegable de la esquina superior izquierda damos click en la opción _Tables_ y ejecutamos los siguientes comandos de gestión y consulta como se ve en las imágenes. Es importante tener en cuenta que se asume se tienen los _datasets_ en S3.

1. Creamos una base de datos. ![HIVE-SQOOP-2](images/HIVE-SQOOP/Img-2.png)
2. Creamos la tabla _hdi_ ![HIVE-SQOOP-3](images/HIVE-SQOOP/Img-3.png) y extraemos los datos correspondientes desde S3. ![HIVE-SQOOP-4](images/HIVE-SQOOP/Img-4.png)
3. Hacemos verificaciones y consultas. ![HIVE-SQOOP-5](images/HIVE-SQOOP/Img-5.png) ![HIVE-SQOOP-6](images/HIVE-SQOOP/Img-6.png) ![HIVE-SQOOP-7](images/HIVE-SQOOP/Img-7.png)
4. Creamos una tabla _expo_ enlazando a S3 ![HIVE-SQOOP-8](images/HIVE-SQOOP/Img-8.png) y realizamos consultas. ![HIVE-SQOOP-9](images/HIVE-SQOOP/Img-9.png)

## 4. WordCount - Hive

1. Creamos una tabla que apunte a los archivos en S3 que vamos a utilizar. ![HIVE-SQOOP-10](images/HIVE-SQOOP/Img-10.png)
2. Corremos el comando para contar ordenando por palabra. ![HIVE-SQOOP-11](images/HIVE-SQOOP/Img-11.png)
3. Corremos el comando una vez más haciendo las modificaciones para ordenar por frecuencia de mayor a menor. ![HIVE-SQOOP-12](images/HIVE-SQOOP/Img-12.png)

### 4.1. Reto

1. Creamos una tabla _results_ en donde se almacenarán los resultados. ![HIVE-SQOOP-13](images/HIVE-SQOOP/Img-13.png)
2. Corremos el comando insertando en ésta. ![HIVE-SQOOP-14](images/HIVE-SQOOP/Img-14.png)
3. Finalemente comprobamos que se hayan guardado los datos. ![HIVE-SQOOP-15](images/HIVE-SQOOP/Img-15.png)

## 5. Apache Sqoop

## 6. MySQL vs Hive
