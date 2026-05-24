##Peab olema võimekus:
#Lisada taske
#Kuvada taske
#Eemaldada taske
import json

def main():

    file_constant = "tasks.json"

    def view_tasks():
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

    def add_task():
        task = input("Enter a task: ").strip()
        if task:
            tasks.append({"task": task, "done": False})
            print("Task added")
        else:
            print("Enter a valid task")

    def remove_task():
        if len(tasks) == 0:
            print("There are no tasks to remove")
            return

        view_tasks()
        try:

            removed_task = int(input("Enter the task you would like to remove: "))
                    
            if 1 <= removed_task <= len(tasks):
                removed = tasks.pop(removed_task - 1)
                print(f"Task '{removed}' removed.")

            else:
                print("Such a task doesn't exist")

        except ValueError:
            print("Entered input isn't valid")

    def complete_tasks():
        if len(tasks) == 0:
           print("There are no tasks to remove")
           return
        view_tasks()
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

    def save_tasks():
        with open(file_constant, "w") as file:
            json.dump(tasks, file, indent=4)

    tasks = load_tasks()

    while True:


        print("\n-------------")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Remove tasks")
        print("4. Complete a task")
        print("5. Exit")
        print("-------------\n")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()

        elif choice == "2":
            add_task()
            save_tasks()

        elif choice == "3":
            remove_task()
            save_tasks()

        elif choice == "4":
            complete_tasks()
            save_tasks()

        elif choice == "5":
            save_tasks()
            print("\nTasks saved.")
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
