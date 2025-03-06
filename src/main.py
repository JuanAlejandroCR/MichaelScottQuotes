from abc import ABC, abstractmethod
import random
import datetime
import os
import schedule
import time
import requests
import tweepy
from dotenv import load_dotenv
from transformers import pipeline

# Cargar variables desde .env
load_dotenv()

# Configuración de credenciales de Twitter
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Validar que las credenciales se cargaron correctamente
if not all([TWITTER_BEARER_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, HUGGINGFACE_API_KEY]):
    print("❌ Error: No se encontraron todas las credenciales en el .env")
    exit(1)

# Configurar cliente de Twitter usando API v2
client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

# Cargar modelo de Hugging Face (mejor calidad de generación de texto)
generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct", device=-1, torch_dtype="auto", token=HUGGINGFACE_API_KEY)

# Interfaz para la fábrica de frases
class PhraseFactory(ABC):
    @abstractmethod
    def get_phrase(self):
        pass

# Fábrica para frases estáticas de la serie obtenidas de una API
class StaticPhraseFactory(PhraseFactory):
    API_URL = "https://officeapi.akashrajpurohit.com/quote/random"
    
    def get_phrase(self):
        while True:
            response = requests.get(self.API_URL)
            if response.status_code == 200:
                data = response.json()
                if data.get('character') == 'Michael Scott':
                    return data.get('quote', "That's what she said!")
        return "That's what she said!"

# Fábrica para frases dinámicas usando Hugging Face
class DynamicPhraseFactory(PhraseFactory):
    def get_phrase(self):
        today = datetime.datetime.now()
        date_str = today.strftime("%d de %B")
        prompt = f"Eres Michael Scott de The Office. Di algo gracioso sobre el día {date_str}."
        
        response = generator(prompt, max_length=50, truncation=True)
        return response[0]["generated_text"]

# Cliente que usa la fábrica
class PhraseGenerator:
    def __init__(self, factory: PhraseFactory):
        self.factory = factory

    def generate_phrase(self):
        return self.factory.get_phrase()

# Función para alternar frases y programar publicaciones
static_factory = StaticPhraseFactory()
dynamic_factory = DynamicPhraseFactory()

static_generator = PhraseGenerator(static_factory)
dynamic_generator = PhraseGenerator(dynamic_factory)

publish_static = True

def post_phrase():
    global publish_static
    phrase = static_generator.generate_phrase() if publish_static else dynamic_generator.generate_phrase()
    publish_static = not publish_static  # Alternar entre frases estáticas y dinámicas
    print("Publicando frase en Twitter:", phrase)
    try:
        response = client.create_tweet(text=phrase)
        print("✅ Publicación exitosa", response)
    except Exception as e:
        print("❌ Error al publicar en Twitter:", e)

# Programar ejecución cada 12 horas
schedule.every(12).hours.do(post_phrase)

if __name__ == "__main__":
    print("Bot de Michael Scott iniciado...")
    while True:
        schedule.run_pending()
        time.sleep(10)
