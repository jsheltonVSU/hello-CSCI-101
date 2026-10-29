Tool_NAME = "SAT Score Motivation Checker"

def run():
    print("Welcome to the SAT Score Checker!")

    score = int(input("Enter your SAT score: "))

    if score < 400 or score > 1600:
        print("Please enter a valid SAT score.")
    elif score >= 1400:
        print("Amazing job! You should be proud!")
    elif score >= 1200:
        print("Good job! Keep up the great work!")
    elif score >= 1000:
        print("Nice effort! Keep studying and improving!")
    else:
        print("Don't give up! Keep practicing. You got this!")
     