from flask import Blueprint, request, jsonify
from backend.db.operations import execute_query, fetch_data

rooms_bp = Blueprint('rooms', __name__)

# Create (POST)
@rooms_bp.route('/', methods=['POST'])
def create_room():
    try:
        data = request.json
        
        if not all(field in data for field in ['room_number', 'capacity']):
            return jsonify({"message": "All fields (room_number, capacity) are required."}), 400

        query = "INSERT INTO rooms (room_number, capacity) VALUES (%s, %s)"
        execute_query(query, (data['room_number'], data['capacity']))
        return jsonify({"message": "Room created successfully"}), 201
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read (GET)
@rooms_bp.route('/', methods=['GET'])
def get_rooms():
    try:
        query = "SELECT * FROM rooms"
        rooms = fetch_data(query)
        return jsonify(rooms), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Read Single (GET)
@rooms_bp.route('/<int:room_id>', methods=['GET'])
def get_single_room(room_id):
    try:
        query = "SELECT * FROM rooms WHERE id = %s"
        single_room = fetch_data(query, (room_id,))
        if single_room:
            return jsonify(single_room[0]), 200
        else:
            return jsonify({"message": "Room not found"}), 404
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Update (PUT)
@rooms_bp.route('/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    try:
        data = request.json

        if not all(field in data for field in ['room_number', 'capacity']):
            return jsonify({"message": "All fields (room_number, capacity) are required."}), 400

        query = "UPDATE rooms SET room_number = %s, capacity = %s WHERE id = %s"
        values = (data['room_number'], data['capacity'], room_id)
        execute_query(query, values)
        
        return jsonify({"message": "Room updated successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500

# Delete (DELETE)
@rooms_bp.route('/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    try:
        query = "DELETE FROM rooms WHERE id = %s"
        execute_query(query, (room_id,))
        return jsonify({"message": "Room deleted successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500
