import random
import math
# from data.data_set import courses, test_dates, time_slots, rooms, room_capacity, students, faculty_availability
from data.database import courses, time_slots, rooms, room_capacity, students, faculty_availability

def generate_schedule_simulated_annealing(dates):

    # dates = test_dates

    def energy(schedule):
        penalty = 0
        faculty_schedule = {}
        for course, (date, time, room) in schedule.items():
            faculty = [f for f, at in faculty_availability.items() if time in at][0]
            if (faculty, date, time) not in faculty_schedule:
                faculty_schedule[(faculty, date, time)] = course
            else:
                penalty += 1
            
        for student, student_courses in students.items():
            student_slots = [
                (date, time) for course, (date, time, _) in schedule.items() if course in student_courses
            ]
            if len(set(student_slots)) != len(student_slots):
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

    current_schedule = random_schedule()
    current_energy = energy(current_schedule)
    temperature = 100.0
    cooling_rate = 0.95

    while temperature > 1:
        new_schedule = neighbor(current_schedule)
        new_energy = energy(new_schedule)

        if acceptance_probability(current_energy, new_energy, temperature) > random.random():
            current_schedule = new_schedule
            current_energy = new_energy

        temperature *= cooling_rate

    result = {'exams': [], 'students': []}
    for course, (date, time, room) in current_schedule.items():
        students_in_course = [s for s, sc in students.items() if course in sc]
        faculty = [f for f, at in faculty_availability.items() if time in at][0]
        result['exams'].append({'course': course, 'date': date, 'time': time, 'faculty': faculty})
        for student in students_in_course:
            result['students'].append({'student': student, 'room': room, 'time': time, 'date': date})

    return result


