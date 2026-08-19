#!/usr/bin/env python3

"""
author: Noah Cho
date: 7/13/26
desc: This module executes the main code for the student registration program
and also calls the data module in order to access course, reigstration, and student files
"""
from datetime import datetime
import data_utils
import sys

def main():
    welcome()

# function displays all welcome info such as time of day and menu
def welcome():
    print("Saddleback College Registration\n")
    while True:
        student_id = input("Enter Student ID (or 'exit) to exit the application: ")
        if student_id == "exit":
            print("Session ended.")
            sys.exit()
        is_student_real = does_contain_ID(student_id)
        
        if is_student_real == True:
            break
        elif is_student_real == False:
            print("Student ID not found, please try again.")
    menu(student_id)
    while True:
        select = input("Enter selection: ").lower()
        print()
        if select == "list":
            list()
            print()
        elif select == "detail":
            detail()
            print()
        elif select == "info":
            info(student_id)
            print()
        elif select == "register":
            register(student_id)
            print()
        elif select == "drop":
            drop(student_id)
            print()
        elif select == "menu":
            commands()
            print()
        elif select == "exit":
            print("Session ended.")
            sys.exit()
        else:
            print("Invalid selection, please try again.")
            print()

# if the studentID entered is in the document then it returns true
def does_contain_ID(student_id):
    list = data_utils.read_student_ID()
    list_b = data_utils.creating_2d_list(list)
    for line in list_b:
        if line[0] == student_id:
            return True
    return False


def return_student_info(student_id, is_student_real):
    if is_student_real:
        list = data_utils.read_student_ID()
        list_b = data_utils.creating_2d_list(list)
        for line in list_b:
            if line[0] == student_id:
                return line
    print("")

def menu(student_ID):
    list = return_student_info(student_ID, True)
    time = datetime.now()
    hour = int(time.strftime("%H"))
    print()
    if 0 <=  hour < 12:
        print(f"Good Morning {list[2].strip()}, what would you like to do today?")
    elif 12 <=  hour < 17:
        print(f"Good Afternoon {list[2].strip()}, what would you like to do today?")
    elif 17 <=  hour < 24:
        print(f"Good Evening {list[2].strip()}, what would you like to do today?")
    
    commands()

def commands():
    print()
    print("list - Full course listing")
    print("detail - Course detail information")
    print("info - Student information")
    print("register - Register for a class")
    print("drop - drop a class")
    print("menu - menu")
    print("exit - End session")
    print()

def list():
    ticket_o_code = input("Sort by ticket # or course code (t/c): ")
    if ticket_o_code == "t":
        courses = data_utils.read_courses()
        courses_b = data_utils.creating_2d_list(courses)
        tickets = []
        for line in courses_b:
            if line[0] == "ticket":
                continue
            else:
                tickets.append(line[0])
        tickets.sort()
        courses_sorted = []
        for element in tickets:
            for line in courses_b:
                if element == line[0]:
                    courses_sorted.append(line)
        print("Course Listing by Ticket Number")     
        display_course_info(courses_sorted)
        print(f"{len(courses_sorted)} Courses")
    elif ticket_o_code == "c":
        courses = data_utils.read_courses()
        courses_b = data_utils.creating_2d_list(courses)
        tickets = []
        for line in courses_b:
            if line[1] == "code":
                continue
            else:
                if line[1] not in tickets:
                    tickets.append(line[1])
        tickets.sort()
        courses_sorted = []
        for element in tickets:
            for line in courses_b:
                if element == line[1]:
                    courses_sorted.append(line)
        print("Course Listing by Course Code")     
        display_course_info(courses_sorted)
        print(f"{len(courses_sorted)} Courses")
      
    else:
        print("Your input is invalid try again.")
        print()
        list()

def display_course_info(course):
    print("Ticket".ljust(7), "Code".ljust(10), "Course Name".ljust(44), "Units".ljust(7), "Day".ljust(7), "Time".ljust(15), "Instructor")
    print("=" * 120)
    for line in course:
        print(line[0].ljust(7), line[1].ljust(10), line[2].ljust(46), f"{float(line[3])}".ljust(5), line[4].ljust(7), line[5].ljust(15), line[6])

def detail():
    ticket = input("Enter course ticket # (or 'exit): ")
    ticket_tries = 0
    if ticket == "exit":
        return
    if ticket != "exit":
        courses = data_utils.read_courses()
        courses_b = data_utils.creating_2d_list(courses)
        for line in courses_b:
            if line[0] == ticket:
                print()
                print(f"Code: {line[1]} Course Name: {line[2]} Units: {float(line[3])} Day: {line[4]} Time: {line[5]} Instrucutor: {line[6]}")
                print()
                print("Enrolled Students")
                print("=" * 100)
                registered = data_utils.read_registered()
                registered_b = data_utils.creating_2d_list(registered)
                student_codes = []
                num_of_students = 0
                for line in registered_b:
                    if line[1] == ticket:
                        student_codes.append(line[0])
                        num_of_students +=1
                for line in student_codes:
                    student = return_student_info(line, True)
                    print(student[0].ljust(14), student[1].ljust(16), student[2])
                print(f"Total Students Registered: {num_of_students}")
            else: 
                ticket_tries += 1
    if ticket_tries == len(courses_b):
        print(f"{ticket} not found")
        print()
        detail()

def info(student_id):
    students = data_utils.read_student_ID()
    students_b = data_utils.creating_2d_list(students)
    courses = []
    courses_2d = []
    for student in students_b:
        if student[0] == student_id:
            print(f"{student[1]}, {student[2]}")
            print()
            print("Registered Courses")
            registered_a = data_utils.read_registered()
            registered_b = data_utils.creating_2d_list(registered_a)
            for registered in registered_b:
                if registered[0] == student_id:
                    courses.append(registered[1].strip())
            courses_a = data_utils.read_courses()
            courses_b = data_utils.creating_2d_list(courses_a)
            for course in courses_b:
                if course[0] in courses:
                    courses_2d.append(course)
            units = 0
            for x in courses_2d:
                units += float(x[3])
            display_course_info(courses_2d)
            print(f"{len(courses)} Course(s) Registered                                   Units: {units}")
            return 

def register(student_id):
    course = input("Enter course ticket # (or 'exit'): ")
    if course == "exit":
        return
    can_add = True


    #is the student already in the course
    registered_a = data_utils.read_registered()
    registered_b = data_utils.creating_2d_list(registered_a)
    for registered in registered_b:
        if registered[1].strip() == course and registered[0] == student_id:
            print(f"{student_id} is already in {course}")
            can_add = False

    # is the course real
    courses_a = data_utils.read_courses()
    courses_b = data_utils.creating_2d_list(courses_a)
    courses_c = []
    for course_d in courses_b:
        if course_d[0] == "ticket":
            continue
        courses_c.append(course_d[0])
    if course not in courses_c:
        print(f"{course} not found.")
        can_add= False

    # cannot exceed 12 units
    course_units = 0
    for course_e in courses_b:
        if course_e[0] == course:
            course_units = float(course_e[3])
    courses = []
    courses_2d = []
    for registered in registered_b:
        if registered[0] == student_id:
            courses.append(registered[1].strip())
    for course_f in courses_b:
        if course_f[0] in courses:
            courses_2d.append(course_f)
            units = 0
    for x in courses_2d:
        units += float(x[3])
        if units + course_units > 12:
            can_add = False
            print("This would exceed the maximum number of units allowed.")

    # cannot exceed 15 students
    how_many_students = 0
    for registered in registered_b:
        if course == registered[1].strip():
            how_many_students +=1

    if how_many_students == 15:
        can_add = False
        print(f"{course} is full.")

    if can_add == True:
        info = f"{student_id},{course}"
        data_utils.write_registered(info)
        print(f"{student_id} was added to {course}")

def drop(student_id):
    course = input("Enter course ticket # (or 'exit'): ")
    found = False
    if course == "exit":
        return

    courses_a = data_utils.read_courses()
    courses_b = data_utils.creating_2d_list(courses_a)
    courses_c = []
    for course_d in courses_b:
        if course_d[0] == "ticket":
            continue
        courses_c.append(course_d[0])
    if course not in courses_c:
        print(f"{course} not found.")
    else:
        registered_a = data_utils.read_registered()
        registered_b = data_utils.creating_2d_list(registered_a)
        for registered in registered_b:
            if registered[0] == student_id and registered[1].strip() == course:
                delete_target = f"{student_id},{course}"
                print(f"{student_id} was dropped from {course}")
                data_utils.delete_registered(registered_a, delete_target)
                found = True

        if found == False:
            print(f"{student_id} is not enrolled in {course}")




    
    

            
                

if __name__ == "__main__":
    main()