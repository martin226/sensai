from pymongo import MongoClient
import os

mongo = MongoClient(os.getenv("MONGODB_URI"))
