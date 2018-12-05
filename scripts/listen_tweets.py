from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import configparser  # Explicar
import json

keywords = ['España']
language = ['es']

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['API']['consumer_key']
consumer_secret = config['API']['consumer_secret']
access_token = config['API']['access_token']
access_token_secret = config['API']['access_token_secret']

class StdOutListener(StreamListener):

    def on_data(self, data):

        # Carga el JSON de la API como un diccionario
        t = json.loads(data)

        print(t)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=keywords, languages=language)
