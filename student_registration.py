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
    list()
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
    print("dorp - drop a class")
    print("menu - menu")
    print("exit - End session")

def list():
    ticket_o_code = input("Sort by ticket # or course code (t/c): ")
    if ticket_o_code == "t":
        courses = data_utils.read_courses()
        courses_b = data_utils.creating_2d_list(courses)
        tickets = []
        for line in courses_b:
            tickets.append(line[0])
        tickets.sort()
        courses_sorted = []
        for element in tickets:
            for line in courses_b:
                if element == line[0]:
                    courses_sorted.append(line)
        display_course_info(courses_sorted)

def display_course_info
    

if __name__ == "__main__":
    main()