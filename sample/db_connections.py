from pymongo import MongoClient
import pprint

class MongoDBConnection(object):
    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

###################   SQL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SQLAlchemyDBConnection(object):
    """SQLAlchemy database connection"""
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.session = None

    def __enter__(self):
        engine = create_engine(self.connection_string)
        Session = sessionmaker()
        self.session = Session(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()