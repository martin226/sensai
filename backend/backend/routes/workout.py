from datetime import datetime

from bson.objectid import ObjectId
from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..database import mongo

workout = Blueprint("workout", __name__)

db = mongo["sensai"]
workout_collection = db["workouts"]
users_collection = db["users"]

default_log = {
    "id": "",
    "name": "",
    "workout_id": "",
    "completed": False,
    "created_at": None,
    "completed_at": None,
}


@workout.route("/list", methods=["GET"])
@jwt_required()
def workout_list():
    workouts = list(workout_collection.find())
    for workout in workouts:
        workout["_id"] = str(workout["_id"])
        workout["id"] = workout.pop("_id")
    return make_response(jsonify({"workouts": workouts}))


@workout.route("/<id_>")
@jwt_required()
def workout_get(id_):
    requested_workout = workout_collection.find_one({"_id": ObjectId(id_)})
    requested_workout["_id"] = str(requested_workout["_id"])
    requested_workout["id"] = requested_workout.pop("_id")
    return make_response(jsonify({"workout": requested_workout}), 200)


@workout.route("/start/<workout_id>")
@jwt_required()
def workout_start(workout_id):
    requested_workout = workout_collection.find_one({"_id": ObjectId(workout_id)})
    requested_workout["_id"] = str(requested_workout["_id"])
    requested_workout["id"] = requested_workout.pop("_id")
    current_user = get_jwt_identity()
    user_from_db = users_collection.find_one({"username": current_user})
    if user_from_db:
        new_log = default_log.copy()
        new_log["name"] = requested_workout["name"]
        new_log["id"] = len(user_from_db["workout_log"])
        new_log["workout_id"] = requested_workout["id"]
        new_log["created_at"] = int(datetime.now().timestamp())
        users_collection.update_one(
            filter={"username": current_user},
            update={"$push": {"workout_log": new_log}},
        )

    return make_response(jsonify({"workout": requested_workout, "log": new_log}), 200)


@workout.route("/end/<int:id_>")
@jwt_required()
def workout_end(id_):
    current_user = get_jwt_identity()
    user_from_db = users_collection.find_one({"username": current_user})
    print(user_from_db)
    if user_from_db:
        workout_log = user_from_db["workout_log"]
        for (idx, workout) in enumerate(workout_log):
            print("a")
            print(id_, idx, workout["id"])
            if workout["id"] == id_:
                workout_log[idx]["completed_at"] = int(datetime.now().timestamp())
                workout_log[idx]["completed"] = True
                break
        users_collection.update_one(
            {"username": current_user}, {"$set": {"workout_log": workout_log}}
        )

    return make_response(jsonify({"message": "Ended workout"}), 200)
