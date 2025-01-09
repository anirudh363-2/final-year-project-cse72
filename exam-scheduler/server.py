import json 

from flask import Flask
from flask_cors import CORS
from routes.courses import courses_bp
from routes.students import students_bp
from routes.faculty import faculty_bp
from routes.rooms import rooms_bp
from routes.other_details import other_details_bp
from routes.timetables import timetables_bp

from data.database import current_data



app = Flask(__name__)

CORS(app, origins="http://localhost:5173", methods=['GET', 'POST', 'PUT', 'DELETE'])


app.register_blueprint(courses_bp, url_prefix='/api/courses')
app.register_blueprint(students_bp, url_prefix='/api/students') 
app.register_blueprint(faculty_bp, url_prefix='/api/faculty')
app.register_blueprint(rooms_bp, url_prefix='/api/rooms')
app.register_blueprint(other_details_bp, url_prefix='/api/other-details')
app.register_blueprint(timetables_bp, url_prefix='/api/timetables')


@app.route('/')
def home():
    return f"""
    <h1>Welcome to the Timetables API</h1>
    <div>
        Current Data: <br />
        <pre>{json.dumps(current_data, indent=4)}</pre>"""


if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == '__main__':      
#     print("\n\nCSP:\n", json.dumps(generate_schedule_csp(), indent=4))
#     print("\n\nGA:\n", json.dumps(generate_schedule_genetic(), indent=4))
#     print("\n\nSA:\n", json.dumps(generate_schedule_simulated_annealing(), indent=4))
#     print("\n\nAI:\n", json.dumps(generate_schedule_openai_api(), indent=4))


