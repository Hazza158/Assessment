import random

# welcome to this math quiz
print("""
    Hello and welcome to the best math quiz around!

    Good luck and have fun!
""")

ask_name = input("what is your name/nickname?")

print("\nHi {}, good luck!".format(ask_name))

# functions go here

# yes / no checker function
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

game_summary = []
end = False
user_choice = ""
questions_asked = 0
correct_questions = 0
incorrect_questions= 0 

# number checking function
# checks that the user has answered the question with an integer, if not answered with an integer print "please try again"
def getValue():
    userInput = ''
    try:
        userInput = int(input("answer the question:"))
    except ValueError:
        return "retry"
    else:
        return userInput

userEntry = getValue()

while userEntry == 'retry':
    print("you answered with a letter, please try again")
    userEntry = getValue()

while end == False:

    # randomises 2 numbers and gives user a '+' or '-' question
    if questions_asked <= 5:
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
            print("incorrect, the real answer was:", real_answer)
            incorrect_questions =+ 1
        
        questions_asked =+ 1
    
    # random '-' choice for the question, gives user '-' question and prints 'correct' if right, prints 'wrong answer' if incorrect
    elif choice == "-":
        real_answer = num_1 - num_2
        if answer == real_answer:
            print("correct")
            correct_questions =+ 1
        
        else:
            print("incorrect, the real answer was:", real_answer)
            incorrect_questions =+ 1
        
        questions_asked =+ 1
    
    if user_choice == "xxx":
        end = True
        break
     

outcome = "Round {}: {}".format(questions_asked)
game_summary.append(outcome)

rounds_won = questions_asked - incorrect_questions

# **** Calculate Game Stats ******
percent_win = rounds_won / questions_asked * 100
percent_lose = incorrect_questions / questions_asked * 100


print()
print ("***** Game History *****")
for game in game_summary:
    print(game)

print()
# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print ("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%)".format(rounds_won,percent_win,incorrect_questions,percent_lose))

print("Thank you for playing")


