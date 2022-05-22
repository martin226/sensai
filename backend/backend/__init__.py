import base64
import os
from datetime import timedelta
from io import BytesIO

import numpy as np
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from PIL import Image
from engineio.payload import Payload

from .ai import class_map
from .routes.auth import auth
from .routes.workout import workout


from threading import Lock

import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

CORS(app)
JWTManager(app)
Payload.max_decode_packets = 50
socket = SocketIO(app, path="/api/coach", cors_allowed_origins="*")


app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(workout, url_prefix="/api/workout")


thread = None
thread_lock = Lock()


def background_thread(data):
    global thread
    try:
        frame = data["frame"]
        reps = data["reps"]
        exercise = data["exercise"]
        prev_state = data["prevState"]
        if exercise not in class_map:
            return

        decoded = base64.b64decode(frame)
        img = np.array(Image.open(BytesIO(decoded)))
        result = class_map[exercise](img, reps, prev_state)
        socket.emit(
            "coach",
            {
                "reps": result.reps,
                "formHint": result.form_hint,
                "state": result.state,
                "exercise": exercise,
            },
        )
    finally:
        thread = None


@socket.on("frame")
def handle_frame(data):
    global thread
    with thread_lock:
        if thread is None:
            thread = socket.start_background_task(background_thread, data)
