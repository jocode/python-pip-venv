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