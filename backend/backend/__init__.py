import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")
mongo = PyMongo(app)
CORS(app)
