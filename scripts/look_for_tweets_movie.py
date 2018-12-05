from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import configparser
import json
import pymongo

# Palabras para trackear
keywords = 'Fantastic', 'Beasts'

# En qué idioma queremos los tweets
language = 'en'

# Leer valores del archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['API']['consumer_key']
consumer_secret = config['API']['consumer_secret']
access_token = config['API']['access_token']
access_token_secret = config['API']['access_token_secret']

# Conectamos con la API de Twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

# La información de conexión MongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.tweets
db.movie.ensure_index("id", unique=True, dropDups=True)
collection = db.movie

for tweet in Cursor(api.search,
                    q=keywords,
                    since="2018-11-28",
                    until="2018-12-05",
                    lang=language,
                    include_retweets=False).items(1000):
    t = tweet._json  # Realmente es un diccionario
    collection.save(t)
