import random

number_one = random.randint(1,100)
number_two = random.randint(1,100)


question = "what is {} + {}".format(number_one, number_two)
ask = input(question)
answer = "yes"

if ask == answer:
    print("correct!")
else:
    print("wrong")
    
