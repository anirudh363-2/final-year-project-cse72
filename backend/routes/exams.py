from flask import Blueprint, request, jsonify
from backend.db.operations import execute_query, fetch_data

exams_bp = Blueprint('exams', __name__)

# Create (POST)
@exams_bp.route('/', methods=['POST'])
def create_exam():
    try:
        data = request.json

        if not all(field in data for field in ['course_id', 'exam_date', 'exam_time', 'room_id', 'faculty_id', 'exam_name']):
            return jsonify({"message": "All fields (course_id, exam_date, exam_time, room_id, faculty_id, exam_name) are required."}), 400
        
        query = "INSERT INTO exams (course_id, exam_date, exam_name, exam_time, room_id, faculty_id) VALUES (%s, %s, %s, %s, %s, %s)"
        execute_query(query, (data['course_id'], data['exam_date'], data['exam_name'], data['exam_time'], data['room_id'], data['faculty_id']))
        return jsonify({"message": "Exam created successfully"}), 201
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read (GET)
@exams_bp.route('/', methods=['GET'])
def get_exams():
    try:
        query = "SELECT * FROM exams"
        exams = fetch_data(query)
        return jsonify(exams), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read Single (GET)
@exams_bp.route('/<int:exam_id>', methods=['GET'])
def get_single_exam(exam_id):
    try:
        query = "SELECT * FROM exams WHERE id = %s"
        single_exam = fetch_data(query, (exam_id,))
        return jsonify(single_exam[0] if single_exam else {"message": "Could not find record"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500
    
# Update (PUT)
@exams_bp.route('/<int:exam_id>', methods=['PUT'])
def update_exam(exam_id):
    try:
        data = request.json

        if not all(field in data for field in ['course_id', 'exam_date', 'exam_time', 'room_id', 'faculty_id', 'exam_name']):
            return jsonify({"message": "All fields (course_id, exam_date, exam_time, room_id, faculty_id, exam_name) are required."}), 400
        
        query = "UPDATE exams SET course_id = %s, exam_date = %s, exam_name = %s,  exam_time = %s, room_id = %s, faculty_id = %s WHERE id = %s"
        values = (data['course_id'], data['exam_date'], data['exam_name'], data['exam_time'], data['room_id'], data['faculty_id'],  exam_id)
        execute_query(query, values)
        
        return jsonify({"message": "Exam updated successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Delete (DELETE)
@exams_bp.route('/<int:exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    try:
        query = "DELETE FROM exams WHERE id = %s"
        execute_query(query, (exam_id,))
        return jsonify({"message": "Exam deleted successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500
