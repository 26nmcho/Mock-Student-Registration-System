#!/usr/bin/env python3

"""
author: Noah Cho
date: 7/13/26
desc: This module executes the main code for the student registration program
and also calls the data module in order to access course, reigstration, and student files
"""

import data_utils
import sys

def main():
    welcome()


def welcome():
    print("Saddleback College Registration")
    while True:
        student_id = input("Enter Student ID (or 'exit) to exit the application: ")
        if student_id == "exit":
            print("Session ended.")
            sys.exit()
        is_student_real = does_contain_ID(student_id)
        print(is_student_real)
        
        if is_student_real == True:
            break
        elif is_student_real == False:
            print("Student ID not found, please try again.")
    menu()

def does_contain_ID(student_id):
    list = data_utils.read_student_ID()
    list_b = data_utils.creating_2d_list(list)
    for line in list_b:
        if line[0] == student_id:
            return True
    return False

def return_student_infor(student_id, is_student_real):
    if is_student_real:
        list = data_utils.read_student_ID()
        list_b = data_utils.creating_2d_list(list)
        for line in list_b:
            if line[0] == student_id:
                return line
    print("")

def menu():

if __name__ == "__main__":
    main()