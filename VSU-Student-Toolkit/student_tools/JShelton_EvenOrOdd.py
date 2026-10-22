"""Instructor-provided example. Students should create their own files."""
TOOL_NAME = 'Even or Odd'


def run():
    print('\n Enter a number to see if its even or odd')
    try:
        number = float(input('First number: '))
    except ValueError:
        print('Please enter valid numbers.')
        return
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
