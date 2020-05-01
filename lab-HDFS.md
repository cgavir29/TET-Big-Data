# Laboratorio HDFS

## 1. DCA

1. Se ingresa por la terminal al DCA utilizando la VPN. ![HDFS-DCA-1](images/HDFS-DCA/Img-1.png)
2. Creación del directorio _datasets_ en el HDFS en la ruta `/user/cgavir29/`. ![HDFS-DCA-2](images/HDFS-DCA/Img-2.png)
3. Clonación del repositorio [st0264eafit/bigdata](https://github.com/st0263eafit/bigdata) que contiene los _datasets_ en `/home/cgavir29`. ![HDFS-DCA-3](images/HDFS-DCA/Img-3.png)
4. Se toma la carpeta _datasets_ y se extraen los `.zip` que allí se encuentran. ![HDFS-DCA-4](images/HDFS-DCA/Img-4.png)
5. Se copia el directorio local `/home/cgavir29/datasets` al directorio HDFS `/user/cgavir29/datasets`. ![HDFS-DCA-5](images/HDFS-DCA/Img-5.png)

## 2. S3

1. Vamos al servicio de S3 y presionamos el botón _Create bucket_. ![HDFS-S3-1](images/HDFS-S3/Img-1.png)
2. Ponemos un nombre al bucket, nos aseguramos que _Block all public access_ no esté activado y damos en _Create bucket_. ![HDFS-S3-2](images/HDFS-S3/Img-2.png)
3. Ahora creamos una carpeta que se llamará `datasets`. ![HDFS-S3-3](images/HDFS-S3/Img-3.png) ![HDFS-S3-4](images/HDFS-S3/Img-4.png)
4. Finalmente damos acceso público al directorio creado ![HDFS-S3-5](images/HDFS-S3/Img-5.png) ![HDFS-S3-6](images/HDFS-S3/Img-6.png) y pasamos a cargar los datos.
5. Primero clonamos el repositorio con los comandos que se ven en pantalla.![HDFS-S3-7](images/HDFS-S3/Img-7.png) Después, en S3 entramos a la carpeta _datasets_ y damos click en _upload_.![HDFS-S3-8](images/HDFS-S3/Img-8.png) Arrastramos los archivos que clonamos del repositorio y seguimos las configuraciones como se indica. ![HDFS-S3-9](images/HDFS-S3/Img-9.png) ![HDFS-S3-10](images/HDFS-S3/Img-10.png) ![HDFS-S3-11](images/HDFS-S3/Img-11.png) ![HDFS-S3-12](images/HDFS-S3/Img-12.png) ![HDFS-S3-13](images/HDFS-S3/Img-13.png) ![HDFS-S3-14](images/HDFS-S3/Img-14.png)

## 3. EMR

### 3.1. Creación

1. Vamos al servicio EMR de Amazon. ![EMR-1](images/EMR/Img-1.png) y damos click en el botón azul _Create cluster_ y nos encontraremos con la siguiente información.
2. Después del paso anterior nos encontraremos con lo siguente. ![EMR-2](images/EMR/Img-2.png) Para configurar adecuadamente nuestro cluster iremos a las opciones avanzadas presionando el link en donde se encuentra el puntero en la imagen anterior.
3. Ahora seleccionamos lo servicios que queremos que tenga nuestro cluster como se ve en la siguiente imagen. ![EMR-3](images/EMR/Img-3.png) y damos click en _Next_ en la esquina inferior derecha.
4. En esta sección indicamos la VPC que vamos a utilizar para nuestro cluster, así como la subnet y el tipo de instancias que utlizaremos para el _Master_ y el _Core_. ![EMR-4](images/EMR/Img-4.png) igual que en el paso anterior presionamos _Next_ en la esquina inferior derecha.
5. Indicamos el nombre el cluster EMR que vamos a crear. ![EMR-5](images/EMR/Img-5.png) y presionamos el botón _Next_.
6. En este paso seleccionamos la _EC2 key pair_ que usaremos para acceder a nustro cluster. ![EMR-6](images/EMR/Img-6.png) y presionamos el botón _Create cluster_.
7. Cuando veamos la siguiente información nuestro cluster (tet-emr) se habrá creado satisfactoriamente. ![EMR-7](images/EMR/Img-7.png)
8. Aún no hemos terminado, debemos consigurar los puertos en el grupo de seguridad para asegurar que se tiene acceso a los diferentes servicios del cluster. Para damos click en el nombre del cluster en la imagen anterior y vamos al link que está subrayado en la siguiente imagen. ![EMR-8](images/EMR/Img-8.png)
9. Seleccionamos el que corresponde al master. ![EMR-9](images/EMR/Img-9.png) y asignamos los permisos correspondientes. ![EMR-10](images/EMR/Img-10.png)

### 3.2. Destrucción

1. Para destruir nuestro cluster simplemente seleccionamos nuestro cluster damos click en el botón _Terminate_. ![EMR-7](images/EMR/Img-7.png) nuestro cluster dejará de estar activo pero no desaparecerá. ![EMR-13](images/EMR/Img-13.png)

### 3.3. Clonación

1. Para recrear un cluster igual al que se creó anterioemente seleccionamos nuestro cluster y vamos click en el botón _Clone_. ![EMR-11](images/EMR/Img-11.png)
2. Aparecerá el siguiente pop-up para preguntarnos si deseamos cambiar la configuración o simplemente crear un nuevo cluster. ![EMR-12](images/EMR/Img-12.png)
3. También podemos recrear (clonar) un cluster con el CLI de AWS y para ello hacemos lo siguiente. Seleccionamos el cluster que queremos clonar y presionamos en _View details_. ![EMR-13](images/EMR/Img-13.png) Una vez allí damos click en _AWS CLI export_. ![EMR-14](images/EMR/Img-14.png) Finalmente copiamos el comando que aparece en pantalla. ![EMR-15](images/EMR/Img-15.png)

### 3.4. Acceso SSH

1. Vamos a los detalles de nuestro cluster, damos click en donde está el mouse y copiamos el comando que aparece subrayado. ![EMR-SSH-1](images/EMR-SSH/Img-1.png)
2. Pegamos el comando en la terminal y ya podemos acceder al cluster, cabe recordar que se debe tener la llave de acceso. También podemos ver que los comandos de HDFS funcionan sin ningún problema.![EMR-SSH-2](images/EMR-SSH/Img-2.png)

### 3.5. Acceso HUE

1. Vamos a los detalles del cluster y copiamos la dirección que parace subrayada. ![HUE-1](images/HUE/Img-1.png)
2. Ahora vamos a un buscador e ingresamos esa dirección poniendo al final `:8888` y veremos la siguiente vista. ![HUE-2](images/HUE/Img-2.png) Si es la primera vez, debe crear una cuenta siguiendo las instrucciones que allí aparecerán.
3. Una vez adentro podemos ver nuestros buckets de S3 siguiendo estos pasos: ![HUE-3](images/HUE/Img-3.png) ![HUE-4](images/HUE/Img-4.png) ![HUE-5](images/HUE/Img-5.png) ![HUE-6](images/HUE/Img-6.png)
4. También podemos acceder desde HUE al HDFS, así: ![HUE-7](images/HUE/Img-7.png) ![HUE-8](images/HUE/Img-8.png) y subir archivos de la siguiente forma. ![HUE-9](images/HUE/Img-9.png) ![HUE-10](images/HUE/Img-10.png) ![HUE-11](images/HUE/Img-11.png)
