from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import configparser
import json

# Palabras para trackear
keywords = 'España'

# En qué idioma queremos los tweets
language = 'es'

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

for tweet in Cursor(api.search,
					q=keywords,
					since="2018-11-28",
					until="2018-12-05",
					lang=language,
					include_retweets=False).items(20):
	print(tweet)
