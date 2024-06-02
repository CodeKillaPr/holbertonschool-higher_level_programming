# Usa la imagen base de Alpine
FROM alpine:latest

# Instala el paquete curl
RUN apk add --no-cache curl

# Copia el archivo config.txt a /app/config.txt en el contenedor
COPY config.txt /app/config.txt

# Define el punto de entrada por defecto (esto es opcional y puede ser ajustado según sea necesario)
CMD ["sh"]
