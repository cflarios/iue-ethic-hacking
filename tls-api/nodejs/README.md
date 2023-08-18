# Autenticación Mutua con Certificados en Node.js

Cómo configurar autenticación mutua utilizando certificados en una REST API construida con Node.js y OpenSSL.

## Paso 1: Generar Certificados de Servidor

1. Crea una carpeta llamada `server-cert` (o el nombre que quieras) en el directorio de tu proyecto.

2. Genera los certificados auto-firmados utilizando OpenSSL. Ejecuta estos comandos en la terminal:
   
   ```bash
   # Generar la clave privada
   openssl genpkey -algorithm RSA -out cert/private-key.pem
   

   # Generar el certificado público firmado por la clave privada
   openssl req -new -key cert/private-key.pem -out cert/certificate.csr
   openssl x509 -req -signkey cert/private-key.pem -in cert/certificate.csr -out cert/public-cert.pem
   ```

## Paso 2: Generar Certificados de Cliente

1. Crea una carpeta llamada `client-cert` (o el nombre que quieras) en el directorio de tu proyecto.

2. Genera una clave privada para el cliente:

   ```bash
   openssl genpkey -algorithm RSA -out client-cert/private-key.pem
   ```
3. Genera una solicitud de firma de certificado (CSR) para el cliente:
   
   ```bash
   openssl req -new -key client-cert/private-key.pem -out client-cert/certificate.csr
   ```
4. Firma el CSR con la clave privada del servidor (esto simula que el servidor actúa como una autoridad de certificación):

   ```bash
   openssl x509 -req -signkey client-cert/private-key.pem -in client-cert/certificate.csr -out client-cert/public-cert.pem
   ```
## Paso 3: Configurar el Servidor para Autenticación de Cliente

1. Modifica el código de tu servidor (archivo `index.js` o en este caso `server.js`) para habilitar la autenticación de cliente:

```
// ...

// Opciones para TLS/SSL
const options = {
  key: fs.readFileSync('cert/private-key.pem'),
  cert: fs.readFileSync('cert/public-cert.pem'),
  requestCert: true,
  rejectUnauthorized: true,
  ca: fs.readFileSync('client-cert/public-cert.pem')
};

// ...

// Verificar la autenticación del cliente
app.use((req, res, next) => {
  if (req.client.authorized) {
    next();
  } else {
    res.status(401).send('No autorizado. Certificado de cliente inválido.');
  }
});

// ...

// Iniciar el servidor
server.listen(port, () => {
  console.log(`Servidor en funcionamiento en https://localhost:${port}`);
});
```
## Paso 4: Realizar pruebas

1. Utiliza `curl` o cualquier otra herramienta similar para realizar solicitudes al servidor utilizando certificados de cliente:

    ```bash
    curl --cert client-cert/public-cert.pem --key client-cert/private-key.pem --cacert cert/public-cert.pem https://localhost:${port}/authenticate
    ```

## EXTRA: Uso de Docker

Si se desea usar una imagen de Docker, solo se necesitan unos cuantos pasos.

1. Construir la imagen de Docker:

Abre una terminal en el mismo directorio que los archivos y el Dockerfile, y ejecuta el siguiente comando para construir la imagen de Docker:

```bash
docker build -t node_ssl_api:1.0 .
```

Esto creará una imagen llamada `node_ssl_api` con la versión `1.0`.

2. Ejecutar un contenedor con la imagen:

Una vez que la imagen esté construida, puedes ejecutar un contenedor basado en ella con el siguiente comando:

```bash
docker run -p 4433:4433 node_ssl_api:1.0   
```

**NOTA**: Este contenedor solo tendrá el `servidor`, el `cliente` se ejecuta desde tu máquina host.