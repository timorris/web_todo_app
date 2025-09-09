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

def check_password(_password, length=8):
    """ Evaluate a given password by the provided length and other criteria. Returns a dictionary of results. """
    _result = {}
    _isDigit = False
    _isUpper = False
    _isLower = False
    _isSpecialChar = False

    if len(_password) >= length:
        _result['length'] = True
    else:
        _result['length'] = False

    if any(char.isdigit() for char in _password):
        _isDigit = True

    _result['IsDigit'] = _isDigit

    if any(char.isupper() for char in _password):
        _isUpper = True

    _result['IsUpper'] = _isUpper

    if any(char.islower() for char in _password):
        _isLower = True

    _result['IsLower'] = _isLower

    if any(not char.isalnum() for char in _password):
        _isSpecialChar = True

    _result['IsSpecialChar'] = _isSpecialChar

    return _result

def get_average():
    """ Gets the average based on the contents of a text file """
    with open("../files/data.txt") as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)

    return average_local

@singledispatch
def process(value):
    print("Default processing:", value)

@process.register(int)
def _(value):
    print("Processing an integer:", value)

@process.register(str)
def _(value):
    print("Processing a string:", value)

print(f"__name__ is {__name__}")
if __name__ == "__main__":
    print("\nGreetings from functions!\n")