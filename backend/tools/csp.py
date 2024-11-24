from datetime import datetime, timedelta
from backend.db.operations import fetch_data, execute_query
from backend.tools.constraints import constraints, time_slots


def schedule_exams(start_date, end_date, exam_name):
    faculty = fetch_data("SELECT * FROM faculty")
    courses = fetch_data("SELECT * FROM courses")
    rooms = fetch_data("SELECT * FROM rooms")
    
    # Parse constraints
    max_exam_hours = constraints['max_hours_invigilation_per_day']
    min_day_gap = constraints['min_day_gap_between_exams']
    no_exam_on_sunday = constraints['no_exam_on_sunday']
    
    schedule = []
    
    
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    dates = []

    
    while current_date <= end_date:
        if not (no_exam_on_sunday and current_date.weekday() == 6):  # Exclude Sundays if required
            dates.append(current_date)
        current_date += timedelta(days=1 + min_day_gap)

    # Cache faculty and room assignments for efficiency
    faculty_cache = {member["id"]: member for member in faculty}
    room_cache = {room["id"]: room for room in rooms}

    
    # Assign exams
    # Loop through each course for each available time slot and date
    for course in courses:
        for date in dates:
            for slot, duration in time_slots:
                if duration > max_exam_hours:
                    continue

                # if not is_valid_gap(date, course, faculty_cache, min_day_gap):
                #     continue

                assigned_room = assign_room(room_cache, course["student_count"], date.strftime("%Y-%m-%d"), slot)
                if not assigned_room:
                    continue

                assigned_faculty = assign_faculty(faculty_cache, date.strftime("%Y-%m-%d"), slot)
                if not assigned_faculty:
                    continue

                schedule.append({
                    "course_id": course["id"],
                    "exam_date": date.strftime("%Y-%m-%d"),
                    "exam_time": slot,
                    "room_id": assigned_room["id"],
                    "faculty_id": assigned_faculty["id"],
                    "exam_name": exam_name
                })

                # Insert into the exams table
                query = """
                    INSERT INTO exams (course_id, exam_date, exam_time, room_id, faculty_id, exam_name)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                execute_query(query, (
                    course["id"], date.strftime("%Y-%m-%d"), slot,
                    assigned_room["id"], assigned_faculty["id"], exam_name
                ))


    
    # for date in dates:
    #     for slot, duration in time_slots:
    #         for course in courses:
    #             if duration > max_exam_hours:
    #                 continue
                
    #             if not is_valid_gap(date, course, faculty_cache, min_day_gap):
    #                 continue
                
    #             assigned_room = assign_room(room_cache, course["student_count"], date.strftime("%Y-%m-%d"), slot)
    #             if not assigned_room:
    #                 continue
                
    #             assigned_faculty = assign_faculty(faculty_cache, date.strftime("%Y-%m-%d"), slot)
    #             if not assigned_faculty:
    #                 continue
                
    #             schedule.append({
    #                 "course_id": course["id"],
    #                 "exam_date": date.strftime("%Y-%m-%d"),
    #                 "exam_time": slot,
    #                 "room_id": assigned_room["id"],
    #                 "faculty_id": assigned_faculty["id"],
    #                 "exam_name": exam_name
    #             })
                
    #             # Insert into the exams table
    #             query = """
    #                 INSERT INTO exams (course_id, exam_date, exam_time, room_id, faculty_id, exam_name)
    #                 VALUES (%s, %s, %s, %s, %s, %s)
    #             """
    #             execute_query(query, (
    #                 course["id"], date.strftime("%Y-%m-%d"), slot,
    #                 assigned_room["id"], assigned_faculty["id"], exam_name
    #             ))



    return {"message": "Exams scheduled successfully", "schedule": schedule}




# def is_valid_gap(exam_date, course, faculty_cache, min_day_gap):
#     """Check if the minimum day gap constraint is respected for a faculty or course."""
#     # Check if there is already an exam for the same course within the min_day_gap range
#     min_date = exam_date - timedelta(days=min_day_gap)
#     max_date = exam_date + timedelta(days=min_day_gap)
    
#     # Check course exams
#     query = """
#         SELECT * FROM exams
#         WHERE course_id = %s AND exam_date BETWEEN %s AND %s
#     """
#     results = fetch_data(query, (course["id"], min_date.strftime("%Y-%m-%d"), max_date.strftime("%Y-%m-%d")))
#     if results:
#         return False  # A conflicting exam already exists for this course

#     # Check faculty exams
#     query = """
#         SELECT * FROM exams
#         WHERE faculty_id = %s AND exam_date BETWEEN %s AND %s
#     """
#     for member in faculty_cache.values():
#         results = fetch_data(query, (member["id"], min_date.strftime("%Y-%m-%d"), max_date.strftime("%Y-%m-%d")))
#         if results:
#             return False  # Faculty is already booked within the required gap

#     return True  # No conflict

def assign_faculty(faculty_cache, exam_date, exam_time):
    """Assign an available faculty member."""
    for member in faculty_cache.values():
        # Check if the faculty member is already assigned at this time
        query = """
            SELECT * FROM exams
            WHERE faculty_id = %s AND exam_date = %s AND exam_time = %s
        """
        results = fetch_data(query, (member["id"], exam_date, exam_time))
        if not results:
            return member
    return None

def assign_room(room_cache, student_count, exam_date, exam_time):
    """Assign an available room based on capacity."""
    for room in room_cache.values():
        if room["capacity"] >= student_count:
            # Check if the room is already booked at this time
            query = """
                SELECT * FROM exams
                WHERE room_id = %s AND exam_date = %s AND exam_time = %s
            """
            results = fetch_data(query, (room["id"], exam_date, exam_time))
            if not results:
                return room
    return None




# v1
# def schedule_exams(start_date, end_date, exam_name):
#     """Schedule exams with room and faculty constraints."""
#     # Fetch data
#     faculty = fetch_data("SELECT * FROM faculty")
#     courses = fetch_data("SELECT * FROM courses")
#     rooms = fetch_data("SELECT * FROM rooms")

#     # Check if data was fetched correctly
#     if not faculty or not courses or not rooms:
#         return {"message": "Missing data: faculty, courses, or rooms not available"}

#     # Parse constraints
#     max_exam_hours = constraints['max_hours_invigilation_per_day']
#     min_day_gap = constraints['min_day_gap_between_exams']
#     no_exam_on_sunday = constraints['no_exam_on_sunday']

#     # Initialize schedule and available time slots
#     schedule = []
#     time_slots = [("9:00 AM - 12:00 PM", 3), ("1:00 PM - 4:00 PM", 3)]
    
#     # Generate valid dates (excluding Sundays if required)
#     current_date = datetime.strptime(start_date, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date, "%Y-%m-%d")
#     dates = []
#     while current_date <= end_date:
#         if not (no_exam_on_sunday and current_date.weekday() == 6):  # Exclude Sundays if required
#             dates.append(current_date)
#         current_date += timedelta(days=1)

#     # Cache faculty and room assignments for efficiency
#     faculty_cache = {member["id"]: member for member in faculty}
#     room_cache = {room["id"]: room for room in rooms}

#     # Schedule exams
#     for date in dates:
#         for slot, duration in time_slots:
#             for course in courses:
#                 if duration > max_exam_hours:
#                     continue

#                 # Check if there is a min_day_gap between this exam and other exams for the same course or faculty
#                 if not is_valid_gap(date, course, faculty_cache, min_day_gap):
#                     continue

#                 # Check room availability
#                 assigned_room = assign_room(room_cache, course["student_count"], date.strftime("%Y-%m-%d"), slot)
#                 if not assigned_room:
#                     logging.warning(f"Skipping exam for course {course['id']} on {date} - No available room")
#                     continue

#                 # Check faculty availability
#                 assigned_faculty = assign_faculty(faculty_cache, date.strftime("%Y-%m-%d"), slot)
#                 if not assigned_faculty:
#                     logging.warning(f"Skipping exam for course {course['id']} on {date} - No available faculty")
#                     continue

#                 # Add the exam to the schedule
#                 schedule.append({
#                     "course_id": course["id"],
#                     "exam_date": date.strftime("%Y-%m-%d"),
#                     "exam_time": slot,
#                     "room_id": assigned_room["id"],
#                     "faculty_id": assigned_faculty["id"],
#                     "exam_name": exam_name
#                 })

#                 # Insert into the exams table
#                 query = """
#                     INSERT INTO exams (course_id, exam_date, exam_time, room_id, faculty_id, exam_name)
#                     VALUES (%s, %s, %s, %s, %s, %s)
#                 """
#                 execute_query(query, (
#                     course["id"], date.strftime("%Y-%m-%d"), slot,
#                     assigned_room["id"], assigned_faculty["id"], exam_name
#                 ))

#     return {"message": "Exams scheduled successfully", "schedule": schedule}




# v2
# def schedule_exams(start_date, end_date, exam_name):
#     faculty = fetch_data("SELECT * FROM faculty")
#     courses = fetch_data("SELECT * FROM courses")
#     rooms = fetch_data("SELECT * FROM rooms")
    
#     # Parse constraints
#     max_exam_hours = constraints['max_hours_invigilation_per_day']
#     min_day_gap = constraints['min_day_gap_between_exams']
#     no_exam_on_sunday = constraints['no_exam_on_sunday']
    
#     schedule = []
#     time_slots = [("9:00 AM - 12:00 PM", 3), ("1:00 PM - 4:00 PM", 3)]
    
#     current_date = datetime.strptime(start_date, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date, "%Y-%m-%d")
#     dates = []
    
#     while current_date <= end_date:
#         if not (no_exam_on_sunday and current_date.weekday() == 6):  # Exclude Sundays if required
#             dates.append(current_date)
#         current_date += timedelta(days=1)
    
#     # Assign exams
#     for date in dates:
#         for slot, duration in time_slots:
#             for course in courses:
#                 if duration > max_exam_hours:
#                     continue
                
#                 if not is_valid_gap(date, course, faculty, min_day_gap):
#                     continue
                
#                 assigned_room = assign_room(rooms, course["student_count"], date.strftime("%Y-%m-%d"), slot)
#                 if not assigned_room:
#                     continue
                
#                 assigned_faculty = assign_faculty(faculty, date.strftime("%Y-%m-%d"), slot)
#                 if not assigned_faculty:
#                     continue
                
#                 schedule.append({
#                     "course_id": course["id"],
#                     "exam_date": date.strftime("%Y-%m-%d"),
#                     "exam_time": slot,
#                     "room_id": assigned_room["id"],
#                     "faculty_id": assigned_faculty["id"],
#                     "exam_name": exam_name
#                 })
                
#                 # Insert into the exams table
#                 query = """
#                     INSERT INTO exams (course_id, exam_date, exam_time, room_id, faculty_id, exam_name)
#                     VALUES (%s, %s, %s, %s, %s, %s)
#                 """
#                 execute_query(query, (
#                     course["id"], date.strftime("%Y-%m-%d"), slot,
#                     assigned_room["id"], assigned_faculty["id"], exam_name
#                 ))

#     return {"message": "Exams scheduled successfully", "schedule": schedule}










# from datetime import datetime, timedelta
# from backend.db.operations import fetch_data, execute_query
# from backend.tools.constraints import constraints

# def schedule_exams(start_date, end_date, exam_name, courses, rooms, faculty):
#     # Parse start and end dates
#     current_date = datetime.strptime(start_date, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
#     schedule = []
#     room_assignments = {}  # Initialize room assignments dictionary to track room bookings
#     faculty_assignments = {}  # Initialize faculty assignments dictionary to track faculty bookings

#     # Loop through each course and assign exam dates
#     for course in courses:
#         # Skip Sundays and find next valid date
#         while current_date.weekday() == 6 or current_date > end_date:  # 6 is Sunday
#             current_date += timedelta(days=1)
        
#         # Assign room and faculty
#         assigned_room = assign_room(rooms, course["student_count"], current_date.strftime("%Y-%m-%d"), room_assignments)
#         assigned_faculty = assign_faculty(faculty, current_date.strftime("%Y-%m-%d"), faculty_assignments)
        
#         # If a room or faculty is not available, continue to the next date
#         if not assigned_room or not assigned_faculty:
#             continue
        
#         # Schedule the exam
#         schedule.append({
#             "course_id": course["id"],
#             "exam_date": current_date.strftime("%Y-%m-%d"),
#             "exam_name": exam_name,
#             "exam_time": "9:00 AM - 12:00 PM",
#             "faculty_id": assigned_faculty["id"],
#             "room_id": assigned_room["id"]
#         })

#         # Move to the next valid date for the next course
#         current_date += timedelta(days=2)  # Skip one day to avoid overlapping exams
    
#     return schedule

# def assign_room(rooms, student_count, exam_date, room_assignments):
#     """Assign a room based on student count."""
#     for room in rooms:
#         if room["capacity"] >= student_count:
#             # Check if the room is already booked on this date
#             if room["id"] not in room_assignments or room_assignments[room["id"]] != exam_date:
#                 room_assignments[room["id"]] = exam_date
#                 return room
#     return None

# def assign_faculty(faculty, exam_date, faculty_assignments):
#     """Assign available faculty member."""
#     for member in faculty:
#         # Check if faculty is already assigned
#         if member["id"] not in faculty_assignments or faculty_assignments[member["id"]] != exam_date:
#             faculty_assignments[member["id"]] = exam_date
#             return member
#     return None

# # Sample data
# courses = [{"id": 1, "name": "Course 1", "student_count": 50},
#            {"id": 2, "name": "Course 2", "student_count": 40},
#            {"id": 3, "name": "Course 3", "student_count": 30}]

# rooms = [{"id": 1, "capacity": 50}, {"id": 2, "capacity": 40}]
# faculty = [{"id": 1, "name": "Faculty 1"}, {"id": 2, "name": "Faculty 2"}]

# # Example function call
# start_date = "2025-02-01"
# end_date = "2025-02-28"
# schedule = schedule_exams(start_date, end_date, courses, rooms, faculty)

# # Print the generated schedule
# for entry in schedule:
#     print(entry)












# from datetime import datetime, timedelta
# from backend.db.operations import fetch_data, execute_query
# from backend.tools.constraints import constraints

# def schedule_exams(start_date, end_date, exam_name):
#     """Schedule exams with room and faculty constraints."""
#     # Fetch data
#     faculty = fetch_data("SELECT * FROM faculty")
#     courses = fetch_data("SELECT * FROM courses")
#     rooms = fetch_data("SELECT * FROM rooms")

#     # Parse constraints
#     max_exam_hours = constraints['max_hours_invigilation_per_day']
#     min_day_gap = constraints['min_day_gap_between_exams']
#     no_exam_on_sunday = constraints['no_exam_on_sunday']

#     # Initialize schedule and available time slots
#     schedule = []
#     time_slots = [("9:00 AM - 12:00 PM", 3), ("1:00 PM - 4:00 PM", 3)]
    
#     # Generate valid dates
#     current_date = datetime.strptime(start_date, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date, "%Y-%m-%d")
#     dates = []
#     while current_date <= end_date:
#         if not (no_exam_on_sunday and current_date.weekday() == 6):  # Exclude Sundays if required
#             dates.append(current_date)
#         current_date += timedelta(days=1)

#     # Schedule exams
#     for date in dates:
#         for slot, duration in time_slots:
#             for course in courses:
#                 if duration > max_exam_hours:
#                     continue

#                 # Check if there is a min_day_gap between this exam and other exams for the same course or faculty
#                 if not is_valid_gap(date, course, faculty, min_day_gap):
#                     continue

#                 # Check room availability
#                 assigned_room = assign_room(rooms, course["student_count"], date.strftime("%Y-%m-%d"), slot)
#                 if not assigned_room:
#                     continue

#                 # Check faculty availability
#                 assigned_faculty = assign_faculty(faculty, date.strftime("%Y-%m-%d"), slot)
#                 if not assigned_faculty:
#                     continue

#                 # Add the exam to the schedule
#                 schedule.append({
#                     "course_id": course["id"],
#                     "exam_date": date.strftime("%Y-%m-%d"),
#                     "exam_time": slot,
#                     "room_id": assigned_room["id"],
#                     "faculty_id": assigned_faculty["id"],
#                     "exam_name": exam_name
#                 })

#                 # Insert into the exams table
#                 query = """
#                     INSERT INTO exams (course_id, exam_date, exam_time, room_id, faculty_id, exam_name)
#                     VALUES (%s, %s, %s, %s, %s, %s)
#                 """
#                 execute_query(query, (
#                     course["id"], date.strftime("%Y-%m-%d"), slot,
#                     assigned_room["id"], assigned_faculty["id"], "Mid term June 2024"
#                 ))

#     return {"message": "Exams scheduled successfully", "schedule": schedule}

# def is_valid_gap(exam_date, course, faculty, min_day_gap):
#     """Check if the minimum day gap constraint is respected for a faculty or course."""
#     # Check if there is already an exam for the same course within the min_day_gap range
#     query = """
#         SELECT * FROM exams
#         WHERE course_id = %s AND exam_date BETWEEN %s AND %s
#     """
#     min_date = exam_date - timedelta(days=min_day_gap)
#     max_date = exam_date + timedelta(days=min_day_gap)
#     results = fetch_data(query, (course["id"], min_date.strftime("%Y-%m-%d"), max_date.strftime("%Y-%m-%d")))
#     if results:
#         return False  # A conflicting exam already exists for this course

#     # Check faculty availability for the min_day_gap
#     query = """
#         SELECT * FROM exams
#         WHERE faculty_id = %s AND exam_date BETWEEN %s AND %s
#     """
#     for member in faculty:
#         results = fetch_data(query, (member["id"], min_date.strftime("%Y-%m-%d"), max_date.strftime("%Y-%m-%d")))
#         if results:
#             return False  # Faculty is already booked within the required gap

#     return True  # No conflict

# def assign_faculty(faculty, exam_date, exam_time):
#     """Assign an available faculty member."""
#     for member in faculty:
#         # Check if the faculty member is already assigned at this time
#         query = """
#             SELECT * FROM exams
#             WHERE faculty_id = %s AND exam_date = %s AND exam_time = %s
#         """
#         results = fetch_data(query, (member["id"], exam_date, exam_time))
#         if not results:
#             return member
#     return None

# def assign_room(rooms, student_count, exam_date, exam_time):
#     """Assign an available room based on capacity."""
#     for room in rooms:
#         if room["capacity"] >= student_count:
#             # Check if the room is already booked at this time
#             query = """
#                 SELECT * FROM exams
#                 WHERE room_id = %s AND exam_date = %s AND exam_time = %s
#             """
#             results = fetch_data(query, (room["id"], exam_date, exam_time))
#             if not results:
#                 return room
#     return None
