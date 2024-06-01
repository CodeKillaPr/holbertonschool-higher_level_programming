# Usar la imagen base de Ubuntu
FROM ubuntu:latest

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que la aplicación va a correr (opcional)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["bash"]
