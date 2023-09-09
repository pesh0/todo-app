from functions import get_todos, write_todos
import time

print("It is "+time.strftime("%x %H:%M:%S"))
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            printing = f"{int(index) + 1} - {item}"
            print(printing)

    elif user_action.startswith("edit"):
        try:
            todos = get_todos("todos.txt")

            number = input("Enter the number of the todo edit: ")
            todos[int(number) - 1] = input("Edit the todo: ") + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            todos = get_todos("todos.txt")

            number = input("Enter the number of the completed todo: ")
            todo_to_remove = todos[int(number) - 1].strip('\n')
            todos.pop(int(number) - 1)
            message = f"Todo {todo_to_remove} was removed from the list."
            write_todos(todos)

            print(message)
        except IndexError:
            print("The todo you want to remove isn't existing")
            continue
    elif user_action.startswith("exit"):
        break
