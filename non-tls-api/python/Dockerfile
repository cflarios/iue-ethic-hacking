# Usar una imagen base que tenga Python
FROM python:3.9

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos necesarios al contenedor
COPY requirements.txt .
COPY app.py .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que la API va a estar escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
