def main():
    tasks = []

    while True:
        print("\n======To-Do list application======")
        print("1.add task")
        print("2.show tasks")
        print("3.update task")
        print("4.delete task")
        print("5.exit")

        choice = input("enter the choice: ")

        if choice == '1':
            task = input("enter the task: ")
            tasks.append(task)
            print(f'Task "{task}" task added!')

        elif choice == '2':
            if not tasks:
           
                print("list is empty.")
            else:
                print("To-Do list:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
        elif choice == '3':
            if not tasks:
                print("To-Do list is empty.")
            else:
                print("To-Do list:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
                index = int(input("enter task number to update: ")) - 1
                new_task = input("enter the new task: ")
                if 0 <= index < len(tasks):
                    tasks[index] = new_task
                    print(f'Task {index + 1} updated to "{new_task}".')
                else:
                    print("invalid task number.")
        elif choice == '4':
            if not tasks:
                print("To-Do list is empty.")
            else:
                print("To-Do list:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
                index = int(input("enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f'Task "{removed_task}" deleted from the list.')
                else:
                    print("invalid task number.")
        elif choice == '5':
            print("goodbye!!")
            break
        else:
            print("Invalid choice enter number between 1 to 5.")
if __name__ == "__main__":
    main()