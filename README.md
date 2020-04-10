# Bitácora

## Laboratorio HDFS

### DCA

1. Se ingresa por la terminal al DCA utilizando la VPN. ![Img-1](./images/HDFS-DCA/Img-1.png)
2. Creación del directorio _datasets_ en el HDFS en la ruta `/user/cgavir29/`. ![Img-2](./images/HDFS-DCA/Img-2.png)
3. Clonación del repositorio https://github.com/st0263eafit/bigdata que contiene los _datasets_ en `/home/cgavir29`. ![Img-3](./images/HDFS-DCA/Img-3.png)
4. Se toma la carpeta _datasets_ y se extraen los `.zip` que allí se encuentran. ![Img-4](./images/HDFS-DCA/Img-4.png)
5. Se copia el directorio local `/home/cgavir29/datasets` al directorio HDFS `/user/cgavir29/datasets`. ![Img-5](./images/HDFS-DCA/Img-5.png)

### Amazon S3

## EMR

### Pre-Creación

1. Antes de empezar es importante conocer el dashboard en el cual estaremos trabajando. ![Img-1](./images/EMR/Img-1.png)
2. Vamos a _Your VPCs_ y creamos una VPC donde haremos todas las configuraciones necesarias para el correcto funcionamiento del cluster EMR. ![Img-2](./images/EMR/Img-2.png)
3. En la sección _Internet Gateway_ creamos una Internet Gateway (IG) para nuestra VPC. ![Img-3](./images/EMR/Img-3.png)
4. Para agregar la IG damos click en _Attach to VPC_. ![Img-4](./images/EMR/Img-4.png)
5. Después vamos a Route Tables, seleccionamos la que tiene en _VPC ID_ el código correspondiente a la creada en el paso uno y le asignamos un nombre. ![Img-5](./images/EMR/Img-5.png)
6. Damos click en el botón de abajo _Routes_ y aparecerá un botón que dice _Edit routes_ damos click en este y añadimos la siguiente configuración. ![Img-6](./images/EMR/Img-6.png)
7. Vamos a la parte de _Subnets_ y damos click en _Create subnet_. Nos encontraremos con la siguiente pantalla, seleccionamos la VPC creada y llenamos los campos necesarios. ![Img-7](./images/EMR/Img-7.png)
8. Finalmente es hora de habilitar el _DNS Hostname_ y para ello vamos a _Your VPCs_, seleccionamos la VPC creada y en _Actions_ damos click en _Edit DNS hostnames_. ![Img-8](./images/EMR/Img-8.png) Nos mostrará la siguiente vista, damos click en el cambo _enable_ y después en guardar. ![Img-9](./images/EMR/Img-9.png)

### Creación

1. Vamos al servicio EMR de Amazon. ![Img-10](./images/EMR/Img-10.png) y damos click en el botón azul _Create cluster_ y nos encontraremos con la siguiente información.
2. Después del paso anterior nos encontraremos con lo siguente. ![Img-11](./images/EMR/Img-11.png) Para configurar adecuadamente nuestro cluster iremos a las opciones avanzadas presionando el link en donde se encuentra el puntero en la imagen anterior.
3. Ahora seleccionamos lo servicios que queremos que tenga nuestro cluster como se ve en la siguiente imagen. ![Img-12](./images/EMR/Img-12.png) y damos click en _Next_ en la esquina inferior derecha.
4. En esta sección indicamos la VPC que vamos a utilizar para nuestro cluster, así como la subnet. ![Img-13](./images/EMR/Img-13.png) igual que en el paso anterior presionamos _Next_ en la esquina inferior derecha.
5. Indicamos el nombre el cluster EMR que vamos a crear. ![Img-14](./images/EMR/Img-14.png) y presionamos el botón _Next_.
6. En este paso seleccionamos la _EC2 key pair_ que usaremos para acceder a nustro cluster. ![Img-15](./images/EMR/Img-15.png) y presionamos el botón _Create cluster_.
7. Cuando veamos la siguiente información nuestro cluster (tet-emr) se habrá creado satisfactoriamente. ![Img-16](./images/EMR/Img-16.png)
8. Aún no hemos terminado, debemos consigurar los puertos en el grupo de seguridad para asegurar que se tiene acceso a los diferentes servicios del cluster. Para damos click en el nombre del cluster en la imagen anterior y vamos al link que está subrayado en la siguiente imagen. ![Img-17](./images/EMR/Img-17.png)
9. Seleccionamos el que corresponde al master. ![Img-18](./images/EMR/Img-18.png) y asignamos los permisos correspondientes. ![Img-19](./images/EMR/Img-19.png) ![Img-20](./images/EMR/Img-20.png)

### Destrucción

1. Para destruir nuestro cluster simplemente seleccionamos nuestro cluster damos click en el botón _Terminate_. ![Img-16](./images/EMR/Img-16.png) nuestro cluster dejará de estar activo pero no desaparecerá. ![Img-23](./images/EMR/Img-23.png)

### Clonación

1. Para recrear un cluster igual al que se creó anterioemente seleccionamos nuestro cluster y vamos click en el botón _Clone_. ![Img-21](./images/EMR/Img-21.png)
2. Parecera el siguiente modal para preguntarnos si deseamos cambiar la configuración o siemplemente crear un nuevo cluster. ![Img-22](./images/EMR/Img-22.png)
3. También podemos recrear (clonar) un cluster con el cli de aws y para ello hacemos lo siguiente. Seleccionamos el cluster que queremos clonar y presionamos en _View details_. ![Img-23](./images/EMR/Img-23.png) Una vez allí damos click en _AWS CLI export_. ![Img-24](./images/EMR/Img-24.png) Finalmente copiamos el comando que aparece en pantalla. ![Img-25](./images/EMR/Img-25.png)
