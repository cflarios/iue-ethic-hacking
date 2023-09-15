import multiprocessing
import requests
import json
from requests.auth import HTTPBasicAuth

# Función que hace una solicitud GET a localhost:5000 con autenticación básica y verifica el código de estado
def verificar_status_code(numero):
    url = f"http://localhost:5000/usuarios"  # Asegúrate de que tu servidor esté en ejecución en localhost:5000

    # Reemplaza 'usuario' y 'contraseña' con tus credenciales de autenticación básica
    auth = HTTPBasicAuth('user', 'password')

    # Datos que deseas enviar en el cuerpo de la solicitud POST (en este caso, un diccionario)
    data = {"id": "1", "nombre": "Juan", "email": "juan@correo.com"}

    # Convierte el diccionario a JSON antes de enviarlo en el cuerpo de la solicitud
    data_json = json.dumps(data)

    # Especifica el encabezado "Content-Type" para indicar que estás enviando datos JSON
    headers = {'Content-Type': 'application/json'}

    # Realiza la solicitud POST
    respuesta = requests.post(url,auth=auth, data=data_json, headers=headers)
    
    if respuesta.status_code == 200 or respuesta.status_code == 201:
        print(f"Proceso {numero}: El código de estado es 200, la solicitud fue exitosa")
    else:
        print(f"Proceso {numero}: Error - Código de estado {respuesta.status_code}")

if __name__ == "__main__":
    # Lista de números para los cuales queremos verificar el código de estado
    numeros = [1, 2, 3, 4]

    procesos = []

    while True:
        try:
            for numero in numeros:
                proceso = multiprocessing.Process(target=verificar_status_code, args=(numero,))
                proceso.start()
                procesos.append(proceso)
            
            # Esperar a que los procesos terminen (esto no se ejecutará debido al bucle infinito en las funciones)
            for proceso in procesos:
                proceso.join()
        except KeyboardInterrupt:
            # Manejamos la interrupción de teclado (Ctrl+C) para detener los procesos de manera segura
            print("Deteniendo los procesos...")
            for proceso in procesos:
                proceso.terminate()
                proceso.join()