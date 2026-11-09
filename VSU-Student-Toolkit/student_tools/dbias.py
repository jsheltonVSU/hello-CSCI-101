"""Instructor-provided example. Students should create their own files."""
TOOL_NAME = 'High or low'


def run():
    print('Check if number is greater than 50')
    try:
        num = float(input('Enter number: '))
    except ValueError:
        print('Please enter valid numbers.')
        return
    if num > 50:
        print(f'> than 50')
    else:
        print(f'< or equal to 50')
