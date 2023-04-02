FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # Default parameter
    with open(filepath, 'r') as file:  # version without file.close()
        todos_local = file.readlines()
    return todos_local


def save_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:  # version without file.close()
        file.writelines(todos_arg)

