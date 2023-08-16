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