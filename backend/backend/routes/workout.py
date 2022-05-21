from flask import Blueprint, jsonify, make_response, request

from ..database import mongo

workout = Blueprint("workout", __name__)

db = mongo["sensai"]
workout_collection = db["workouts"]


@workout.route("/list", methods=["GET"])
def workout_list():
    workouts = list(workout_collection.find())
    for workout in workouts:
        workout["_id"] = str(workout["_id"])
        workout["id"] = workout.pop("_id")
    return make_response(jsonify({"workouts": workouts}))
