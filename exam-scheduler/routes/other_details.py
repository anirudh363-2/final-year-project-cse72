from flask import Blueprint, request, jsonify
from data.database import other_details_collection, serialize_document
from bson.objectid import ObjectId

other_details_bp = Blueprint('other_details', __name__)

@other_details_bp.route('/', methods=['POST'])
def create_other_details():
    data = request.json
    other_details_id = other_details_collection.insert_one({
        "timeSlots": data["timeSlots"],
        "roomCapacity": data["roomCapacity"],
    }).inserted_id
    return jsonify({"message": "Other Details created", "id": str(other_details_id)}), 201

@other_details_bp.route('/', methods=['GET'])
def get_other_details():
    other_details = list(other_details_collection.find())
    return jsonify([serialize_document(other_details) for other_details in other_details]), 200

@other_details_bp.route('/<string:other_details_id>', methods=['GET'])
def get_other_detail(other_details_id):
    other_details = other_details_collection.find_one({"_id": ObjectId(other_details_id)})
    if other_details:
        return jsonify(serialize_document(other_details)), 200
    return jsonify({"error": "Other Details not found"}), 404

@other_details_bp.route('/<string:other_details_id>', methods=['PUT'])
def update_other_details(other_details_id):
    data = request.json
    result = other_details_collection.update_one(
        {"_id": ObjectId(other_details_id)},
        {"$set": {"timeSlots": data["timeSlots"], "roomCapacity": data["roomCapacity"]}
    })
    if result.matched_count:
        return jsonify({"message": "Other Details updated"}), 200
    return jsonify({"error": "Other Details not found"}), 404

@other_details_bp.route('/<string:other_details_id>', methods=['DELETE'])
def delete_other_details(other_details_id):
    result = other_details_collection.delete_one({"_id": ObjectId(other_details_id)})
    if result.deleted_count:
        return jsonify({"message": "Other Details deleted"}), 200
    return jsonify({"error": "Other Details not found"}), 404