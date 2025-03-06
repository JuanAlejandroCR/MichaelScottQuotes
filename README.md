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
- **requests** para obtener frases de la API de *The Office*
- **schedule** para manejar las publicaciones cada 30 minutos
- **Docker** para contenerizar el bot

¡Diviértete con las frases de Michael Scott! 🎉
