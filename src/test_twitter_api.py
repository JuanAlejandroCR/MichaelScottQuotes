import tweepy
import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Configurar credenciales de Twitter desde .env
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Configurar autenticación para la API v2
client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

# Intentar publicar un tweet usando la API v2
try:
    tweet = "Hola, Twitter! 🚀 Esta es una prueba de la API v2."
    response = client.create_tweet(text=tweet)
    print("✅ Tweet publicado correctamente:", response)
except Exception as e:
    print("❌ Error al publicar el tweet:", e)
