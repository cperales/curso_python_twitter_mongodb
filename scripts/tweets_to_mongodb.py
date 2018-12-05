import pymongo
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import configparser
import datetime

# La información de conexión MongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.prueba
db.tweets.ensure_index("id", unique=True, dropDups=True)
collection = db.tweets

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

        tweet_id = t['id_str']
        username = t['user']['screen_name']
        followers = t['user']['followers_count']
        text = t['text']
        hashtags = t['entities']['hashtags']
        dt = t['created_at']
        print('dt:', dt)
        language = t['lang']

        # Convertir el timestamp string dado por Twitter
        created = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')

        tweet = {'_id':tweet_id, 'id':tweet_id, 'username':username, 'followers':followers, 'text':text, 'hashtags':hashtags, 'language':language, 'created':created}

        collection.save(tweet)

        print(username + ':' + ' ' + text)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=keywords, languages=language)
