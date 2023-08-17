# Usar una imagen base que tenga Python
FROM python:3.9

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos necesarios al contenedor
COPY client.py .
COPY server.py .
COPY cert.pem .
COPY key.pem .

# Exponer el puerto en el que la API va a estar escuchando
EXPOSE 4443

# Ejecutar el servidor Python en segundo plano (usando "&") y luego el cliente
CMD ["bash", "-c", "python server.py & sleep 3 && python client.py"]
