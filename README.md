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
8. Finalmente es hora de habilitar el _DNS Hostname_ y para ello vamos a _Your VPCs_, seleccionamos la VPC creada y en _Actions_ damos click en _Edit DNS hostnames_. ![Img-8](./images/EMR/Img-8.png)
Nos mostrará la siguiente vista, damos click en el cambo _enable_ y después en guardar. ![Img-9](./images/EMR/Img-9.png)

### Creación

### Destrucción

### Clonación
