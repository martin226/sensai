import os
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from .routes.auth import auth
from .routes.workout import workout

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

CORS(app)
JWTManager(app)


app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(workout, url_prefix="/api/workout")
