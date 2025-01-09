from flask import Blueprint, request, jsonify
from data.database import timetables_collection, serialize_document
from bson.objectid import ObjectId

from tools.ai_generated  import generate_schedule_openai_api
from tools.genetic_algorithm import generate_schedule_genetic
from tools.constraint_satisfaction import generate_schedule_csp
from tools.simulated_annealing import generate_schedule_simulated_annealing

from tools.get_dates import get_dates_excluding_sundays

timetables_bp = Blueprint('timetables', __name__)


@timetables_bp.route('/', methods=['POST'])
def create_timetables():
    try:
        # Get the input data
        data = request.json

        # Generate the list of dates excluding Sundays
        dates = get_dates_excluding_sundays(data["start_date"], data["end_date"])

        # Methods dictionary for generating schedules
        methods = {
            "ConstraintSatisfactionProblem": generate_schedule_csp(dates),
            "GeneticAlgorithm": generate_schedule_genetic(dates),
            "SimulatedAnnealing": generate_schedule_simulated_annealing(dates),
            "OpenAI": generate_schedule_openai_api(dates)
        }

        # Insert timetable into database
        timetables_id = timetables_collection.insert_one({
            "name": data["name"],
            "methods": methods
        }).inserted_id

        # Return success response
        return jsonify({"message": "Timetables created", "id": str(timetables_id), "name": data["name"]}), 201

    except Exception as e:
        # Return error response with HTTP 500 and error message
        return jsonify({"message": "An error occurred while generating the timetable", "error": str(e)}), 500
    
    

@timetables_bp.route('/', methods=['GET'])
def get_timetables():
    timetables = list(timetables_collection.find())
    return jsonify([serialize_document(timetables) for timetables in timetables]), 200

@timetables_bp.route('/<string:timetables_id>', methods=['GET'])
def get_timetable(timetables_id):
    timetables = timetables_collection.find_one({"_id": ObjectId(timetables_id)})
    if timetables:
        return jsonify(serialize_document(timetables)), 200
    return jsonify({"error": "Timetables not found"}), 404

@timetables_bp.route('/<string:timetables_id>', methods=['PUT'])
def update_timetables(timetables_id):
    data = request.json
    result = timetables_collection.update_one(
        {"_id": ObjectId(timetables_id)},
        {"$set": {"name": data["name"], "methods": data["methods"]}
    })
    if result.matched_count:
        return jsonify({"message": "Timetables updated"}), 200
    return jsonify({"error": "Timetables not found"}), 404

@timetables_bp.route('/<string:timetables_id>', methods=['DELETE'])
def delete_timetables(timetables_id):
    result = timetables_collection.delete_one({"_id": ObjectId(timetables_id)})
    if result.deleted_count:
        return jsonify({"message": "Timetables deleted"}), 200
    return jsonify({"error": "Timetables not found"}), 404




