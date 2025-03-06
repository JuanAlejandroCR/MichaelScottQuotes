# Michael Scott Bot

Este bot publica frases de Michael Scott en Twitter/X cada 12 horas. Alterna entre frases icónicas obtenidas de la API de *The Office* y frases generadas con IA usando *Hugging Face*.

## 🔹 Instalación y Ejecución

### 1️⃣ **Ejecución sin Docker**
```sh
pip install -r requirements.txt
python src/main.py
```

### 2️⃣ **Ejecución con Docker**
```sh
docker-compose up --build -d
```

## 🔹 Tecnologías utilizadas
- **Python 3.11**
- **Hugging Face** para generación de frases con *Mistral-7B-Instruct*
- **requests** para obtener frases icónicas desde la API de *The Office*
- **schedule** para manejar las publicaciones cada 12 horas
- **tweepy** para interactuar con la API de Twitter/X
- **python-dotenv** para la gestión de variables de entorno
- **transformers** y **torch** para el procesamiento de IA
- **Docker** para contenerizar el bot

---
# That's what she said! 🎉
