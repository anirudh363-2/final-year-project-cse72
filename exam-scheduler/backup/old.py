# # # 1. Constraint Satisfaction Problem (CSP)
# # from ortools.sat.python import cp_model

# # def generate_schedule_csp():
# #     model = cp_model.CpModel()

# #     # Example input data
# #     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
# #     students = {
# #         'Student1': ['Math', 'Physics'],
# #         'Student2': ['Math', 'Chemistry'],
# #         'Student3': ['Biology', 'Chemistry'],
# #     }
# #     time_slots = [0, 1, 2, 3]
# #     faculty_availability = {
# #         'Faculty1': [0, 1],
# #         'Faculty2': [2, 3],
# #     }
# #     room_capacity = 2
# #     rooms = ['Room1', 'Room2']

# #     # Variables
# #     exam_schedule = {}
# #     for course in courses:
# #         for slot in time_slots:
# #             for room in rooms:
# #                 exam_schedule[(course, slot, room)] = model.NewBoolVar(f'{course}_{slot}_{room}')

# #     # Constraints
# #     for course in courses:
# #         model.Add(sum(exam_schedule[(course, slot, room)] for slot in time_slots for room in rooms) == 1)

# #     for student, student_courses in students.items():
# #         for slot in time_slots:
# #             model.Add(
# #                 sum(exam_schedule[(course, slot, room)] for course in student_courses for room in rooms) <= 1
# #             )

# #     for slot in time_slots:
# #         for room in rooms:
# #             model.Add(
# #                 sum(exam_schedule[(course, slot, room)] for course in courses) <= room_capacity
# #             )

# #     faculty_schedule = {}
# #     for course in courses:
# #         for slot in time_slots:
# #             faculty_schedule[(course, slot)] = model.NewBoolVar(f'{course}_faculty_{slot}')
# #             model.Add(
# #                 faculty_schedule[(course, slot)] == sum(exam_schedule[(course, slot, room)] for room in rooms)
# #             )

# #     for slot in time_slots:
# #         for faculty, available_slots in faculty_availability.items():
# #             if slot not in available_slots:
# #                 model.Add(
# #                     sum(faculty_schedule[(course, slot)] for course in courses) == 0
# #                 )

# #     solver = cp_model.CpSolver()
# #     status = solver.Solve(model)

# #     if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
# #         print("CSP Exam Schedule:")
# #         for course in courses:
# #             for slot in time_slots:
# #                 for room in rooms:
# #                     if solver.Value(exam_schedule[(course, slot, room)]) == 1:
# #                         print(f"Course: {course}, Time Slot: {slot}, Room: {room}")
# #     else:
# #         print("No feasible schedule found.")

# # # 2. Genetic Algorithm
# # import random

# # def generate_schedule_genetic():
# #     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
# #     students = {
# #         'Student1': ['Math', 'Physics'],
# #         'Student2': ['Math', 'Chemistry'],
# #         'Student3': ['Biology', 'Chemistry'],
# #     }
# #     time_slots = [0, 1, 2, 3]
# #     rooms = ['Room1', 'Room2']

# #     def fitness(schedule):
# #         score = 0
# #         for student, student_courses in students.items():
# #             student_slots = [slot for course, slot in schedule.items() if course in student_courses]
# #             if len(set(student_slots)) == len(student_slots):
# #                 score += 1
# #         return score

# #     def generate_individual():
# #         return {course: random.choice(time_slots) for course in courses}

# #     def mutate(individual):
# #         course = random.choice(courses)
# #         individual[course] = random.choice(time_slots)

# #     population = [generate_individual() for _ in range(100)]

# #     for _ in range(100):
# #         population.sort(key=fitness, reverse=True)
# #         next_generation = population[:10]
# #         for _ in range(90):
# #             parent = random.choice(next_generation)
# #             child = parent.copy()
# #             mutate(child)
# #             next_generation.append(child)
# #         population = next_generation

# #     best_schedule = max(population, key=fitness)
# #     print("Genetic Algorithm Exam Schedule:")
# #     for course, slot in best_schedule.items():
# #         print(f"Course: {course}, Time Slot: {slot}")

# # # 3. Simulated Annealing
# # import math

# # def generate_schedule_simulated_annealing():
# #     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
# #     students = {
# #         'Student1': ['Math', 'Physics'],
# #         'Student2': ['Math', 'Chemistry'],
# #         'Student3': ['Biology', 'Chemistry'],
# #     }
# #     time_slots = [0, 1, 2, 3]

# #     def fitness(schedule):
# #         score = 0
# #         for student, student_courses in students.items():
# #             student_slots = [slot for course, slot in schedule.items() if course in student_courses]
# #             if len(set(student_slots)) == len(student_slots):
# #                 score += 1
# #         return score

# #     def generate_neighbor(schedule):
# #         neighbor = schedule.copy()
# #         course = random.choice(courses)
# #         neighbor[course] = random.choice(time_slots)
# #         return neighbor

# #     current_schedule = {course: random.choice(time_slots) for course in courses}
# #     current_fitness = fitness(current_schedule)
# #     temperature = 100

# #     while temperature > 1:
# #         neighbor = generate_neighbor(current_schedule)
# #         neighbor_fitness = fitness(neighbor)
# #         if neighbor_fitness > current_fitness or random.random() < math.exp((neighbor_fitness - current_fitness) / temperature):
# #             current_schedule = neighbor
# #             current_fitness = neighbor_fitness
# #         temperature *= 0.99

# #     print("Simulated Annealing Exam Schedule:")
# #     for course, slot in current_schedule.items():
# #         print(f"Course: {course}, Time Slot: {slot}")

# # # 4. Using OpenAI API
# # def generate_schedule_openai():
# #     import openai

# #     openai.api_key = ""
# #     prompt = (
# #         "You are tasked with generating an exam timetable. Ensure no student has overlapping exams and optimize room usage."
# #         "Here are the courses: Math, Physics, Chemistry, Biology."
# #         "Students: Student1(Math, Physics), Student2(Math, Chemistry), Student3(Biology, Chemistry)."
# #         "Time slots: 0, 1, 2, 3. Rooms: Room1, Room2."
# #         "Generate an optimized schedule."
# #     )

# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",
# #         messages=[
# #             {"role": "system", "content": "You are a helpful assistant for scheduling."},
# #             {"role": "user", "content": prompt}
# #         ]
# #     )

# #     print("OpenAI Generated Schedule:")
# #     print(response['choices'][0]['message']['content'].strip())


# # # Execute all methods
# # generate_schedule_csp()
# # generate_schedule_genetic()
# # generate_schedule_simulated_annealing()
# # generate_schedule_openai()



# # 1. Constraint Satisfaction Problem (CSP)
# from ortools.sat.python import cp_model

# def generate_schedule_csp():
#     model = cp_model.CpModel()

#     # Example input data
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     rooms = ['Room1', 'Room2']
#     room_capacity = 2

#     # Variables
#     exam_schedule = {}
#     for course in courses:
#         for date in dates:
#             for time in time_slots:
#                 for room in rooms:
#                     exam_schedule[(course, date, time, room)] = model.NewBoolVar(f'{course}_{date}_{time}_{room}')

#     # Constraints
#     for course in courses:
#         model.Add(
#             sum(
#                 exam_schedule[(course, date, time, room)] 
#                 for date in dates 
#                 for time in time_slots 
#                 for room in rooms
#             ) == 1
#         )

#     for student, student_courses in students.items():
#         for date in dates:
#             for time in time_slots:
#                 model.Add(
#                     sum(
#                         exam_schedule[(course, date, time, room)] 
#                         for course in student_courses 
#                         for room in rooms
#                     ) <= 1
#                 )

#     for date in dates:
#         for time in time_slots:
#             for room in rooms:
#                 model.Add(
#                     sum(
#                         exam_schedule[(course, date, time, room)] 
#                         for course in courses
#                     ) <= room_capacity
#                 )

#     faculty_schedule = {}
#     for course in courses:
#         for date in dates:
#             for time in time_slots:
#                 faculty_schedule[(course, date, time)] = model.NewBoolVar(f'{course}_faculty_{date}_{time}')
#                 model.Add(
#                     faculty_schedule[(course, date, time)] == 
#                     sum(exam_schedule[(course, date, time, room)] for room in rooms)
#                 )

#     for date in dates:
#         for time in time_slots:
#             for faculty, available_times in faculty_availability.items():
#                 if time not in available_times:
#                     model.Add(
#                         sum(
#                             faculty_schedule[(course, date, time)] 
#                             for course in courses
#                         ) == 0
#                     )

#     solver = cp_model.CpSolver()
#     status = solver.Solve(model)

#     if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
#         print("CSP Exam Schedule:")
#         print("+------------+------------+--------+-------+-------------------+----------------+")
#         print("|   Course   |    Date    |  Time  | Room  |      Students     |   Faculty      |")
#         print("+------------+------------+--------+-------+-------------------+----------------+")
#         for course in courses:
#             for date in dates:
#                 for time in time_slots:
#                     for room in rooms:
#                         if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
#                             students_in_course = [s for s, sc in students.items() if course in sc]
#                             faculty = [f for f, at in faculty_availability.items() if time in at][0]
#                             print(f"| {course:10} | {date:10} | {time:6} | {room:5} | {', '.join(students_in_course):17} | {faculty:14} |")
#         print("+------------+------------+--------+-------+-------------------+----------------+")
#     else:
#         print("No feasible schedule found.")

# # 2. Genetic Algorithm
# import random

# def generate_schedule_genetic():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }

#     def fitness(schedule):
#         score = 0
#         for student, student_courses in students.items():
#             student_slots = [
#                 (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
#             ]
#             if len(set(student_slots)) == len(student_slots):
#                 score += 1
#         return score

#     def generate_individual():
#         return {
#             course: (
#                 random.choice(dates), 
#                 random.choice(time_slots), 
#                 random.choice(rooms)
#             ) for course in courses
#         }

#     def mutate(individual):
#         course = random.choice(courses)
#         individual[course] = (
#             random.choice(dates), 
#             random.choice(time_slots), 
#             random.choice(rooms)
#         )

#     population = [generate_individual() for _ in range(100)]

#     for _ in range(100):
#         population.sort(key=fitness, reverse=True)
#         next_generation = population[:10]
#         for _ in range(90):
#             parent = random.choice(next_generation)
#             child = parent.copy()
#             mutate(child)
#             next_generation.append(child)
#         population = next_generation

#     best_schedule = max(population, key=fitness)
#     print("Genetic Algorithm Exam Schedule:")
#     print("+------------+------------+--------+-------+-------------------+----------------+")
#     print("|   Course   |    Date    |  Time  | Room  |      Students     |   Faculty      |")
#     print("+------------+------------+--------+-------+-------------------+----------------+")
#     for course, (date, time, room) in best_schedule.items():
#         students_in_course = [s for s, sc in students.items() if course in sc]
#         faculty = [f for f, at in faculty_availability.items() if time in at][0]
#         print(f"| {course:10} | {date:10} | {time:6} | {room:5} | {', '.join(students_in_course):17} | {faculty:14} |")
#     print("+------------+------------+--------+-------+-------------------+----------------+")

# # 3. Simulated Annealing
# import math

# def generate_schedule_simulated_annealing():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }

#     def fitness(schedule):
#         score = 0
#         for student, student_courses in students.items():
#             student_slots = [
#                 (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
#             ]
#             if len(set(student_slots)) == len(student_slots):
#                 score += 1
#         return score

#     def generate_neighbor(schedule):
#         neighbor = schedule.copy()
#         course = random.choice(courses)
#         neighbor[course] = (
#             random.choice(dates), 
#             random.choice(time_slots), 
#             random.choice(rooms)
#         )
#         return neighbor

#     current_schedule = {
#         course: (
#             random.choice(dates), 
#             random.choice(time_slots), 
#             random.choice(rooms)
#         ) for course in courses
#     }
#     current_fitness = fitness(current_schedule)
#     temperature = 100

#     while temperature > 1:
#         neighbor = generate_neighbor(current_schedule)
#         neighbor_fitness = fitness(neighbor)
#         if neighbor_fitness > current_fitness or random.random() < math.exp((neighbor_fitness - current_fitness) / temperature):
#             current_schedule = neighbor
#             current_fitness = neighbor_fitness
#         temperature *= 0.99

#     print("Simulated Annealing Exam Schedule:")
#     print("+------------+------------+--------+-------+-------------------+----------------+")
#     print("|   Course   |    Date    |  Time  | Room  |      Students     |   Faculty      |")
#     print("+------------+------------+--------+-------+-------------------+----------------+")
#     for course, (date, time, room) in current_schedule.items():
#         students_in_course = [s for s, sc in students.items() if course in sc]
#         faculty = [f for f, at in faculty_availability.items() if time in at][0]
#         print(f"| {course:10} | {date:10} | {time:6} | {room:5} | {', '.join(students_in_course):17} | {faculty:14} |")
#     print("+------------+------------+--------+-------+-------------------+----------------+")

# # 4. Using OpenAI API
# def generate_schedule_openai():
#     import openai

#     openai.api_key = ""
#     prompt = (
#         "Generate a detailed exam timetable based on the following requirements:\n"
#         "- No student has overlapping exams.\n"
#         "- Each exam is assigned a specific date, time, and room.\n"
#         "- Assign faculty members to invigilate each exam.\n"
#         "- Include details like course, date, time, room, students, and faculty in charge.\n"
#         "Input data:\n"
#         "Courses: Math, Physics, Chemistry, Biology.\n"
#         "Students: Student1 (Math, Physics), Student2 (Math, Chemistry), Student3 (Biology, Chemistry).\n"
#         "Faculty: Faculty1, Faculty2.\n"
#         "Available time slots: 9 AM, 12 PM, 3 PM.\n"
#         "Rooms: Room1 (capacity: 2), Room2 (capacity: 2).\n"
#         "Faculty availability: Faculty1 (9 AM, 12 PM), Faculty2 (12 PM, 3 PM).\n"
#         "Output a table with the following columns: Course, Date, Time, Room, Students, Faculty."
#     )

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a scheduling assistant."},
#             {"role": "user", "content": prompt},
#         ]
#     )

#     print("OpenAI Generated Schedule:")
#     print(response['choices'][0]['message']['content'].strip())

# # Execute all methods
# generate_schedule_csp()
# generate_schedule_genetic()
# generate_schedule_simulated_annealing()
# generate_schedule_openai()


# import random
# import math
# from ortools.sat.python import cp_model
# import openai

# # Example input data (same for all methods)
# courses = [f"Course{i}" for i in range(1, 21)]  # 2000 courses
# students = {f"Student{i}": [f"Course{j}" for j in range(1, 4)] for i in range(1, 11)}  # 1000 students, 10 courses each
# time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
# dates = ['2024-12-15', '2024-12-16']
# rooms = [f'Room{i}' for i in range(1, 31)]  # 300 rooms

# # Fitness function (same for Genetic Algorithm and Simulated Annealing)
# def fitness(schedule):
#     score = 0
#     # Example: penalize if a student has overlapping exams
#     for student, student_courses in students.items():
#         student_schedule = []
#         for course in student_courses:
#             course_schedule = schedule.get(course)
#             if course_schedule:
#                 if course_schedule in student_schedule:
#                     score -= 10  # Penalize overlap
#                 else:
#                     student_schedule.append(course_schedule)
#         score += len(student_schedule)  # Reward for unique course allocations
#     return score


# # 1. **CSP (Constraint Satisfaction Problem) Approach**
# # def generate_schedule_csp():
# #     model = cp_model.CpModel()

# #     # Variables for scheduling
# #     exam_schedule = {}
# #     for course in courses:
# #         for date in dates:
# #             for time in time_slots:
# #                 for room in rooms:
# #                     exam_schedule[(course, date, time, room)] = model.NewBoolVar(f'{course}_{date}_{time}_{room}')

# #     # Constraints (same as above)
# #     for course in courses:
# #         model.AddSumConstraint([exam_schedule[(course, date, time, room)] for date in dates for time in time_slots for room in rooms], 1)

# #     for student, student_courses in students.items():
# #         for course in student_courses:
# #             for date in dates:
# #                 for time in time_slots:
# #                     for room in rooms:
# #                         model.AddAtMostOne([exam_schedule[(course, date, time, room)] for course in student_courses])

# #     # Solve the model
# #     solver = cp_model.CpSolver()
# #     status = solver.Solve(model)

# #     if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
# #         print("CSP Schedule Generated:")
# #         for course in courses:
# #             for date in dates:
# #                 for time in time_slots:
# #                     for room in rooms:
# #                         if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
# #                             print(f"{course}: {date}, {time}, {room}")
# #     else:
# #         print("No feasible schedule found.")
# # def generate_schedule_csp():
# #     model = cp_model.CpModel()

# #     # Variables for scheduling
# #     exam_schedule = {}
# #     for course in courses:
# #         for date in dates:
# #             for time in time_slots:
# #                 for room in rooms:
# #                     exam_schedule[(course, date, time, room)] = model.NewBoolVar(f'{course}_{date}_{time}_{room}')

# #     # Constraints: Each course must be assigned to exactly one time slot and room
# #     for course in courses:
# #         model.AddLinearConstraint(
# #             sum(exam_schedule[(course, date, time, room)] for date in dates for time in time_slots for room in rooms) == 1
# #         )

# #     # Constraints: Each student can have only one exam at a time (simplified for this example)
# #     for student, student_courses in students.items():
# #         for course in student_courses:
# #             model.AddLinearConstraint(
# #                 sum(exam_schedule[(course, date, time, room)] for date in dates for time in time_slots for room in rooms) <= 1
# #             )

# #     # Solve the model
# #     solver = cp_model.CpSolver()
# #     status = solver.Solve(model)

# #     if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
# #         print("CSP Schedule Generated:")
# #         for course in courses:
# #             for date in dates:
# #                 for time in time_slots:
# #                     for room in rooms:
# #                         if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
# #                             print(f"{course}: {date}, {time}, {room}")
# #     else:
# #         print("No feasible schedule found.")
# def generate_schedule_csp():
#     model = cp_model.CpModel()

#     # Variables for scheduling
#     exam_schedule = {}
#     for course in courses:
#         for date in dates:
#             for time in time_slots:
#                 for room in rooms:
#                     exam_schedule[(course, date, time, room)] = model.NewBoolVar(f'{course}_{date}_{time}_{room}')

#     # Constraints: Each course must be assigned to exactly one time slot and room
#     for course in courses:
#         model.AddLinearConstraint(
#             sum(exam_schedule[(course, date, time, room)] for date in dates for time in time_slots for room in rooms), 
#             1, 1  # lb=1 (lower bound) and ub=1 (upper bound)
#         )

#     # Constraints: Each student can have only one exam at a time (simplified for this example)
#     for student, student_courses in students.items():
#         for course in student_courses:
#             model.AddLinearConstraint(
#                 sum(exam_schedule[(course, date, time, room)] for date in dates for time in time_slots for room in rooms), 
#                 0, 1  # lb=0 and ub=1 to ensure the student can have at most 1 exam at the same time
#             )

#     # Solve the model
#     solver = cp_model.CpSolver()
#     status = solver.Solve(model)

#     if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
#         print("CSP Schedule Generated:")
#         for course in courses:
#             for date in dates:
#                 for time in time_slots:
#                     for room in rooms:
#                         if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
#                             print(f"{course}: {date}, {time}, {room}")
#     else:
#         print("No feasible schedule found.")



# # 2. **Genetic Algorithm Approach**
# def generate_schedule_genetic():
#     # Generate random schedule
#     def generate_random_schedule():
#         schedule = {}
#         for course in courses:
#             date = random.choice(dates)
#             time = random.choice(time_slots)
#             room = random.choice(rooms)
#             schedule[course] = (date, time, room)
#         return schedule

#     # Selection function
#     def select_parents(population):
#         selected = random.sample(population, 2)
#         return selected

#     # Crossover function
#     def crossover(parent1, parent2):
#         child = {}
#         for course in courses:
#             if random.random() < 0.5:
#                 child[course] = parent1[course]
#             else:
#                 child[course] = parent2[course]
#         return child

#     # Mutation function
#     def mutate(schedule):
#         course = random.choice(courses)
#         schedule[course] = (random.choice(dates), random.choice(time_slots), random.choice(rooms))
#         return schedule

#     # Genetic Algorithm to evolve the schedule
#     def genetic_algorithm():
#         population_size = 100
#         generations = 1000
#         mutation_rate = 0.1
#         population = [generate_random_schedule() for _ in range(population_size)]

#         for generation in range(generations):
#             population = sorted(population, key=fitness, reverse=True)
#             if fitness(population[0]) == len(courses):  # Perfect score
#                 break

#             next_generation = population[:10]  # Elitism: keep top 10 schedules

#             while len(next_generation) < population_size:
#                 parent1, parent2 = select_parents(population)
#                 child = crossover(parent1, parent2)
#                 if random.random() < mutation_rate:
#                     child = mutate(child)
#                 next_generation.append(child)

#             population = next_generation

#         best_schedule = population[0]
#         print("Genetic Algorithm Schedule Generated:")
#         for course, (date, time, room) in best_schedule.items():
#             print(f"{course}: {date}, {time}, {room}")

#     genetic_algorithm()


# # 3. **Simulated Annealing Approach**
# def generate_schedule_simulated_annealing():
#     # Generate a random schedule
#     def generate_random_schedule():
#         schedule = {}
#         for course in courses:
#             date = random.choice(dates)
#             time = random.choice(time_slots)
#             room = random.choice(rooms)
#             schedule[course] = (date, time, room)
#         return schedule

#     # Simulated Annealing algorithm
#     def simulated_annealing():
#         current_schedule = generate_random_schedule()
#         current_fitness = fitness(current_schedule)

#         temperature = 1000  # Starting temperature
#         cooling_rate = 0.95
#         stop_temperature = 0.1

#         while temperature > stop_temperature:
#             new_schedule = generate_random_schedule()  # Generate a neighboring solution
#             new_fitness = fitness(new_schedule)

#             if new_fitness > current_fitness or random.random() < math.exp((new_fitness - current_fitness) / temperature):
#                 current_schedule = new_schedule
#                 current_fitness = new_fitness

#             temperature *= cooling_rate  # Cool down the system

#         print("Simulated Annealing Schedule Generated:")
#         for course, (date, time, room) in current_schedule.items():
#             print(f"{course}: {date}, {time}, {room}")

#     simulated_annealing()


# 4. **Using OpenAI API (Prompt Approach)**
# def generate_schedule_openai():
#     openai.api_key = ''

#     prompt = """
#     You are an AI scheduling assistant. Your task is to generate a schedule for a university's exam system. There are:
#     - 2000 courses
#     - 1000 students, each enrolled in 10 courses
#     - 400 faculty members
#     - 300 rooms with a capacity of 2 students each
#     - Four time slots: '9 AM', '12 PM', '3 PM', '6 PM'
#     - Two dates: '2024-12-15' and '2024-12-16'
    
#     You need to create a schedule with the following:
#     1. A table with courses, their assigned date, time, room, and faculty member.
#     2. A table with students, their assigned room, date, and time.
    
#     Consider constraints such as:
#     - A student can only attend one exam at a time.
#     - Faculty members are only available during specific time slots.
#     - Rooms have limited capacity.
    
#     Provide the output in the following format:
#     Table 1: Course Schedule
#     +------------+------------+--------+-------+-------------------+-------------------+
#     | Course     | Date       | Time   | Room  | Students          | Faculty           |
#     +------------+------------+--------+-------+-------------------+-------------------+
#     | Course1    | 2024-12-15 | 9 AM   | Room1 | Student1, Student2| Faculty1          |
    
#     Table 2: Student Schedule
#     +------------+--------+------------+--------+
#     | Student    | Room   | Date       | Time   |
#     +------------+--------+------------+--------+
#     | Student1   | Room1  | 2024-12-15 | 9 AM   |
#     """

#     response = openai.Completion.create(
#         engine="gpt-4",
#         prompt=prompt,
#         max_tokens=1000
#     )

#     print("OpenAI API Schedule Generated:")
#     print(response.choices[0].text.strip())

# def generate_schedule_openai():
#     openai.api_key = ''  # Replace with your OpenAI API key

#     # Define a prompt for the model to generate a schedule
#     prompt = """
#     You are tasked with generating an exam schedule for the following courses:
#     - Course 1: Math 101
#     - Course 2: History 201
#     - Course 3: Computer Science 301
#     - Course 4: Physics 401

#     The available dates are: [2024-12-20, 2024-12-21, 2024-12-22]
#     The available time slots are: [9:00 AM, 1:00 PM]
#     The available rooms are: [Room A, Room B]

#     The constraint is that no student can have more than one exam on the same day.

#     Provide the schedule in the format:
#     Course: [Course Name]
#     Date: [Date]
#     Time: [Time]
#     Room: [Room]
#     """

#     # Use the chat-based API (v1/chat/completions)
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # Or "gpt-4" if you prefer
#         messages=[{"role": "system", "content": "You are a helpful assistant."},
#                   {"role": "user", "content": prompt}],
#         temperature=0.7,  # Adjust for creativity
#         max_tokens=500,   # Adjust token limit as needed
#     )

#     # Parse and display the response
#     schedule = response['choices'][0]['message']['content']
#     print("OpenAI Generated Schedule:")
#     print(schedule)


# # Execute all methods
# def execute_all_methods():
#     generate_schedule_csp()
#     generate_schedule_genetic()
#     generate_schedule_simulated_annealing()
#     generate_schedule_openai()

# # Run the execution
# execute_all_methods()



# def generate_schedule_openai_api():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     room_capacity = 2

#     # Build prompt for the API
# #     prompt = f"""
# # You are an AI tasked with scheduling exams. The constraints are as follows:
# # 1. There are the following courses: {', '.join(courses)}.
# # 2. Students are enrolled in specific courses: {students}.
# # 3. Time slots for exams are: {', '.join(time_slots)}.
# # 4. Exam dates are: {', '.join(dates)}.
# # 5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
# # 6. Faculty availability is as follows: {faculty_availability}.
# # 7. No student can have overlapping exams, and room capacity cannot be exceeded.

# # Generate an exam schedule with the following format:
# # Table 1: course, date, time, faculty
# # Table 2: student, room, time, date

# # Return the schedule in structured JSON format.
# #     """

#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date

#     Return the schedule in structured JSON format.
#     """


#     # Call OpenAI API
#     try:
#         response = openai.Completion.create(
#             engine="gpt-4",  # Use a GPT-3.5 or GPT-4 capable engine
#             prompt=prompt,
#             max_tokens=500,
#             temperature=0.7
#         )
#         output = response['choices'][0]['text'].strip()

#         # Parse the JSON output (assume the AI returns structured JSON)
#         schedule = eval(output)  # Use ast.literal_eval for safer parsing in production
        
#         # Extract and print tables
#         table_1 = schedule['Table 1']
#         table_2 = schedule['Table 2']

#         # Print Table 1
#         print("OpenAI API Exam Schedule - Table 1:")
#         print("+------------+------------+--------+----------------+")
#         print("|   Course   |    Date    |  Time  |     Faculty    |")
#         print("+------------+------------+--------+----------------+")
#         for row in table_1:
#             print(f"| {row['course']:10} | {row['date']:10} | {row['time']:6} | {row['faculty']:14} |")
#         print("+------------+------------+--------+----------------+")

#         # Print Table 2
#         print("OpenAI API Exam Schedule - Table 2:")
#         print("+------------+-------+--------+------------+")
#         print("|   Student  | Room  |  Time  |    Date    |")
#         print("+------------+-------+--------+------------+")
#         for row in table_2:
#             print(f"| {row['student']:10} | {row['room']:5} | {row['time']:6} | {row['date']:10} |")
#         print("+------------+-------+--------+------------+")

#     except Exception as e:
#         print(f"An error occurred while using the OpenAI API: {e}")


# def generate_schedule_openai_api():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     room_capacity = 2

#     # Build prompt for the API
#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date

#     Return the schedule in structured JSON format.
#     """

#     # Call OpenAI API
#     try:
#         response = openai.Completion.create(
#             engine="gpt-4",  # Use GPT-4 engine instead of deprecated Davinci
#             prompt=prompt,
#             max_tokens=500,
#             temperature=0.7
#         )
#         output = response['choices'][0]['text'].strip()

#         # Parse the JSON output (assume the AI returns structured JSON)
#         schedule = eval(output)  # Use ast.literal_eval for safer parsing in production
        
#         # Extract and print tables
#         table_1 = schedule['Table 1']
#         table_2 = schedule['Table 2']

#         # Print Table 1
#         print("OpenAI API Exam Schedule - Table 1:")
#         print("+------------+------------+--------+----------------+")
#         print("|   Course   |    Date    |  Time  |     Faculty    |")
#         print("+------------+------------+--------+----------------+")
#         for row in table_1:
#             print(f"| {row['course']:10} | {row['date']:10} | {row['time']:6} | {row['faculty']:14} |")
#         print("+------------+------------+--------+----------------+")

#         # Print Table 2
#         print("OpenAI API Exam Schedule - Table 2:")
#         print("+------------+-------+--------+------------+")
#         print("|   Student  | Room  |  Time  |    Date    |")
#         print("+------------+-------+--------+------------+")
#         for row in table_2:
#             print(f"| {row['student']:10} | {row['room']:5} | {row['time']:6} | {row['date']:10} |")
#         print("+------------+-------+--------+------------+")

#     except Exception as e:
#         print(f"An error occurred while using the OpenAI API: {e}")


# def generate_schedule_openai_api():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     room_capacity = 2

#     # Build prompt for the API
#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date

#     Return the schedule in structured JSON format.
#     """

#     # Call OpenAI API using chat model and the correct endpoint
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # Use GPT-4 model
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             # max_tokens=500,
#             temperature=0.7
#         )
#         output = response['choices'][0]['message']['content'].strip()

#         # Parse the JSON output (assume the AI returns structured JSON)
#         schedule = eval(output)  # Use ast.literal_eval for safer parsing in production
        
#         # Extract and print tables
#         table_1 = schedule['Table 1']
#         table_2 = schedule['Table 2']

#         # Print Table 1
#         print("OpenAI API Exam Schedule - Table 1:")
#         print("+------------+------------+--------+----------------+")
#         print("|   Course   |    Date    |  Time  |     Faculty    |")
#         print("+------------+------------+--------+----------------+")
#         for row in table_1:
#             print(f"| {row['course']:10} | {row['date']:10} | {row['time']:6} | {row['faculty']:14} |")
#         print("+------------+------------+--------+----------------+")

#         # Print Table 2
#         print("OpenAI API Exam Schedule - Table 2:")
#         print("+------------+-------+--------+------------+")
#         print("|   Student  | Room  |  Time  |    Date    |")
#         print("+------------+-------+--------+------------+")
#         for row in table_2:
#             print(f"| {row['student']:10} | {row['room']:5} | {row['time']:6} | {row['date']:10} |")
#         print("+------------+-------+--------+------------+")

#     except Exception as e:
#         print(f"An error occurred while using the OpenAI API: {e}")


# def generate_schedule_openai_api():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     room_capacity = 2

#     # Build prompt for the API
#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date

#     Return the schedule in structured JSON format.
#     """

#     # Call OpenAI API using chat model and the correct endpoint
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # Use GPT-4 model
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,
#             temperature=0.7
#         )
#         output = response['choices'][0]['message']['content'].strip()

#         # Parse the JSON output (assume the AI returns structured JSON)
#         schedule = eval(output)  # Use ast.literal_eval for safer parsing in production
        
#         # Extract and print tables
#         table_1 = schedule['Table 1']
#         table_2 = schedule['Table 2']

#         # Print Table 1
#         print("OpenAI API Exam Schedule - Table 1:")
#         print("+------------+------------+--------+----------------+")
#         print("|   Course   |    Date    |  Time  |     Faculty    |")
#         print("+------------+------------+--------+----------------+")
#         for row in table_1:
#             print(f"| {row['course']:10} | {row['date']:10} | {row['time']:6} | {row['faculty']:14} |")
#         print("+------------+------------+--------+----------------+")

#         # Print Table 2
#         print("OpenAI API Exam Schedule - Table 2:")
#         print("+------------+-------+--------+------------+")
#         print("|   Student  | Room  |  Time  |    Date    |")
#         print("+------------+-------+--------+------------+")
#         for row in table_2:
#             print(f"| {row['student']:10} | {row['room']:5} | {row['time']:6} | {row['date']:10} |")
#         print("+------------+-------+--------+------------+")

#     except Exception as e:
#         print(f"An error occurred while using the OpenAI API: {e}")


# def generate_schedule_openai_api():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     room_capacity = 2

#     # Build prompt for the API
#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date

#     Return the schedule in structured JSON format.
#     """

#     # Debugging step: Print the prompt to check for any formatting issues
#     print("Generated prompt for OpenAI API:")
#     print(repr(prompt))  # Print the prompt as raw text to ensure it's correctly formatted

#     # Call OpenAI API using chat model and the correct endpoint
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # Use GPT-4 model
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,
#             temperature=0.7
#         )
        
#         # Extract the AI response
#         output = response['choices'][0]['message']['content'].strip()

#         # Debugging step: Print the AI's response to ensure it's valid JSON
#         print("Raw response from OpenAI API:")
#         print(repr(output))  # Print the response to see if it's valid JSON

#         # Parse the JSON output (assume the AI returns structured JSON)
#         schedule = eval(output)  # Use ast.literal_eval for safer parsing in production
        
#         # Extract and print tables
#         table_1 = schedule['Table 1']
#         table_2 = schedule['Table 2']

#         # Print Table 1
#         print("OpenAI API Exam Schedule - Table 1:")
#         print("+------------+------------+--------+----------------+")
#         print("|   Course   |    Date    |  Time  |     Faculty    |")
#         print("+------------+------------+--------+----------------+")
#         for row in table_1:
#             print(f"| {row['course']:10} | {row['date']:10} | {row['time']:6} | {row['faculty']:14} |")
#         print("+------------+------------+--------+----------------+")

#         # Print Table 2
#         print("OpenAI API Exam Schedule - Table 2:")
#         print("+------------+-------+--------+------------+")
#         print("|   Student  | Room  |  Time  |    Date    |")
#         print("+------------+-------+--------+------------+")
#         for row in table_2:
#             print(f"| {row['student']:10} | {row['room']:5} | {row['time']:6} | {row['date']:10} |")
#         print("+------------+-------+--------+------------+")

#     except Exception as e:
#         print(f"An error occurred while using the OpenAI API: {e}")


# import openai
# import json

# def generate_schedule_openai_api():
#     courses = ['Math', 'Physics', 'Chemistry', 'Biology']
#     students = {
#         'Student1': ['Math', 'Physics'],
#         'Student2': ['Math', 'Chemistry'],
#         'Student3': ['Biology', 'Chemistry'],
#     }
#     time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
#     dates = ['2024-12-15', '2024-12-16']
#     rooms = ['Room1', 'Room2']
#     faculty_availability = {
#         'Faculty1': ['9 AM', '12 PM'],
#         'Faculty2': ['3 PM', '6 PM'],
#     }
#     room_capacity = 2

#     # Build prompt for the API
#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date

#     Return the schedule in structured JSON format.
#     """

#     # Call OpenAI API using chat model and the correct endpoint
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # Use GPT-4 model
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,
#             temperature=0.7
#         )
        
#         # Extract the AI's response (skip the introductory message)
#         raw_output = response['choices'][0]['message']['content'].strip()
        
#         # Look for the JSON part in the response and extract it
#         start_index = raw_output.find("{")
#         end_index = raw_output.rfind("}") + 1
#         json_output = raw_output[start_index:end_index]

#         # Debugging: Print the extracted JSON
#         print("Extracted JSON response:")
#         print(json_output)

#         # Parse the extracted JSON output
#         schedule = json.loads(json_output)  # Safely parse the JSON string

#         # Extract and print tables
#         exams = schedule['exams']
#         students_schedule = schedule['students']

#         # Print the exams table
#         print("OpenAI API Exam Schedule - Table 1:")
#         print("+------------+------------+--------+----------------+")
#         print("|   Course   |    Date    |  Time  |     Faculty    |")
#         print("+------------+------------+--------+----------------+")
#         for exam in exams:
#             print(f"| {exam['course']:10} | {exam['date']:10} | {exam['time']:6} | {exam['faculty']:14} |")
#         print("+------------+------------+--------+----------------+")

#         # Print the students table
#         print("OpenAI API Exam Schedule - Table 2:")
#         print("+------------+-------+--------+------------+")
#         print("|   Student  | Room  |  Time  |    Date    |")
#         print("+------------+-------+--------+------------+")
#         for student in students_schedule:
#             for course in student['courses']:
#                 print(f"| {student['student']:10} | {course['room']:5} | {course['time']:6} | {course['date']:10} |")
#         print("+------------+-------+--------+------------+")

#     except Exception as e:
#         print(f"An error occurred while using the OpenAI API: {e}")



    # def energy(schedule):
    #     penalty = 0
    #     # Check for student schedule conflicts
    #     for student, student_courses in students.items():
    #         student_slots = [
    #             (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
    #         ]
    #         if len(set(student_slots)) != len(student_slots):  # Overlapping exams
    #             penalty += 1
        
    #     # Check for room capacity conflicts
    #     for date in dates:
    #         for time in time_slots:
    #             for room in rooms:
    #                 courses_in_room = [
    #                     course for course, (c_date, c_time, c_room) in schedule.items()
    #                     if c_date == date and c_time == time and c_room == room
    #                 ]
    #                 if len(courses_in_room) > room_capacity:
    #                     penalty += len(courses_in_room) - room_capacity
        
    #     return penalty



    # def fitness(schedule):
    #     score = 0
    #     for student, student_courses in students.items():
    #         student_slots = [
    #             (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
    #         ]
    #         if len(set(student_slots)) == len(student_slots):
    #             score += 1
    #     return score





# import json
# import random
# import math

# # Shared Data (Assumed to be provided)
# courses = ['Math', 'Physics', 'Chemistry', 'Biology']
# students = {
#     'Student1': ['Math', 'Physics'],
#     'Student2': ['Math', 'Chemistry'],
#     'Student3': ['Biology', 'Chemistry'],
# }
# time_slots = ['9 AM', '12 PM', '3 PM', '6 PM']
# dates = ['2024-12-15', '2024-12-16']
# faculty_availability = {
#     'Faculty1': ['9 AM', '12 PM'],
#     'Faculty2': ['3 PM', '6 PM'],
# }
# rooms = ['Room1', 'Room2']
# room_capacity = 2


# # Google OR-Tools CSP Approach (Modified to JSON output)
# from ortools.sat.python import cp_model

# def generate_schedule_csp():
#     model = cp_model.CpModel()
#     exam_schedule = {}
#     faculty_schedule = {}

#     # Variables
#     for course in courses:
#         for date in dates:
#             for time in time_slots:
#                 for room in rooms:
#                     exam_schedule[(course, date, time, room)] = model.NewBoolVar(f'{course}_{date}_{time}_{room}')

#     for course in courses:
#         for date in dates:
#             for time in time_slots:
#                 faculty_schedule[(course, date, time)] = model.NewBoolVar(f'{course}_faculty_{date}_{time}')

#     # Constraints (as before)

#     # Solve
#     solver = cp_model.CpSolver()
#     status = solver.Solve(model)

#     schedule_data = {
#         "exams": [],
#         "students": []
#     }

#     if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
#         for course in courses:
#             for date in dates:
#                 for time in time_slots:
#                     for room in rooms:
#                         if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
#                             faculty = [
#                                 f for f, times in faculty_availability.items() if time in times
#                             ][0]
#                             students_in_course = [s for s, sc in students.items() if course in sc]
#                             schedule_data["exams"].append({
#                                 "course": course,
#                                 "date": date,
#                                 "time": time,
#                                 "faculty": faculty
#                             })
#                             for student in students_in_course:
#                                 schedule_data["students"].append({
#                                     "student": student,
#                                     "room": room,
#                                     "time": time,
#                                     "date": date
#                                 })
#     return json.dumps(schedule_data, indent=4)


# # Genetic Algorithm Approach (Modified to JSON output)
# def generate_schedule_genetic():
#     def fitness(schedule):
#         score = 0
#         faculty_schedule = {}
#         for course, (date, time, room) in schedule.items():
#             faculty = [f for f, at in faculty_availability.items() if time in at][0]
#             if (faculty, date, time) not in faculty_schedule:
#                 faculty_schedule[(faculty, date, time)] = course
#             else:
#                 score -= 1
        
#         for student, student_courses in students.items():
#             student_slots = [
#                 (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
#             ]
#             if len(set(student_slots)) == len(student_slots):
#                 score += 1
#         return score

#     def generate_individual():
#         return {
#             course: (
#                 random.choice(dates), 
#                 random.choice(time_slots), 
#                 random.choice(rooms)
#             ) for course in courses
#         }

#     def mutate(individual):
#         course = random.choice(courses)
#         individual[course] = (
#             random.choice(dates), 
#             random.choice(time_slots), 
#             random.choice(rooms)
#         )

#     population = [generate_individual() for _ in range(100)]

#     for _ in range(100):
#         population.sort(key=fitness, reverse=True)
#         next_generation = population[:10]
#         for _ in range(90):
#             parent = random.choice(next_generation)
#             child = parent.copy()
#             mutate(child)
#             next_generation.append(child)
#         population = next_generation

#     best_schedule = max(population, key=fitness)

#     schedule_data = {
#         "exams": [],
#         "students": []
#     }

#     for course, (date, time, room) in best_schedule.items():
#         students_in_course = [s for s, sc in students.items() if course in sc]
#         faculty = [f for f, at in faculty_availability.items() if time in at][0]
#         schedule_data["exams"].append({
#             "course": course,
#             "date": date,
#             "time": time,
#             "faculty": faculty
#         })
#         for student in students_in_course:
#             schedule_data["students"].append({
#                 "student": student,
#                 "room": room,
#                 "time": time,
#                 "date": date
#             })

#     return json.dumps(schedule_data, indent=4)


# # Simulated Annealing Approach (Modified to JSON output)
# def generate_schedule_simulated_annealing():
#     def energy(schedule):
#         penalty = 0
#         faculty_schedule = {}
#         for course, (date, time, room) in schedule.items():
#             faculty = [f for f, at in faculty_availability.items() if time in at][0]
#             if (faculty, date, time) not in faculty_schedule:
#                 faculty_schedule[(faculty, date, time)] = course
#             else:
#                 penalty += 1
        
#         for student, student_courses in students.items():
#             student_slots = [
#                 (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
#             ]
#             if len(set(student_slots)) != len(student_slots):
#                 penalty += 1
            
#         return penalty

#     def random_schedule():
#         return {
#             course: (
#                 random.choice(dates), 
#                 random.choice(time_slots), 
#                 random.choice(rooms)
#             ) for course in courses
#         }

#     def neighbor(schedule):
#         course = random.choice(courses)
#         new_schedule = schedule.copy()
#         new_schedule[course] = (
#             random.choice(dates), 
#             random.choice(time_slots), 
#             random.choice(rooms)
#         )
#         return new_schedule

#     def acceptance_probability(old_energy, new_energy, temperature):
#         if new_energy < old_energy:
#             return 1.0
#         return math.exp((old_energy - new_energy) / temperature)

#     current_schedule = random_schedule()
#     current_energy = energy(current_schedule)
#     temperature = 100.0
#     cooling_rate = 0.95

#     while temperature > 1:
#         new_schedule = neighbor(current_schedule)
#         new_energy = energy(new_schedule)

#         if acceptance_probability(current_energy, new_energy, temperature) > random.random():
#             current_schedule = new_schedule
#             current_energy = new_energy

#         temperature *= cooling_rate

#     schedule_data = {
#         "exams": [],
#         "students": []
#     }

#     for course, (date, time, room) in current_schedule.items():
#         students_in_course = [s for s, sc in students.items() if course in sc]
#         faculty = [f for f, at in faculty_availability.items() if time in at][0]
#         schedule_data["exams"].append({
#             "course": course,
#             "date": date,
#             "time": time,
#             "faculty": faculty
#         })
#         for student in students_in_course:
#             schedule_data["students"].append({
#                 "student": student,
#                 "room": room,
#                 "time": time,
#                 "date": date
#             })

#     return json.dumps(schedule_data, indent=4)


# # OpenAI API Approach (Modified to return schedule in JSON)
# import openai

# openai.api_key = "sk-1234567890abcdef1234567890abcdef"

# def generate_schedule_openai_api():
#     prompt = f"""
#     You are an AI tasked with scheduling exams. The constraints are as follows:
#     1. There are the following courses: {', '.join(courses)}.
#     2. Students are enrolled in specific courses: {students}.
#     3. Time slots for exams are: {', '.join(time_slots)}.
#     4. Exam dates are: {', '.join(dates)}.
#     5. Rooms available: {', '.join(rooms)} with a maximum capacity of {room_capacity} students.
#     6. Faculty availability is as follows: {faculty_availability}.
#     7. No student can have overlapping exams, and room capacity cannot be exceeded.
#     8. No faculty member can be assigned to multiple exams at the same time.

#     Generate an exam schedule with the following format:
#     Table 1: course, date, time, faculty
#     Table 2: student, room, time, date
#     """

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,
#             temperature=0.7
#         )

#         raw_output = response['choices'][0]['message']['content'].strip()
#         start_index = raw_output.find("{")
#         end_index = raw_output.rfind("}") + 1
#         json_output = raw_output[start_index:end_index]

#         schedule = json.loads(json_output)

#         return json.dumps(schedule, indent=4)

#     except Exception as e:
#         return f"An error occurred while using the OpenAI API: {e}"


# # Test function calls
# print("CSP:\n", generate_schedule_csp())
# print("GA:\n",generate_schedule_genetic())
# print("SA:\n", generate_schedule_simulated_annealing())
# print("AI:\n", generate_schedule_openai_api())
