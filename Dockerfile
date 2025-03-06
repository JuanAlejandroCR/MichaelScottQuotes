# Dockerfile para el bot de Michael Scott con Hugging Face

# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt .
COPY src/ ./src/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establecer caché para modelos de Hugging Face
ENV HF_HOME=/root/.cache/huggingface

# Ejecutar el bot
CMD ["python", "src/main.py"]
