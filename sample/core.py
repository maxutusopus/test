from pymongo import MongoClient
#from db_connections


import pprint

# class MongoDBConnection(object):
#     def __init__(self, host='localhost', port=27017):
#         self.host = host
#         self.port = port
#         self.connection = None
#
#     def __enter__(self):
#         self.connection = MongoClient(self.host, self.port)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.close()


mongo = MongoDBConnection()
with mongo:
    collection = mongo.connection.arztdata.arzt
#    arzt = collection.find({'_id': '5729c54ad285a8120c4ef1c5'})
#    print(arzt)
    for doc in collection.find_one({'ll_arzt_id': 'A199291'}):
        pprint.pprint(dir(doc))
