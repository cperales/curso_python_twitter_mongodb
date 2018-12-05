from tweepy import OAuthHandler
from tweepy import API
import configparser
import json

# Palabras para trackear
keywords = ['España']

# En qué idioma queremos los tweets
language = ['es']

# Leer valores del archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['API']['consumer_key']
consumer_secret = config['API']['consumer_secret']
access_token = config['API']['access_token']
access_token_secret = config['API']['access_token_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)
api.update_status('Twitteando usando la autentificación OAuth via Tweepy!') 
