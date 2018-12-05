import pymongo
import datetime

client = pymongo.MongoClient("localhost", 27017)  # Qué significa localhost
db = client.prueba
# db.tweets.ensure_index("id", unique=True, dropDups=True)  # Para evitar problemas
collection = db.tweets

# Rellenar campos similares a un tweet de la API
tweet_id = '279974'  # El Tweet ID de Twitter en formato string
username = 'Relampague'  # El nombre del usuario del tweet
followers = 417  # Número de seguidores del usuario
text = 'Estoy en el curso de python de la US'  # El texto del tweet
language = 'es'  # El idioma del tweet
created = datetime.datetime.now()  # La fecha del tweet

# Cargar todas estas características en un diccionario
tweet = {'_id': tweet_id,
		 'username':username,
		 'followers':followers,
		 'text':text,
		 'language':language,
		 'created':created}

# Guardar este diccionario en MongoDB
collection.save(tweet)
