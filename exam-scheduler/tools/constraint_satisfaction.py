from ortools.sat.python import cp_model
# from data.data_set import courses, test_dates, time_slots, rooms, room_capacity, students, faculty_availability
from data.database import courses, time_slots, rooms, room_capacity, students, faculty_availability

def generate_schedule_csp(dates):

    # dates = test_dates

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

    result = {'exams': [], 'students': []}
    
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        for course in courses:
            for date in dates:
                for time in time_slots:
                    for room in rooms:
                        if solver.Value(exam_schedule[(course, date, time, room)]) == 1:
                            faculty = [
                                f for f, times in faculty_availability.items() if time in times
                            ][0]
                            students_in_course = [s for s, sc in students.items() if course in sc]
                            result['exams'].append({'course': course, 'date': date, 'time': time, 'faculty': faculty})
                            for student in students_in_course:
                                result['students'].append({'student': student, 'room': room, 'time': time, 'date': date})
    
    return result

