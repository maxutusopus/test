# from pymongo import MongoClient

from sample import db_connections as m
import pprint

import time



def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('Elapsed time:{}'.format(te-ts))

        return result

    return timed

@timeit
def test():
    w = 1 + 1
    print(w)


test()

mongo = m.MongoDBConnection()
with mongo:
    collection = mongo.connection.arztdata.arzt
    #    arzt = collection.find({'_id': '5729c54ad285a8120c4ef1c5'})
    #    print(arzt)
    result = ()
    for i, doc in enumerate(collection.find()):
        # print(i, doc['nachname'])
        result = i

    print(result)


