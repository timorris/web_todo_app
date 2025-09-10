from functools import singledispatch

FILE_PATH='.'

def get_todos(filename='todos.txt'):
    """ Read a text file and return the list of to-do items. """
    with open(f'{FILE_PATH}/{filename}', 'r') as file:
        return file.readlines()

def write_todos(contents, filename='todos.txt'):
    """ Append to the list of to-do items in a text file. """
    with open(f'{FILE_PATH}/{filename}', 'w') as file:
        file.writelines(contents)

if __name__ == "__main__":
    print("\nGreetings from functions!\n")