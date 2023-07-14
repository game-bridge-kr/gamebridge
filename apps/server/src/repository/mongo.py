from pymongo import MongoClient 
from pymongo.database import Database
from pymongo.collection import Collection
from ..constants import mongo_db_url, mongo_db_database
from enum import Enum


class CollectionEnum(Enum):
    USER = "user"


class MongoDatabase:
    def connect(self):
        self.client = MongoClient(mongo_db_url())
        self.db = self.client.get_database(mongo_db_database())

    def close(self):
        self.client.close()

    def get_database(self) -> Database:
        return self.db

    def get_users(self) -> Collection:
        return self.db.get_collection(CollectionEnum.USER.value)
    

database = MongoDatabase()