import openai
import json
from dotenv import load_dotenv
import os

# from data.data_set import courses, test_dates, time_slots, rooms, room_capacity, students, faculty_availability
from data.database import courses, time_slots, rooms, room_capacity, students, faculty_availability


# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY_2')


# Set up OpenAI API key
openai.api_key = API_KEY


def generate_schedule_openai_api(dates):

    # dates = test_dates

    # Build prompt for the API
    prompt = f"""
    You are an AI tasked with scheduling exams. The constraints are as follows:
    1. There are the following courses: {', '.join(courses)}.
    2. Students are enrolled in specific courses: {students}.
    3. Time slots for exams are: {', '.join(time_slots)}.
    4. Exam dates are: {', '.join(dates)}.
    5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
    6. Faculty availability is as follows: {faculty_availability}.
    7. No student can have overlapping exams, and room capacity cannot be exceeded. 
    8. Student can have more than one exam, but it should not overlap.
    9. No faculty member can be assigned to multiple exams at the same time.

    Generate an exam schedule with the following format:
    Table 1: course, date, time, faculty
    Table 2: student, room, time, date

    Make sure that each student is assigned to an exam for all the courses that they are registered for.

    Make sure the name the first table "exams" and the second table "students".

    Return the schedule in structured JSON format.
    """

    # Call OpenAI API using chat model and the correct endpoint
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use GPT-4 model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        # Extract the AI's response (skip the introductory message)
        raw_output = response['choices'][0]['message']['content'].strip()
        
        # Look for the JSON part in the response and extract it
        start_index = raw_output.find("{")
        end_index = raw_output.rfind("}") + 1
        json_output = raw_output[start_index:end_index]

        # Debugging: Print the extracted JSON
        # print("Extracted JSON response:")
        # print(json_output)

        # Parse the extracted JSON output
        schedule = json.loads(json_output)  # Safely parse the JSON string

        # Extract and print tables
        table_1 = schedule['exams']
        table_2 = schedule['students']

        result = { 'exams': table_1, 'students': table_2 }

        return result
    except Exception as e:
        raise Exception(f"An error occurred while using the OpenAI API: {e}")


