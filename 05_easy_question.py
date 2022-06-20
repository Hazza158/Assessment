import random
import math


end = False
questions_asked = 0
correct_questions = 0
incorrect_questions= 0 

while end == False:
    if questions_asked <= 10 | questions_asked >= 10:
        choice = random.choice("+-")
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        print(num_1, choice, num_2)
        answer = int(input("answer the question"))
    
    if choice == "+":
        real_answer = num_1 + num_2 
        if answer == real_answer:
            print("correct")
        correct_questions =+ 1 

    elif choice == "-":
        real_answer = num_1 - num_2



   