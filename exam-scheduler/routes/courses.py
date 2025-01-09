from flask import Blueprint, request, jsonify
from data.database import courses_collection, serialize_document
from bson.objectid import ObjectId


courses_bp = Blueprint('courses', __name__)


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.json
    course_id = courses_collection.insert_one({"name": data["name"]}).inserted_id
    return jsonify({"message": "Course created", "id": str(course_id)}), 201


@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = list(courses_collection.find())
    return jsonify([serialize_document(course) for course in courses]), 200

@courses_bp.route('/<string:course_id>', methods=['GET'])
def get_course(course_id):
    course = courses_collection.find_one(ObjectId(course_id))
    return jsonify(serialize_document(course)), 200



@courses_bp.route('/<string:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.json
    result = courses_collection.update_one(
        {"_id": ObjectId(course_id)},
        {"$set": {"name": data["name"]}}
    )
    if result.matched_count:
        return jsonify({"message": "Course updated"}), 200
    return jsonify({"error": "Course not found"}), 404


@courses_bp.route('/<string:course_id>', methods=['DELETE'])
def delete_course(course_id):
    result = courses_collection.delete_one({"_id": ObjectId(course_id)})
    if result.deleted_count:
        return jsonify({"message": "Course deleted"}), 200
    return jsonify({"error": "Course not found"}), 404
