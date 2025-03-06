# Dockerfile para el bot de Michael Scott con Ollama

# Usar una imagen base de Python
FROM python:3.11-slim

# Instalar Ollama
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://ollama.com/install.sh | sh

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt .
COPY src/ ./src/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Descargar modelo en Ollama
RUN ollama pull mistral

# Ejecutar el bot
CMD ["python", "src/main.py"]
