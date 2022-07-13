import random
"""this allows code with the 'random.randint' to randomise"""

# welcome to this math quiz
print("""
    Hello and welcome to the best math quiz around!

    Good luck and have fun!
""")

ask_name = input("what is your name/nickname?")

print("\nHi {}, good luck!".format(ask_name))

# functions go here

# Number checking function goes here
user_choice = ""
game_summary = []


# number checking function
# checks that the user has answered the question with an integer,
# if not answered with an integer print "please try again"
def intcheck(question, low=None, high=None, exit_code=None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


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

        You will choose how many questions you want to be asked, when you have answered them all

        it will show what you got wrong and what you got right.

        It will also show what you got right and wrong in percentages(%)

        Good Luck.

        """)
    return ""


if played_before == "yes":
    instructions()

# main routine goes here
end = False

questions_asked = 0

correct_questions = 0

incorrect_questions= 0

choose_instruction = ""

# allows user to input how many questions they want to be asked
questions_wanted = intcheck("How many questions:", 1)

end_quiz = "no"

while questions_asked < questions_wanted:

    # randomises 2 numbers and gives user a '+' or '-' question
    if questions_asked <= 10 | questions_asked >=10:
        choice = random.choice("+-")
        num_1 = random.randint(10, 20)
        num_2 = random.randint(1, 10)
        print(num_1, choice, num_2)
        answer = intcheck("answer the question:")

    # random '+' choice for the question, gives user '+' question and prints 'correct' if right, prints 'wrong answer' if incorrect
    if choice == "+":
        real_answer = num_1 + num_2
        if answer == real_answer:
            print()
            feedback = print(":) correct :)")
            print()
            correct_questions += 1

        else:
            print()
            feedback = print(":( incorrect, the real answer was:", real_answer, ":(")
            print()
            incorrect_questions += 1

        questions_asked += 1

    # random '-' choice for the question, gives user '-' question and prints 'correct' if right, prints 'wrong answer' if incorrect
    elif choice == "-":
        real_answer = num_1 - num_2
        if answer == real_answer:
            print()
            feedback = print(":) correct :)")
            print()
            correct_questions += 1

        else:
            print()
            feedback = print(":( incorrect, the real answer was:", real_answer, ":(")
            print()
            incorrect_questions += 1

        questions_asked += 1

# shows user what question it was that they answered
# then puts it in a list
    outcome = "Question {}: {}".format(questions_asked, feedback)
    game_summary.append(outcome)

questions_won = questions_asked - incorrect_questions

# **** Calculate Game Stats ******
percent_win = correct_questions / questions_asked * 100
percent_lose = incorrect_questions / questions_asked * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()
# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%)".format(correct_questions, percent_win, incorrect_questions, percent_lose))

print()
print("Thanks for playing", ask_name, "!")
