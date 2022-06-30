import random

correct = 0
incorrect = 0
name = input("Please enter your name: ")
for count in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol = random.choice(["+", "-",])
    print("Please solve:\n", num1, symbol, num2)
    user = int(input(""))

    if symbol == "+":
        answer = num1 + num2
    elif symbol == "-":
        answer = num1 - num2

    if user == answer:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect, the correct answer was", answer)

print(name, ", You Got", correct, "Out Of 10")