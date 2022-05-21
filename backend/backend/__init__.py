from datetime import timedelta
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from .routes.auth import auth
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

CORS(app)
JWTManager(app)


app.register_blueprint(auth, url_prefix="/api/auth")
