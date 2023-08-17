# Usar una imagen base de Node.js (elige la versión que necesites)
FROM node:14

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de configuración y dependencias
COPY package.json package-lock.json /app/

# Instalar las dependencias del proyecto
RUN npm install

# Copiar el resto de los archivos del proyecto al directorio de trabajo en el contenedor
COPY . /app/

# Exponer el puerto en el que se ejecuta la aplicación
EXPOSE 4433

# Comando para ejecutar la aplicación
CMD ["bash", "-c", "npm run start & sleep 3 && npm run valid-client && sleep 2 && npm run invalid-client"]
