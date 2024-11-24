from flask import Blueprint, request, jsonify
from backend.db.operations import execute_query, fetch_data

faculty_bp = Blueprint('faculty', __name__)

# Create (POST)
@faculty_bp.route('/', methods=['POST'])
def create_faculty():
    try:
        data = request.json

        if not all(field in data for field in ['faculty_id', 'name']):
            return jsonify({"message": "All fields (faculty_id, name) are required."}), 400
        
        query = "INSERT INTO faculty (faculty_id, name) VALUES (%s, %s)"
        execute_query(query, (data['faculty_id'], data['name']))
        return jsonify({"message": "Faculty created successfully"}), 201
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read (GET)
@faculty_bp.route('/', methods=['GET'])
def get_faculty():
    try:
        query = "SELECT * FROM faculty"
        faculty = fetch_data(query)
        return jsonify(faculty), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read Single (GET)
@faculty_bp.route('/<int:fac_id>', methods=['GET'])
def get_single_faculty(fac_id):
    try:
        query = "SELECT * FROM faculty WHERE id = %s"
        single_faculty = fetch_data(query, (fac_id,))
        return jsonify(single_faculty[0] if single_faculty else {"message": "Could not find record"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500
    
# Update (PUT)
@faculty_bp.route('/<int:fac_id>', methods=['PUT'])
def update_faculty(fac_id):
    try:
        data = request.json

        if not all(field in data for field in ['faculty_id', 'name']):
            return jsonify({"message": "All fields (faculty_id, name) are required."}), 400
        
        query = "UPDATE faculty SET faculty_id = %s, name = %s WHERE id = %s"
        values = (data['faculty_id'], data['name'], fac_id)
        execute_query(query, values)
        
        return jsonify({"message": "Faculty updated successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# Delete (DELETE)
@faculty_bp.route('/<int:fac_id>', methods=['DELETE'])
def delete_student(fac_id):
    try:
        query = "DELETE FROM faculty WHERE id = %s"
        execute_query(query, (fac_id,))
        return jsonify({"message": "Faculty deleted successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500