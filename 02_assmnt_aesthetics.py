def statement_generator(statement, decoration):
    sides = decoration * 3 

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""



statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
statement_generator("Congratulations You Got a Unicorn", "!")