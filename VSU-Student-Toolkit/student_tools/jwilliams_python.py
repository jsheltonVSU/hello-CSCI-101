"""Instructor-provided example. Students should create their own files."""
TOOL_NAME = 'divide two numbers'


def run():
    print('\n divide Two Numbers')
    try:
        first = float(input('First number: '))
        second = float(input('Second number: '))
    except ZeroDivisionError:
        print('Cannot divide by zero.')
        return
    print(f'Result: {first / second}')
