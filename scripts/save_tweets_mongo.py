import pymongo
import json

# Creamos la conexión
client = pymongo.MongoClient("localhost", 27017)
db = client.tweets
collection = db.movie

# Para guardar
list_tweets = [tweet for tweet in collection.find()] 

with open('backup_tweets.json', 'w') as outfile:
    json.dump(list_tweets, outfile, default=str)

# Para insertar
with open('backup_tweets.json', 'r') as infile:
    list_tweets_2 = json.load(infile)
    for tweet in list_tweets_2:
        try:
            collection.save(tweet)
        except:
            id_conflict = tweet.pop('_id')
            collection.update_one({'_id': id_conflict},
                                  {'$set': tweet},
                                  upsert=False)
