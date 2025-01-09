import os
from dotenv import load_dotenv
from pymongo import MongoClient


# Load environment variables from .env file
load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# Replace the URI string with your MongoDB connection string
client = MongoClient(DATABASE_URI)

# Access a specific database
db = client[DATABASE_NAME]


# Collections
courses_collection = db["courses"]
students_collection = db["students"]
faculty_collection = db["faculty"]
rooms_collection = db["rooms"]
other_details_collection = db["otherDetails"]
timetables_collection = db["timetables"]

# Helper function to convert ObjectId to string
def serialize_document(document):
    document["_id"] = str(document["_id"])
    return document

courses = [course["name"] for course in courses_collection.find()]
print(courses)

students = {f"{student['rollNumber']}_{student['name']}": [course for course in student["courses"]] for student in students_collection.find()}
print(students)

print(other_details_collection.find())

time_slots = other_details_collection.find()[0]["timeSlots"]
print(time_slots)

faculty_availability = {f"{faculty['name']}": faculty["availability"] for faculty in faculty_collection.find()}
print(faculty_availability)

rooms = [room["name"] for room in rooms_collection.find()]
print(rooms)

room_capacity = int(other_details_collection.find()[0]["roomCapacity"])
print(room_capacity)

current_data = {
    "courses": courses,
    "students": students,
    "timeSlots": time_slots,
    "facultyAvailability": faculty_availability,
    "rooms": rooms,
    "roomCapacity": room_capacity
}