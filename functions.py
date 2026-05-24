from constants import file_constant
import json

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\n-------------")
        print("There are no tasks")
        print("-------------\n")

    else:
        print("\n-------------")
        print("Tasks:")
        for i, task in enumerate(tasks, start= 1):
            if task["done"]:
                status = "X"
            else:
                status = ""
            print(f"{i}. '{task['task']}' [ {status} ]")
        print("-------------\n")

def add_task(tasks):
    task = input("Enter a task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added")
    else:
        print("Enter a valid task")

def remove_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks to remove")
        return

    view_tasks(tasks)
    try:

        removed_task = int(input("Enter the task you would like to remove: "))
                
        if 1 <= removed_task <= len(tasks):
            removed = tasks.pop(removed_task - 1)
            print(f"Task '{removed}' removed.")

        else:
            print("Such a task doesn't exist")

    except ValueError:
        print("Entered input isn't valid")

def complete_tasks(tasks):
    if len(tasks) == 0:
       print("There are no tasks to remove")
       return
    view_tasks(tasks)
    try:

        completed_task = int(input("Enter the task you would like to complete: "))
                
        if 1 <= completed_task <= len(tasks):
            tasks[completed_task - 1]['done'] = not tasks[completed_task - 1]['done']
            if tasks[completed_task - 1]['done']:
                print(f"Task '{tasks[completed_task - 1]['task']}' completed.")
            else:
                print(f"Task '{tasks[completed_task - 1]['task']}' status changed.")

        else:
            print("Such a task doesn't exist")

    except ValueError:
        print("Entered input isn't valid")


def load_tasks():
    try:
        with open(file_constant) as file:
            opened = json.load(file)
            return opened
        
    except FileNotFoundError:
        tasks = []
        return tasks

def save_tasks(tasks):
    with open(file_constant, "w") as file:
        json.dump(tasks, file, indent=4)