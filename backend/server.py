from flask import Flask
from backend.routes.faculty import faculty_bp
from backend.routes.courses import courses_bp
from backend.routes.rooms import rooms_bp
from backend.routes.exams import exams_bp
from backend.routes.generate_timetable import generate_timetable_bp

# from backend.routes.generate_csp import generate_csp_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(faculty_bp, url_prefix='/api/faculty')
app.register_blueprint(courses_bp, url_prefix='/api/courses')
app.register_blueprint(rooms_bp, url_prefix='/api/rooms')
app.register_blueprint(exams_bp, url_prefix='/api/exams')
app.register_blueprint(generate_timetable_bp, url_prefix='/api/generate_timetable')

if __name__ == "__main__":
    app.run(debug=True)