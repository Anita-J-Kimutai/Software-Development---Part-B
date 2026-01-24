TASK MANAGEMENT SYSTEM

OVERVIEW

This program is a command-line application built in python.
It allows a user to create, delete, update and view tasks from a list.
It users file I/O to persistenly store tasks in a JSON file.
The program demonstrates the use of fundamental programming concepts i.e.
Dictionaries
Lists
variables
Functions
File handling
Error handling
User interaction

FEATURES

Add new tasks with a due date

View all tasks

Mark tasks as completed 

Delete tasks

Persistent storage - JSON 

User-friendly command-line menu

Input validation and error handling

Inline code comments for maintainability


TECHNOLOGIES USED

Python 3.14.0

Built-in Python modules:
Os – for managing file operations
JSON – for structured task storage

PROJECT FILES

File Name	Description
TMS.py - Source code
Tasks.json - Persistently stores data 
README.md	Project documentation

Running the Application
Requirements:

Install Python 3.14.0

Steps

Save the Python file as TMS.py

Open Command Prompt or Terminal.

Navigate to the folder containing the file.

Run the program using: python TMS.py



The System's menu will appears.


Menu Options

Add Task — allows user to add a task with its due date

View Tasks — allows user to view all tasks in the list

Mark Task as Completed — enables a user to update task status

Delete Task - allows user to erase a task from the list

Exit - closes the program


DATA STORAGE
The tasks are persistently store in a file named Tasks,json in JSON format allow the tasks to be saved and generated automatically evey time you program the run


Below is an example of a recorded task:
 {
    "S/No": 1,
    "Title": "Web development",
    "Due_date": "2026-01-25",
    "completed": true
  }

ERROR HANDLING

The system incorporates error handling to manage:

Non-numeric serial number inputs
Invalid menu selections
Empty fields i.e. due date/task description
User-friendly messages to guide users on errors

DOCUMENTATION

The source code uses inline comments to improve readability and maintainability of the code. It explains:

Error handling mechanisms
File I/O operations
Loops and conditions
Use of functions
Use of lists and dictionaries





