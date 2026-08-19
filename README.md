# Student Registration System

A command-line student registration system written in Python. The program allows users to view courses, search for course details, view student registration information, register students for courses, and drop students from courses.

## Features

- View all available courses
- Sort courses by:
  - Ticket number
  - Course code
- View detailed information for a specific course
- View students currently enrolled in a course
- View a student's registered courses
- Register a student for a course
- Drop a student from a course
- Prevent duplicate registrations
- Prevent registration for invalid course tickets
- Enforce a maximum of 12 registered units per student
- Enforce a maximum course capacity of 15 students

## Project Structure

```text
Final Project/
│
├── student_registration.py
├── data_utils.py
├── README.md
│
└── data/
    ├── students.dic
    ├── courses.dic
    └── registration.dic
