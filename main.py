##Peab olema võimekus:
#Lisada taske
#Kuvada taske
#Eemaldada taske
#67

def main():

    tasks = []

    def view_tasks():
        if len(tasks) == 0:
            print("\n-------------")
            print("There are no tasks")
            print("-------------\n")

        else:
            print("\n-------------")
            print("Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            print("-------------\n")



    while True:
        print("\n-------------")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Remove tasks")
        print("4. Exit")
        print("-------------\n")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()

        elif choice == "2":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print("Task added")
            else:
                print("Enter a valid task")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove")
                continue

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

        elif choice == "4":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
