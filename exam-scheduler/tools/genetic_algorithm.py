import random
# from data.data_set import courses, test_dates, time_slots, rooms, room_capacity, students, faculty_availability
from data.database import courses, time_slots, rooms, room_capacity, students, faculty_availability

def generate_schedule_genetic(dates):

    # dates = test_dates

    def fitness(schedule):
        score = 0
        faculty_schedule = {}
        for course, (date, time, room) in schedule.items():
            faculty = [f for f, at in faculty_availability.items() if time in at][0]
            if (faculty, date, time) not in faculty_schedule:
                faculty_schedule[(faculty, date, time)] = course
            else:
                score -= 1
        
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
    
    result = {'exams': [], 'students': []}
    for course, (date, time, room) in best_schedule.items():
        students_in_course = [s for s, sc in students.items() if course in sc]
        faculty = [f for f, at in faculty_availability.items() if time in at][0]
        result['exams'].append({'course': course, 'date': date, 'time': time, 'faculty': faculty})
        for student in students_in_course:
            result['students'].append({'student': student, 'room': room, 'time': time, 'date': date})

    return result

