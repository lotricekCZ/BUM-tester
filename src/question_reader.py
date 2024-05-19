import random
import re

p = re.compile("(\\d+\\.)(.*)", re.VERBOSE)

questions_file = open("./assets/questions.txt")
questions = questions_file.readlines()
while len(questions) != 0:
    selected = random.randint(0, len(questions) - 1)
    selected_question = questions[selected].split(' ', 1)
    print(selected_question[1])
    a = ''
    while a != 'y' and a != 'n':
        a = input("operation: y/n/w: ")
        if a == 'w':
            print(selected_question[0])
        elif a == 'y':
            del questions[selected]
    