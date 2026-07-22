#!/usr/bin/env python3

"""
author: Noah Cho
date: 7/13/26
desc: Thie module contains functions for data retrieval and organization regarding student
registration.
"""


FILENAMEA = "students.dic"
FILENAMEB = "courses.dic"

def main():
    list = read_student_ID()
    list_b = creating_2d_list(list)

    print(list_b[0][0])

def read_student_ID():
    try:
        with open(FILENAMEA) as f:
            student_info = f.readlines()
        return student_info
    except FileNotFoundError:
        print(f"Could not find the {FILENAMEA} file.")
    except Exception as e:
        print(type(e), e)
    return ""

def read_courses():
    try: 
        with open(FILENAMEB) as c:
            courses = c.readlines()
            return courses
    except FileNotFoundError:
        print(f"Could not find the {FILENAMEB} file.")
    except Exception as e:
        print(type(e), e)
    return ""

def creating_2d_list(list):
    count = 0
    two_d_array = []
    for line in list:
        internal_list = []
        start_comma = 0
        end_comma = 0
        for char in line:
            if char == ",":
                if start_comma > 0:
                    internal_list.append(line[start_comma:end_comma])
                    start_comma = end_comma +1
                elif start_comma == 0:
                    internal_list.append(line[:end_comma])
                    start_comma = end_comma +1
            end_comma += 1
        internal_list.append(line[start_comma:end_comma])
        two_d_array.append(internal_list)
    
    return two_d_array


    
if __name__ =="__main__":
    main()