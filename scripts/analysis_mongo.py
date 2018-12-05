import pymongo
import datetime

client = pymongo.MongoClient("localhost", 27017)
db = client.prueba
collection = db.tweets

print('Tenemos', collection.count_documents({}), 'documentos')

for doc in collection.find({"lang": "es"}):
	print(doc)

author_list = []
for doc in collection.find():
	author = doc['username']
	if author not in author_list:
		author_list.append(doc['author'])
