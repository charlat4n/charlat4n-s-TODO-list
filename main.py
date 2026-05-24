##Peab olema võimekus:
#Lisada taske
#Kuvada taske
#Eemaldada taske
import json
from functions import *

def main():

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
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)

        elif choice == "4":
            complete_tasks(tasks)
            save_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("\nTasks saved.")
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
