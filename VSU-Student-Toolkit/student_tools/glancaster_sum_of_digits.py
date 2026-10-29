"""Instructor-provided example. Students should create their own files."""
TOOL_NAME = "sum of digits calculator"

def run():
    number = int(input("Enter a number: "))
    digit = 0 
    sum = 0
    for counter in range (len(str(number))):
        digit = number % 10
        sum = sum + digit
        number = number // 10

    print(f"The sum of the digits is: {sum}")