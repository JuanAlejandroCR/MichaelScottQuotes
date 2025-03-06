import os
from transformers import pipeline
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener el Token de Hugging Face desde .env
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Verificar si el token está cargado correctamente
if not HUGGINGFACE_API_KEY:
    print("❌ Error: No se encontró el token de Hugging Face en .env")
    exit(1)

# Cargar el modelo de Hugging Face
try:
    generator = pipeline(
        "text-generation",
        model="facebook/opt-6.7b",
        device=-1,  # Usar CPU, cambiar a 0 si tienes GPU
        torch_dtype="auto",
        token=HUGGINGFACE_API_KEY
    )
    print("✅ Modelo cargado correctamente.")
except Exception as e:
    print(f"❌ Error al cargar el modelo: {e}")
    exit(1)

# Probar la generación de texto
prompt = "Eres Michael Scott de The Office. Di algo gracioso sobre el día de hoy."
try:
    response = generator(prompt, max_length=50, truncation=True)
    print("\n✅ Salida del modelo:")
    print(response[0]["generated_text"])
except Exception as e:
    print(f"❌ Error al generar texto: {e}")
