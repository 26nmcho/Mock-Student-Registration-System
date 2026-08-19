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
    select = input("Enter selection: ")
    if select == "list":
        list()
    elif select == "detail":
        detail()
    elif select == "info":
        info()

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
        print(f"Good Morning {list[2]}, what would you like to do today?")
    elif 12 <=  hour < 17:
        print(f"Good Afternoon {list[2]}, what would you like to do today?")
    elif 17 <=  hour < 24:
        print(f"Good Evening {list[2]}, what would you like to do today?")
    
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
        print(f"{len(courses_sorted)}")
    elif ticket_o_code == "c":
        courses = data_utils.read_courses()
        courses_b = data_utils.creating_2d_list(courses)
        tickets = []
        for line in courses_b:
            if line[1] == "code":
                continue
            else:
                tickets.append(line[1])
        tickets.sort()
        courses_sorted = []
        for element in tickets:
            for line in courses_b:
                if element == line[1]:
                    courses_sorted.append(line)
        print("Course Listing by Ticket Number")     
        display_course_info(courses_sorted)
        print(f"{len(courses_sorted)}")
      
    else:
        print("Your input is invalid try again.")
        print()
        list()

def display_course_info(course):
    print("Ticket".ljust(7), "Code".ljust(10), "Course Name".ljust(44), "Units".ljust(7), "Day".ljust(7), "Time".ljust(15), "Instructure")
    print("=" * 120)
    for line in course:
        print(line[0].ljust(7), line[1].ljust(10), line[2].ljust(46), f"{float(line[3])}".ljust(5), line[4].ljust(7), line[5].ljust(15), line[6])

def detail():
    ticket = input("Enter course ticket # (or 'exit): ")
    ticket_tries = 0
    if ticket != "exit":
        courses = data_utils.read_courses()
        courses_b = data_utils.creating_2d_list(courses)
        for line in courses_b:
            if line[0] == ticket:
                print(f"Code {line[1]} Course Name: {line[2]} Units: {float(line[3])} Day: {line[4]} Time: {line[5]} Instrucutor: {line[6]}")
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
                    print(student[0].ljust(14), student[1].ljust(16), student(2))
                print(f"Total Students Registered: {num_of_students}")
            else: 
                ticket_tries += 1
    if ticket_tries == len(courses_b):
        print(f"{ticket} not found")
        print()
        detail()

def info():
    student_id = input("Student ID")
    students = data_utils.read_student_ID()
    students_b = data_utils.creating_2d_list(students)
    courses = []
    filtered_courses = []
    courses_2d = []
    for student in students_b:
        if student[0] == student_id:
            list = return_student_info(student_id, True)
            print(f"{list[1], {list[2]}}")
            print()
            print("Registered Courses")
            registered = data_utils.read_registered()
            registered_b = data_utils.creating_2d_list(registered)
            for registered in registered_b:
                if registered[0] == student_id:
                    courses.append(registered[1])
            courses_a = data_utils.read_courses()
            courses_b = data_utils.creating_2d_list(courses_a)
            for course in courses_b:
                for registered_course in courses:
                    if registered_course == course[0]:
                        courses_2d.append(course)
            display_course_info(courses_2d)
            
                

if __name__ == "__main__":
    main()