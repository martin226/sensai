from flask import Blueprint, jsonify, make_response
from bson.objectid import ObjectId

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


@workout.route("/<id_>")
def workout_get(id_):
    requested_workout = workout_collection.find_one({"_id": ObjectId(id_)})
    requested_workout["_id"] = str(requested_workout["_id"])
    requested_workout["id"] = requested_workout.pop("_id")
    return make_response(jsonify({"workout": requested_workout}), 200)
