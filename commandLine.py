
def getValue():
    userInput = ''
    try:
        userInput = int(input("Please enter a number:"))
    except ValueError:
        return "retry"
    else:
        return userInput

userEntry = getValue()

while userEntry == 'retry':
    print("You entered a non-numeric number. Please try again.")
    userEntry = getValue()

print("You entered:",userEntry)


