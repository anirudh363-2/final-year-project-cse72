from flask import Blueprint, request, jsonify
from data.database import rooms_collection, serialize_document
from bson.objectid import ObjectId

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/', methods=['POST'])
def create_room():
    data = request.json
    room_id = rooms_collection.insert_one({
        "name": data["name"]
    }).inserted_id
    return jsonify({"message": "Room created", "id": str(room_id)}), 201

@rooms_bp.route('/', methods=['GET'])
def get_rooms():
    rooms = list(rooms_collection.find())
    return jsonify([serialize_document(room) for room in rooms]), 200

@rooms_bp.route('/<string:room_id>', methods=['GET'])
def get_room(room_id):
    room = rooms_collection.find_one({"_id": ObjectId(room_id)})
    if room:
        return jsonify(serialize_document(room)), 200
    return jsonify({"error": "Room not found"}), 404

@rooms_bp.route('/<string:room_id>', methods=['PUT'])
def update_room(room_id):
    data = request.json
    result = rooms_collection.update_one(
        {"_id": ObjectId(room_id)},
        {"$set": {"name": data["name"]}}
    )
    if result.matched_count:
        return jsonify({"message": "Room updated"}), 200
    return jsonify({"error": "Room not found"}), 404

@rooms_bp.route('/<string:room_id>', methods=['DELETE'])
def delete_room(room_id):
    result = rooms_collection.delete_one({"_id": ObjectId(room_id)})
    if result.deleted_count:
        return jsonify({"message": "Room deleted"}), 200
    return jsonify({"error": "Room not found"}), 404