
#validates date
import datetime

# to store and load tasks from a file
import json

# it checks if a file exists before reading it
import os

#This is the file where tasks will be stored
StoredTasks= "tasks.json"

"""
This function loads tasks from the JSON file
It returns an empty list if the file doesn't exist
"""
def generate_tasks():

    #checks if file exists before attempting to open the file
    if os.path.exists(StoredTasks):

        #opens file stored in StoredTasks in read mode
        with open(StoredTasks, "r") as f:    
            return json.load(f)
    return []

"""
This function saves tasks to the JSON file.
Ensures persistance
"""
def stored_tasks(tasks):

    #opens file stored in StoredTasks in write mode
    #saves the tasks in json format
    with open(StoredTasks, "w") as f:
        #writes into the file, indenting makes it easy to read     
        json.dump(tasks, f, indent=2)     

#Function to validate date
def valid_due_date():
    """
    Prompts user to enter a valid date in te format YYYY-MM-DD
    """
    while True:
        due_date = input("Enter Due date (YYYY-MM-DD): ").strip()

        try:
            #Converts string to  date object
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
            return due_date  #returns a valid date
        
        except ValueError:
            #Error message when uses enters incorrect date format
            print("Invalid date format. Please enter date as YYYY-MM-DD (for example, 2000-06-29).")


#Function to add new task to the tasks list
def add_task(tasks):
    
    title = input("Enter task: ").strip()     #prompts a user to write a task
    due_date = valid_due_date()     #Calls the valid_due_date() function to get due date

    #Error message below appears if user does not enter either the task name or due date
    if not title:
        print("Error!! Task description or due date cannot be empty.")
        return

    task = {

            #len(tasks) - counts how many tasks are already in the list
            #+ 1 - adds one to the numer of taks in the list     
        
        "id": len(tasks) + 1,     #Assign each task a unique serial number
        "title": title,
        "due_date": due_date,
        "completed": False     #task is marked incomplete immediately its keyed in.
    }

    tasks.append(task)     #adds new task at the end of the list
    stored_tasks(tasks)     #writes the newly added task to the JSON file
    print("Task added!")

#Function to display tasks
def display_task(tasks):

#The message below is displayed if no task has been written to the list
    if not tasks:
        print("No tasks available")
        return

    print("\nMy To-Do List:")    #list tittle

    print("-" * 50)    #prints horizontal separator line made up of 50 dashes(-)
    for task in tasks:
        """
         Deremines task status using tick and cross
         ✘ for incomplete tasks
         ✔ for completed tasks
        """
        status = "✔ Completed" if task.get("completed", False) else "✘ Pending" 
        
        print(f"S/No: {task['id']}")
        print(f"Task: {task['title']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {status}")
        print("-" * 50)     #prints horizontal separator line made up of 50 dashes(-)
    
#Function to mark task as completed using their serial number
def mark_taskComplete(tasks):

    try:
        task_sno = int(input("Enter task Serial number(S/No): "))
    
    #For non-numeric value. If users enters another data type the error message is displayed
    except ValueError:
        print("Error! Please enter a valid serial number")
        return

    #Loops through the list to find a matching serial number
    for task in tasks:
        if task["id"] == task_sno:
            task["completed"] = True
            stored_tasks(tasks)     #saves update to the JSON file
            print("Marked as complete!")
            return

    print("Error! Task serial number not found.")

#Function to delete tasks using their serial number
def del_task(tasks):
    
    try:
        task_sno = int(input("Enter task serial number (S/No): "))

     #For non-numeric value. If users enters another data type the error message is displayed
    except ValueError:
        print("Error! Please enter a valid serial number")
        return

    #Loops through the list to find a matching serial number
    for task in tasks:
        if task["id"] == task_sno:
            tasks.remove(task)       #deletes task whose serial numer has been selected

            # Reassign serial number after a task has been deleted ensuring theyremain sequential
            for index, task in enumerate(tasks):
                task["id"] = index + 1

            stored_tasks(tasks)     #saves the updates to the JSON file
            print("Task deleted!")
            return

    #error message displayed when a user enters a serial number that is not in the list
    print("Error: Task ID not found.")     

#Fuction for the program loop
def main():
    """
        This is the main program loop
        It controls the program flow and how a user interacts with the program
        
    """

    tasks =generate_tasks()     #loads tasks in the list
    
    #displays the main menu
    print("\nTask Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    while True:
        
        #Allows user to choose from the menu options
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_task(tasks)
        elif choice == "3":
            mark_taskComplete(tasks)
        elif choice == "4":
            del_task(tasks)
        elif choice == "5":
            print("Bye!")
            break
        else:
            
            #if user does not select options 1-5 this error message is diplayed
            print("Invalid choice! Try again.")     

# It makes sure the main funtion runs when file is directly executed
if __name__ == "__main__":
    main()
    
