# Module 7 - Course Information System

course_room = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

course_instructor = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_time = {
    "CSC101": "9:00 AM",
    "CSC102": "10:00 AM",
    "CSC103": "11:00 AM",
    "NET110": "1:00 PM",
    "COM241": "2:00 PM"
}

course_number = input("Enter a course number:\n")

if course_number in course_room:
    print(f"Course: {course_number}")
    print(f"Room Number: {course_room[course_number]}")
    print(f"Instructor: {course_instructor[course_number]}")
    print(f"Meeting Time: {course_time[course_number]}")
else:
    print("Course not found. Please try again.")
