# PIP y entornos virtuales

**Qué es python?**
Python es un lenguaje de programación _interpretado_ cuya filosofía hace hincapié en una sintaxis que favorezca un código legible. Se trata de un lenguaje de programación **multiparadigma**, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es administrado por la Python Software Foundation. Su nombre es un guiño al grupo cómico británico Monty Python.


Python es un lenguaje de programación muy popular, y es usado en muchos proyectos. En este tutorial, vamos a instalar Python 3 y PIP, y vamos a crear un entorno virtual para instalar paquetes de Python.

:fire: **Nota:** Para esta caso se va a hacer uso de WSL (Windows Subsystem for Linux), asi que si no tienen instalado WSL, pueden seguir el siguiente tutorial: [WSL](https://gndx.dev/blog/instalar-wsl2-en-windows-11/)

- `sudo apt update`
- `sudo apt upgrade`
- `python3 --version`
- `sudo apt install -y python3-pip` Install the package manager for Python3

- `pip3 -V`

- `sudo apt install -y build-essential libssl-dev libffi-dev python3-dev` Install the dependencies  for professional environments


Como se esta usando WSL, y se va a usar VSCode, es necesario instalar el plugin de Python para VSCode, para que se pueda usar el intellisense de Python.
- WSL
- python on WSL

- `mkdir folder-name` Permite crear una carpeta


> :warning: En algunos casos WSL puede fallar al intentar abrirlo y le muestra un error como este:
> `The service cannot be started`
> Para solucionar este problema, se debe ejecutar el siguiente comando en CMD como administrador:
> **`sc config LxssManager start=auto`**

:warning: El problema es generado por Kaspersky.
Kaspersky le mostrará una ventana emergente sobre un hilo potencial. Dígale a Kaspersky que ignore la alerta. No haga clic en el botón "Repararlo" de Kaspersky o deshará la solución.

## Qué es PIP

PIP es un sistema de gestión de paquetes usado para instalar y administrar paquetes de software escritos en Python. Muchos paquetes pueden ser encontrados en el índice de paquetes de Python.

- matplotlib
- numpy

Un ambiente virtual es un entorno aislado donde se puede instalar paquetes de Python sin afectar el entorno global. Esto es útil cuando se trabaja con diferentes proyectos que requieren diferentes versiones de paquetes de Python.


Para usar los entornos virtuales, primero se debe instalar el paquete virtualenv. El paquete virtualenv se puede instalar usando PIP.

- **Verifica donde está python y pip**
    - `which python3`
    - `which pip3`
- **Instalar venv en Linux o WSL**
    - `sudo apt install -y python3-venv`

- **Poner cada proyecto en su propio ambiente, entrar en cada carpeta.**
    - `python3 -m venv env` Crear un ambiente virtual (**`env`** indica el nombre del ambiente)

- **Activar el ambiente**
    - `source env/bin/activate` Activar el ambiente virtual
    - `which python3` Verificar que se esta usando el ambiente virtual

- **Desactivar el ambiente**
    - `deactivate`

- **Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo**
    - `pip3 install matplotlib`
    - `pip3 install numpy`

- **Verificar las instalaciones**
    - `pip3 freeze`


**:bulb: NOTA**: Cuando creamos el ambiente virtual, podremos usar **python3** o **python** para ejecutar el intérprete de Python. Pero cuando instalamos paquetes usando PIP, debemos usar **pip3** o **pip**. En algunos casos apunta a la misma versión que se tenga.

> No importa si se usa el mismo nombre para el ambiente virtual, ya que se crean en diferentes directorios. Por ejemplo, si se crea un ambiente virtual llamado **env** en el directorio **/home/user1**, y luego se crea otro ambiente virtual llamado **env** en el directorio **/home/user2**, no habrá ningún problema.

## Archivo de gestión de dependencias (`requirements.txt`)

- `pip3 freeze > requirements.txt` Crear un archivo con las dependencias instaladas
- `pip3 install -r requirements.txt` Instalar las dependencias del archivo

- https://fakeapi.platzi.com/


## Usando FastAPI

FastAPI es un framework moderno, rápido (alta performance) para construir APIs con Python 3.6+ basado en estándares abiertos para APIs: OpenAPI y JSON Schema.

Para poder crearnos un ambiente virtual, debemos tener instalado el paquete virtualenv. El paquete virtualenv se puede instalar usando PIP.

- `cd folder-name`
- `python3 -m venv env`
- `source env/bin/activate`

- `pip install fastapi`
- `pip install "uvicorn[standard]"`
- `pip freeze > requirements.txt`

Para ejecutar el servidor, debemos ejecutar el siguiente comando:

- `uvicorn main:app --reload`


## ¿Qué es Docker?

Docker es una plataforma de código abierto que permite crear, probar e implementar aplicaciones rápidamente. Docker usa contenedores para permitir que las aplicaciones se ejecuten rápidamente en cualquier entorno, sin importar si es en un servidor, una máquina virtual o en la nube.

Puede ocurrer que en algunos ambientes se use diferentes versiones de Python. Por ejemplo, en un entorno de desarrollo, se puede usar Python 3.8, mientras que en un entorno de producción, se puede usar Python 3.6. Para evitar este problema, se puede usar Docker para crear un contenedor con Python 3.8, y luego ejecutar el código en el contenedor.

[Instalación de Docker](https://platzi.com/clases/4261-python-pip/55136-instalacion-de-docker/)
[Video instalación de Docker en WSL](https://www.youtube.com/watch?v=ZO4KWQfUBBc)

Luego que se instala Docker, se debe crear una imagen de Docker. Una imagen de Docker es un archivo de solo lectura que contiene un sistema de archivos, junto con algunos metadatos. Una imagen de Docker se puede usar para crear contenedores. Un contenedor es una instancia de ejecución de una imagen de Docker.

- Crear un archivo `Dockerfile` en la raíz del proyecto

```dockerfile	
FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade  -r /app/requirements.txt
COPY . /app

CMD bash -c "while true; do sleep 1; done"
```

Para correr el contenedor, se debe crear un archivo `docker-compose.yml` en la raíz del proyecto

```yml
services:
    app:
        build:
        context: .
        dockerfile: Dockerfile
```

- `docker-compose build` Crear el contenedor
- `docker-compose up -d` Lanzar el contenedor
- `docker-compose ps` Ver los contenedores y el estado
- `docker-compose exec app bash` Entrar al contenedor
- `exit` Salir del contenedor

- `docker-compose down` Detener el contenedor
- `docker-compose up -d --build` Re-construir el contenedor
- `docker-compose exec app bash` Entrar al contenedor
- `pyhton main.py` Ejecutar el programa

En este punto, es como si se estuviera conectando a un servidor remoto.

- `python main.py` Ejecutar el programa


### ¿Por qué es importante usar docker?

- **Docker es una herramienta que nos permite crear contenedores**. Un contenedor es un entorno aislado que nos permite ejecutar aplicaciones de forma segura y confiable. Los contenedores nos permiten ejecutar aplicaciones en cualquier sistema operativo, sin importar si es Linux, Windows o Mac.
Se aisla todo el sistema, incluyendo el lenguaje de programación, las librerías, el sistema operativo, etc. Esto nos permite tener un entorno de desarrollo y producción idénticos.


## Docker para el día a día: auutomatizando la vinculación de archivos

Esto permite tener una experiencia de desarrollo similar a la de un entorno de producción, y lo que nos permite la vinculación de archivos es que podamos modificar el código en nuestro editor de texto favorito, y que los cambios se reflejen en el contenedor.

Para poder vincular archivos, debemos agregar la etiqueta **`volumes`** en el archivo `docker-compose.yml`

```yml
services:
    app:
        build:
        context: .
        dockerfile: Dockerfile
        volumes:
        - .:/app
```

- `docker-compose up -d` Recargar el contenedor


## Dockerizando nuestra API

Para poder dockerizar nuestra API, debemos crear un archivo `Dockerfile` en la raíz del proyecto

```dockerfile
FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

Y crear un archivo `docker-compose.yml` en la raíz del proyecto

```yml
services:
  fastapi:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:
      - "80:80"
```

Debemos estar en la carpeta raíz del proyecto, y ejecutar los siguientes comandos:

- `docker-compose build` Crear el contenedor
- `docker-compose up -d` Lanzar el contenedor
- `docker-compose ps` Ver los contenedores y el estado