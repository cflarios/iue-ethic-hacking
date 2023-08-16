# Conexión TLS simple

Cómo configurar autenticación TLS entre cliente y servidor usando Python.

## Paso 1: Generar Certificados de Servidor

1. Genera los certificados auto-firmados utilizando OpenSSL. Ejecuta estos comandos en la terminal:
   
   ```bash
   # Generar certificado

   openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem -subj "/C=CO/ST=Antioquia/L=Medellin/O=IUE/OU=Hackeo_etico/CN=cflarios/emailAddress=cflarios@correo.iue.edu.co"
   ```


- **C**, el cual es un código de 2 letras para un país, ej: CO (Colombia)
- **ST**, el cual es el nombre del estado o la provincia, ej: Antioquia;
- **L** *(opcional)*, el cual es el nombre de la ciudad, ej: Medellin;
- **O**, es el nombre de la organización;
- **OU** *(opcional)*, es el nombre del departamento de la organización;
- **CN**, el cual es el hostname:
  - **Warning** Si cambias el valor de **CN**, tendrás que cambiar la variable 'hostname' en el archivo [client.py](client.py) con la que elegiste.
- **emailAddress** *(opcional)*, es el correo electrónico.

## Paso 2: Correr el servidor

Abre una terminal e introduce el siguiente comando:

```bash
python3 server.py
```

## Paso 3: Correr el cliente

Abre una terminal e introduce el siguiente comando:

```bash
python3 client.py
```