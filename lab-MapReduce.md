# Laboratorio 2 - MapReduce

## 1. WordCount - LOCAL

1. Ingresamos a la carpeta `02-mapreduce` dentro del repositorio [bigdata](https://github.com/st0263eafit/bigdata).
2. Corremos el `wordcount-local.py` ![WC-MR-LOCAL-1](images/WC-MR-LOCAL/Img-1.png) y después el `wordcount-mr.py` en modo local. ![WC-MR-LOCAL-2](images/WC-MR-LOCAL/Img-2.png)

## 2. WordCount - HADOOP

1. Ingresamos a [jupter116.dis.eafit.edu.co](https://jupyter116.dis.eafit.edu.co/hub/login) y nos logeamos.
2. Una vez adentro iremos a la terminal para ingresar a la máquina. ![WC-MR-HADOOP-1](images/WC-MR-HADOOP/Img-1.png) ![WC-MR-HADOOP-2](images/WC-MR-HADOOP/Img-2.png)
3. Corremos el `wordcount-mrjob.py` de forma local. ![WC-MR-HADOOP-3](images/WC-MR-HADOOP/Img-3.png) ![WC-MR-HADOOP-4](images/WC-MR-HADOOP/Img-4.png)

## 3. WordCount - EMR

1. Ingresamos al cluster de EMR utilizando `ssh`. ![WC-MR-EMR-1](images/WC-MR-EMR/Img-1.png)
2. Instalamos `git` usando `yum install git -y` y clonamos el respositorio [bigdata](https://github.com/st0263eafit/bigdata) como se ve en la imagen. ![WC-MR-EMR-2](images/WC-MR-EMR/Img-2.png)
3. Instalamos `mrjob` con el comando `sudo pip-3.6 install mrjob` después seguimos los pasos como en la imagen para correr el `wordcount-mrjob.py`.![WC-MR-EMR-3](images/WC-MR-EMR/Img-3.png) Finalmente obtenemos el siguiente resultado. ![WC-MR-EMR-4](images/WC-MR-EMR/Img-4.png)

## 4. Ejercicio Seleccionado

Se escogió el ejercicio 1 y se obtuvo el siguiente resultado ![EMPLOYEE-1](images/EMPLOYEE/Img-1.png) el código se encuentra en [empleados.py](empleados.py).
