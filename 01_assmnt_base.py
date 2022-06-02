import random

# welcome to this math quiz
print("""
    Hello and welcome to the best math quiz around!

    Good luck and have fun!
""")


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
    print()
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return "" 

if played_before == "yes": 
    instructions()


choose_instruction = ("press <1> for easy, <2> for medium, <3> for hard")
easy_mode = 0
medium_mode = 0
hard_mode = 0

# ask user for # of rounds, <enter> for infinite mode 

print()
print("what difficulty do you want to play on?")
print()

choose = input("{} or 'xxx' to end: ".format(choose_instruction))

print()
print("you chose {}".format(choose))
print()

if choose == "1":
    print("you are now playing on easy difficulty")

if choose == "2":
    print("you are now playing on medium difficulty")

elif choose == "3":
    print("you are now playing on hard difficulty")











