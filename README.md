# GrainChainChallenge
Este proyecto da solución al problema de matrices

# Instrucciones para correr el proyecto

### Instalar Python
Se requiere tener instalada alguna versión de python ( 3.8 o superior).
se puede descargar e instalar siguiendo los pasos desde la pagina oficial www.python.org

Una vez instalado python al ser una versi{on 3, todo lo que ejecutemos será con python3.

### Instalar PIP
Ahora, requerimos tener instalado el instalador de paquetes de python, (pip), en este caso pip3. 
Para ello ejecutaremos el siguiente comando ( en mi caso uso linux): 

```
    sudo apt-get install python3-pip
```

una vez instalado pip, necesitaremos crear un entorno virtual, por lo que procederemos a instalar virtual env, que es una herramienta que nos ayudará a crear el entorno virtual. 
haremos uso de pip para la instalación 

```
sudo pip3 install virtualenv
```

una vez instalado virtual env, procederemos a crear un entorno virtual, para ello ejecutaremos el siguiente comando: 

```
python3 -m venv .venv

```
En este caso yo instalaré el entorno virtual en el directorio raíz del proyecto. 

una vez creado el entorno virtual, será necesario acceder a el y activarlo, esto lo haremos con el comando: 

```
source .venv/bin/activate

```

una vez dentro y activado el entorno virtual, aparecerá al inicio de la línea de comandos de la siguiente forma: (venv)

Ahora, será necesario instalar los requerimientos para poder correr el proyecto. 

Para ello, dentro del entorno virtual ejecutarémos el siguiente comando: 

```
pip3 instal -r requirements.txt

```
Este comando nos ayudará a instalar todas las librerías/bibliotecas necesarias para que nuestro proyecto funcione. 

Una vez instaladas las librerías ya podrémos correr nuestro proyecto, lo harémos con el siguiente comando: 


```
python3 app.py

```

El proyecto corre en el puerto :5000 podremos acceder al frontend desde el navegador  con la dirección 

```
http://localhost:5000

```

Como PLUS, y para hacerles el trabajo más sencillo, tomé la decisión de subir este proyecto a un servidor, donde podrán acceder a través del siguiente link: 
```
https://limitless-sea-46792.herokuapp.com/

```
Donde nos aparecerá esta pantalla: 
![image](https://user-images.githubusercontent.com/37637850/156895336-6a999b8e-6dae-4213-bcc0-e58c93aa79d8.png)

Debemos cargar un archivo que contenga una matríz de 1 y 0 ( puede ser como queramos, siempre y cuando respetando únicamente los valores 0 y 1). 
Los números pueden estar separados por espacio o por coma, acontinuación adjunto un ejemplo de una matriz separada por espacios: 
![image](https://user-images.githubusercontent.com/37637850/156895413-7f4d03f7-8ffe-4d69-98e9-daf8610facf8.png)

Una vez cargado el archivo, pulsamos sobre el botón calcular iluminación. 

Esta acción nos llevará a la vista de la matríz, donde debemos pulsar sobre el botón "Acomodar N focos"
donde N es el número de focos por acomodar. 
![image](https://user-images.githubusercontent.com/37637850/156895510-cab76232-5d7b-4cca-be24-e73d88888e6d.png)

Una vez pulsado, podremos ver la palabra "FOCO", misma que indíca que en ese lugar debe ir un Foco. 
Por igual, podemos ver las celdas en amarillo. 

![image](https://user-images.githubusercontent.com/37637850/156895594-3adf8eb8-f5d5-4854-9be6-1d03932fbc45.png)


Si deseamos cambiar la matríz, bastará con pulsar el botón cargar nueva habitación, crear un nuevo archivo .txt de matriz (como el ejemplo mostrado anteriormente) cargarlo y repetír el proceso. 

Espero Este proyecto sea de su agrado. 

## GRACIAS POR SU TIEMPO Y ATENCIÓN



 
