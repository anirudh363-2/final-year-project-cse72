from flask import Blueprint, request, jsonify
from backend.db.operations import execute_query, fetch_data

courses_bp = Blueprint('courses', __name__)

# Create (POST)
@courses_bp.route('/', methods=['POST'])
def create_course():
    try:
        data = request.json

        if not all(field in data for field in ['course_code', 'course_name', 'student_count']):
            return jsonify({"message": "All fields (course_code, course_name, student_count) are required."}), 400
        
        query = "INSERT INTO courses (course_code, course_name, student_count) VALUES (%s, %s, %s)"
        execute_query(query, (data['course_code'], data['course_name'], data['student_count']))
        return jsonify({"message": "Course created successfully"}), 201
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read (GET)
@courses_bp.route('/', methods=['GET'])
def get_courses():
    try:
        query = "SELECT * FROM courses"
        courses = fetch_data(query)
        return jsonify(courses), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read Single (GET)
@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_single_course(course_id):
    try:
        query = "SELECT * FROM courses WHERE id = %s"
        single_course = fetch_data(query, (course_id,))
        return jsonify(single_course[0] if single_course else {"message": "Could not find record"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Update (PUT)
@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    try:
        data = request.json

        if not all(field in data for field in ['course_code', 'course_name', 'student_count']):
            return jsonify({"message": "All fields (course_code, course_name, student_count) are required."}), 400
        
        query = "UPDATE courses SET course_code = %s, course_name = %s, student_count = %s WHERE id = %s"
        values = (data['course_code'], data['course_name'], data['student_count'], course_id)
        execute_query(query, values)
        
        return jsonify({"message": "Course updated successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Delete (DELETE)
@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        query = "DELETE FROM courses WHERE id = %s"
        execute_query(query, (course_id,))
        return jsonify({"message": "Course deleted successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500
