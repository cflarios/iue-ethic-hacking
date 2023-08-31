# API REST Básica con Python y Flask

Este es un ejemplo de una API REST sencilla construida utilizando Python y el framework Flask. La API gestiona una lista de tareas (ToDo's) y permite realizar operaciones básicas como obtener todos los elementos, agregar nuevos elementos y eliminar elementos por índice.

## Instalación

1. Asegúrate de tener [Python](https://www.python.org/) instalado en tu máquina.

2. Clona o descarga este repositorio.

3. Abre una terminal y navega hasta el directorio del proyecto.

4. Instala Flask utilizando el siguiente comando:

   ```bash
   pip install Flask
   ```

## Uso

1. Ejecuta la aplicación utilizando el siguiente comando:
  
   ```bash
   python app.py
   ```
2. Accede a la API utilizando un navegador web o herramientas como `curl`:
 
  - Obtener todos los elementos:

    ```bash
    curl http://localhost:5000/data
    ```
  - Agregar un elemento:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"task": "Hacer compras"}' http://localhost:5000/data
    ```
3. Eliminar un elemento por su índice:

    ```bash
    curl -X DELETE http://localhost:5000/data/0
    ```

## Ejemplo de Datos

La API utiliza una lista de tareas (data) como datos de ejemplo. Algunos elementos de ejemplo:

- Hacer la compra
- Estudiar para el examen
- Ir al gym

## EXTRA: Uso de Docker

Si se desea usar una imagen de Docker, solo se necesitan unos cuantos pasos.

1. Construir la imagen de Docker:

    Abre una terminal en el mismo directorio que los archivos y el Dockerfile, y ejecuta el siguiente comando para construir la imagen de Docker:

    ```bash
    docker build -t python_basic_api:1.0 .
    ```

    Esto creará una imagen llamada `python_basic_api` con la versión `1.0`.

2. Ejecutar un contenedor con la imagen:

    Una vez que la imagen esté construida, puedes ejecutar un contenedor basado en ella con el siguiente comando:

    ```bash
    docker run -p 5000:5000 python_basic_api:1.0   
    ```