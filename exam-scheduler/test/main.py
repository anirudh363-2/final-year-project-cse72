 # Input data
courses = ['Math', 'Physics', 'Chemistry', 'Biology']
students = {
    'Student1': ['Math', 'Physics'],
    'Student2': ['Math', 'Chemistry'],
    'Student3': ['Biology', 'Chemistry'],
}
time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
dates = ['2024-12-15', '2024-12-16']
faculty_availability = {
    'Faculty1': ['9 AM', '12 PM'],
    'Faculty2': ['3 PM', '6 PM'],
}
rooms = ['Room1', 'Room2']
room_capacity = 2

try:
    from ortools.sat.python import cp_model
except ModuleNotFoundError:
    print("The 'ortools' library is not installed. Please install it using 'pip install ortools' and try again.")
    exit()

def generate_schedule_csp():
    model = cp_model.CpModel()


    # Variables
    exam_schedule = {}
    for course in courses:
        for date in dates:
            for time in time_slots:
                for room in rooms:
                    exam_schedule[(course, date, time, room)] = model.NewBoolVar(f'{course}_{date}_{time}_{room}')

    faculty_schedule = {}
    for course in courses:
        for date in dates:
            for time in time_slots:
                faculty_schedule[(course, date, time)] = model.NewBoolVar(f'{course}_faculty_{date}_{time}')

    # Constraints
    # Each course should have one time slot, date, and room
    for course in courses:
        model.Add(
            sum(
                exam_schedule[(course, date, time, room)]
                for date in dates
                for time in time_slots
                for room in rooms
            ) == 1
        )

    # No overlapping exams for any student
    for student, student_courses in students.items():
        for date in dates:
            for time in time_slots:
                model.Add(
                    sum(
                        exam_schedule[(course, date, time, room)]
                        for course in student_courses
                        for room in rooms
                    ) <= 1
                )

    # Room capacity constraint
    for date in dates:
        for time in time_slots:
            for room in rooms:
                model.Add(
                    sum(
                        exam_schedule[(course, date, time, room)]
                        for course in courses
                    ) <= room_capacity
                )

    # Faculty availability
    for date in dates:
        for time in time_slots:
            for faculty, available_times in faculty_availability.items():
                if time not in available_times:
                    model.Add(
                        sum(
                            faculty_schedule[(course, date, time)]
                            for course in courses
                        ) == 0
                    )

    # Faculty cannot be assigned to multiple exams at the same time
    for date in dates:
        for time in time_slots:
            for faculty in faculty_availability.keys():
                model.Add(
                    sum(
                        faculty_schedule[(course, date, time)]
                        for course in courses
                    ) <= 1
                )

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        print("CSP Exam Schedule:")
        table_1 = []
        table_2 = []
        for course in courses:
            for date in dates:
                for time in time_slots:
                    for room in rooms:
                        if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
                            faculty = [
                                f for f, times in faculty_availability.items() if time in times
                            ][0]
                            students_in_course = [s for s, sc in students.items() if course in sc]
                            table_1.append([course, date, time, faculty])
                            for student in students_in_course:
                                table_2.append([student, room, time, date])

        # Print Table 1
        print("+------------+------------+--------+----------------+")
        print("|   Course   |    Date    |  Time  |     Faculty    |")
        print("+------------+------------+--------+----------------+")
        for row in table_1:
            print(f"| {row[0]:10} | {row[1]:10} | {row[2]:6} | {row[3]:14} |")
        print("+------------+------------+--------+----------------+")

        # Print Table 2
        print("+------------+-------+--------+------------+")
        print("|   Student  | Room  |  Time  |    Date    |")
        print("+------------+-------+--------+------------+")
        for row in table_2:
            print(f"| {row[0]:10} | {row[1]:5} | {row[2]:6} | {row[3]:10} |")
        print("+------------+-------+--------+------------+")
    else:
        print("No feasible schedule found.")

# 2. Genetic Algorithm
import random

def generate_schedule_genetic():



    def fitness(schedule):
        score = 0
        faculty_schedule = {}
        for course, (date, time, room) in schedule.items():
            faculty = [f for f, at in faculty_availability.items() if time in at][0]
            # Check if faculty already has an exam at this time
            if (faculty, date, time) not in faculty_schedule:
                faculty_schedule[(faculty, date, time)] = course
            else:
                score -= 1  # Penalty if faculty is assigned to multiple courses at the same time
        
        # Check for student schedule conflicts
        for student, student_courses in students.items():
            student_slots = [
                (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
            ]
            if len(set(student_slots)) == len(student_slots):
                score += 1
        return score





    def generate_individual():
        return {
            course: (
                random.choice(dates), 
                random.choice(time_slots), 
                random.choice(rooms)
            ) for course in courses
        }

    def mutate(individual):
        course = random.choice(courses)
        individual[course] = (
            random.choice(dates), 
            random.choice(time_slots), 
            random.choice(rooms)
        )

    population = [generate_individual() for _ in range(100)]

    for _ in range(100):
        population.sort(key=fitness, reverse=True)
        next_generation = population[:10]
        for _ in range(90):
            parent = random.choice(next_generation)
            child = parent.copy()
            mutate(child)
            next_generation.append(child)
        population = next_generation

    best_schedule = max(population, key=fitness)
    table_1 = []
    table_2 = []
    for course, (date, time, room) in best_schedule.items():
        students_in_course = [s for s, sc in students.items() if course in sc]
        faculty = [f for f, at in faculty_availability.items() if time in at][0]
        table_1.append([course, date, time, faculty])
        for student in students_in_course:
            table_2.append([student, room, time, date])

    # Print Table 1
    print("Genetic Algorithm Exam Schedule - Table 1:")
    print("+------------+------------+--------+----------------+")
    print("|   Course   |    Date    |  Time  |     Faculty    |")
    print("+------------+------------+--------+----------------+")
    for row in table_1:
        print(f"| {row[0]:10} | {row[1]:10} | {row[2]:6} | {row[3]:14} |")
    print("+------------+------------+--------+----------------+")

    # Print Table 2
    print("Genetic Algorithm Exam Schedule - Table 2:")
    print("+------------+-------+--------+------------+")
    print("|   Student  | Room  |  Time  |    Date    |")
    print("+------------+-------+--------+------------+")
    for row in table_2:
        print(f"| {row[0]:10} | {row[1]:10} | {row[2]:6} | {row[3]:10} |")
    print("+------------+-------+--------+------------+")


# 3. Simulated Annealing
import math
import random

def generate_schedule_simulated_annealing():


    def energy(schedule):
        penalty = 0
        faculty_schedule = {}
        # Check for faculty scheduling conflicts
        for course, (date, time, room) in schedule.items():
            faculty = [f for f, at in faculty_availability.items() if time in at][0]
            if (faculty, date, time) not in faculty_schedule:
                faculty_schedule[(faculty, date, time)] = course
            else:
                penalty += 1  # Penalty if faculty is assigned to multiple courses at the same time
            
        # Check for student schedule conflicts
        for student, student_courses in students.items():
            student_slots = [
                (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
            ]
            if len(set(student_slots)) != len(student_slots):  # Overlapping exams
                penalty += 1
            
        return penalty





    def random_schedule():
        return {
            course: (
                random.choice(dates), 
                random.choice(time_slots), 
                random.choice(rooms)
            ) for course in courses
        }

    def neighbor(schedule):
        course = random.choice(courses)
        new_schedule = schedule.copy()
        new_schedule[course] = (
            random.choice(dates), 
            random.choice(time_slots), 
            random.choice(rooms)
        )
        return new_schedule

    def acceptance_probability(old_energy, new_energy, temperature):
        if new_energy < old_energy:
            return 1.0
        return math.exp((old_energy - new_energy) / temperature)

    # Simulated Annealing parameters
    current_schedule = random_schedule()
    current_energy = energy(current_schedule)
    temperature = 100.0
    cooling_rate = 0.95

    # Main loop
    while temperature > 1:
        new_schedule = neighbor(current_schedule)
        new_energy = energy(new_schedule)

        if acceptance_probability(current_energy, new_energy, temperature) > random.random():
            current_schedule = new_schedule
            current_energy = new_energy

        temperature *= cooling_rate

    # Generate Tables
    table_1 = []
    table_2 = []
    for course, (date, time, room) in current_schedule.items():
        students_in_course = [s for s, sc in students.items() if course in sc]
        faculty = [f for f, at in faculty_availability.items() if time in at][0]
        table_1.append([course, date, time, faculty])
        for student in students_in_course:
            table_2.append([student, room, time, date])

    # Print Table 1
    print("Simulated Annealing Exam Schedule - Table 1:")
    print("+------------+------------+--------+----------------+")
    print("|   Course   |    Date    |  Time  |     Faculty    |")
    print("+------------+------------+--------+----------------+")
    for row in table_1:
        print(f"| {row[0]:10} | {row[1]:10} | {row[2]:6} | {row[3]:14} |")
    print("+------------+------------+--------+----------------+")

    # Print Table 2
    print("Simulated Annealing Exam Schedule - Table 2:")
    print("+------------+-------+--------+------------+")
    print("|   Student  | Room  |  Time  |    Date    |")
    print("+------------+-------+--------+------------+")
    for row in table_2:
        print(f"| {row[0]:10} | {row[1]:5} | {row[2]:6} | {row[3]:10} |")
    print("+------------+-------+--------+------------+")



import openai

# Set up OpenAI API key
openai.api_key = ""


import json

def generate_schedule_openai_api():

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
    8. No faculty member can be assigned to multiple exams at the same time.

    Generate an exam schedule with the following format:
    Table 1: course, date, time, faculty
    Table 2: student, room, time, date

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
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract the AI's response (skip the introductory message)
        raw_output = response['choices'][0]['message']['content'].strip()
        
        # Look for the JSON part in the response and extract it
        start_index = raw_output.find("{")
        end_index = raw_output.rfind("}") + 1
        json_output = raw_output[start_index:end_index]

        # Debugging: Print the extracted JSON
        print("Extracted JSON response:")
        print(json_output)

        # Parse the extracted JSON output
        schedule = json.loads(json_output)  # Safely parse the JSON string

        # Extract and print tables
        table_1 = schedule['exams']
        table_2 = schedule['students']

        # Print Table 1
        print("OpenAI API Exam Schedule - Table 1:")
        print("+------------+------------+--------+----------------+")
        print("|   Course   |    Date    |  Time  |     Faculty    |")
        print("+------------+------------+--------+----------------+")
        for row in table_1:
            print(f"| {row['course']:10} | {row['date']:10} | {row['time']:6} | {row['faculty']:14} |")
        print("+------------+------------+--------+----------------+")

        # Print Table 2
        print("OpenAI API Exam Schedule - Table 2:")
        print("+------------+-------+--------+------------+")
        print("|   Student  | Room  |  Time  |    Date    |")
        print("+------------+-------+--------+------------+")
        for row in table_2:
            print(f"| {row['student']:10} | {row['room']:5} | {row['time']:6} | {row['date']:10} |")
        print("+------------+-------+--------+------------+")

    except Exception as e:
        print(f"An error occurred while using the OpenAI API: {e}")



if __name__ == '__main__':      
    generate_schedule_csp()
    generate_schedule_genetic()
    generate_schedule_simulated_annealing()
    generate_schedule_openai_api()

