from flask import Blueprint, request, jsonify
from data.database import students_collection, serialize_document
from bson.objectid import ObjectId

students_bp = Blueprint('students', __name__)

@students_bp.route('/', methods=['POST'])
def create_student():
    data = request.json
    student_id = students_collection.insert_one({
        "name": data["name"],
        "rollNumber": data["rollNumber"],
        "courses": data["courses"]
    }).inserted_id
    return jsonify({"message": "Student created", "id": str(student_id)}), 201


@students_bp.route('/', methods=['GET'])
def get_students():
    students = list(students_collection.find())
    return jsonify([serialize_document(student) for student in students]), 200


@students_bp.route('/<string:student_id>', methods=['GET'])
def get_student(student_id):
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return jsonify(serialize_document(student)), 200
    return jsonify({"error": "Student not found"}), 404


@students_bp.route('/<string:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": {"name": data["name"], "rollNumber": data["rollNumber"], "courses": data["courses"]}}
    )
    if result.matched_count:
        return jsonify({"message": "Student updated"}), 200
    return jsonify({"error": "Student not found"}), 404


@students_bp.route('/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    result = students_collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count:
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404
