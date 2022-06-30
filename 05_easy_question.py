import random
import math

ask_name = input("what is your name/nickname?")

print("Hi {}, good luck!".format(ask_name))

end = False
questions_asked = 0
correct_questions = 0
incorrect_questions= 0 
yes_no_list = ["yes", "no"]

while end == False:

    # randomises 2 numbers and gives user a '+' or '-' question
    if questions_asked <= 10:
        user_choice = ""
        choice = random.choice("+-")
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        print(num_1, choice, num_2)
        answer = int(input("answer the question:"))
    
   
    
    # random '+' choice for the question, gives user '+' question and prints 'correct' if right, prints 'wrong answer' if incorrect
    if choice == "+":
        real_answer = num_1 + num_2 
        if answer == real_answer:
            print("correct")
            correct_questions =+ 1
        
        else:
            print("wrong answer, the answer was", real_answer)
            incorrect_questions =+ 1
        
        questions_asked =+ 1
    
    # random '-' choice for the question, gives user '-' question and prints 'correct' if right, prints 'wrong answer' if incorrect
    elif choice == "-":
        real_answer = num_1 - num_2
        if answer == real_answer:
            print("correct")
            correct_questions =+ 1
        
        else:
            print("wrong answer, the answer was", real_answer)
            incorrect_questions =+ 1
        
        questions_asked =+ 1
    
    if answer == "xxx":
        end = True
        break
     
    
print("Hi", ask_name, ",  you got", correct_questions, "out of 10")

   