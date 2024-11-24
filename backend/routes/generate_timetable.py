from backend.tools.csp import schedule_exams
from flask import Blueprint, request, jsonify


generate_timetable_bp = Blueprint('generate_timetable', __name__)

# Generate Timetable (POST)
@generate_timetable_bp.route('/', methods=['POST'])
def generate_timetable():
    """Generate timetable using Constraint Satisfaction Problem (CSP)"""
    try:
        data = request.json
        return jsonify(schedule_exams(data['start_date'], data['end_date'], data['exam_name'])), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "An error occurred"}), 500