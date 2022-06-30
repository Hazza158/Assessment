import random

# welcome to this math quiz
print("""
    Hello and welcome to the best math quiz around!

    Good luck and have fun!
""")

ask_name = input("what is your name/nickname?")

print("\nHi {}, good luck!".format(ask_name))

# functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        
        if response == "yes" or response == "y":
            response = "yes"
            return response
            
        
        elif response == "no" or response == "n":
            response = "no"
            return response
        
        else:
            print("please answer yes / no")

# ask user if they want to see instructions or just play the game
played_before = yes_no("Do you want to see the instructions")

def instructions():
    print("""
        
        ***How To Play The Game***

        choose what difficulty you want to play on (easy, medium, hard)
        
        """)
    return "" 

if played_before == "yes": 
    instructions()


choose_instruction = ("press <1> for easy, <2> for medium, <3> for hard")


# ask user what difficulty they want to play on, then let them choose 

print()
print("what difficulty do you want to play on?")
print()

choose = input("{} or 'xxx' to end: ".format(choose_instruction))

# tells user what difficulty they chose and are playing on 
print()
print("you chose {}".format(choose))
print()

if choose == "1":
    print("you are now playing on easy difficulty")

elif choose == "2":
    print("you are now playing on medium difficulty")

elif choose == "3":
    print("you are now playing on hard difficulty")


end = False
questions_asked = 0
correct_questions = 0
incorrect_questions= 0 

while end == False:

    # randomises 2 numbers and gives user a '+' or '-' question
    if questions_asked <= 5:
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
    
    if user_choice == "xxx":
        end = True
        break
     

print("Hi", ask_name, ",  you got", correct_questions, "out of 5")
