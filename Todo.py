todoList = []


def showMenu():
    print("=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit \n")


while True:
    showMenu()
    task = input("What would you like to do? \n").strip().lower()

    if task == "add task" or task == "1":
        addTask = input("What task do you want to add? \n")
        todoList.append(addTask)
        print(f"You added {addTask} to your todo list.\n")

    elif task == "view tasks" or task == "2":
        if len(todoList) == 0:
            print("Your todo list is Empty!\n")
        else:
            for index, task in enumerate(todoList):
                print("Your tasks include: ")
                print(f"{index + 1}: {task}\n")

    elif task == "delete task" or task == "3":
        try:
            deleteTask = int(input("Enter the number of the task to delete: \n"))
            print(f"You removed {todoList[deleteTask - 1]} from your todo list.\n")
            todoList.pop(deleteTask - 1)
        except ValueError:
            print("Please enter a valid number.\n")
        except IndexError:
            print("Task does not exist.\n")

    elif task == "quit" or task == "4":
        break

    else:
        print("Invalid option, please try again.\n")
