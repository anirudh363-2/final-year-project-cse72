from flask import Blueprint, request, jsonify
from data.database import faculty_collection, serialize_document
from bson.objectid import ObjectId

faculty_bp = Blueprint('faculty', __name__)

@faculty_bp.route('/', methods=['POST'])
def create_faculty():
    data = request.json
    faculty_id = faculty_collection.insert_one({
        "name": data["name"],
        "availability": data["availability"],
    }).inserted_id
    return jsonify({"message": "Faculty created", "id": str(faculty_id)}), 201

@faculty_bp.route('/', methods=['GET'])
def get_faculty():
    faculty = list(faculty_collection.find())
    return jsonify([serialize_document(faculty) for faculty in faculty]), 200

@faculty_bp.route('/<string:faculty_id>', methods=['GET'])
def get_single_faculty(faculty_id):
    faculty = faculty_collection.find_one({"_id": ObjectId(faculty_id)})
    if faculty:
        return jsonify(serialize_document(faculty)), 200
    return jsonify({"error": "Faculty not found"}), 404

@faculty_bp.route('/<string:faculty_id>', methods=['PUT'])
def update_faculty(faculty_id):
    data = request.json
    result = faculty_collection.update_one(
        {"_id": ObjectId(faculty_id)},
        {"$set": {"name": data["name"], "availability": data["availability"]}}
    )   
    if result.matched_count:
        return jsonify({"message": "Faculty updated"}), 200
    return jsonify({"error": "Faculty not found"}), 404

@faculty_bp.route('/<string:faculty_id>', methods=['DELETE'])
def delete_faculty(faculty_id):
    result = faculty_collection.delete_one({"_id": ObjectId(faculty_id)})
    if result.deleted_count:
        return jsonify({"message": "Faculty deleted"}), 200
    return jsonify({"error": "Faculty not found"}), 404