game_summary = []

outcome = "Round {}: {}".format(questions_asked, feedback)
game_summary.append(outcome)

rounds_won = questions_asked - incorrect_questions

# **** Calculate Game Stats ******
percent_win = rounds_won / questions_asked * 100
percent_lose = incorrect-questions / questions_asked * 100


print()
print ("***** Game History *****")
for game in game_summary:
    print(game)

print()
# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print ("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%)".format(rounds_won,percent_win,incorrect_questions,percent_lose))

print("Thank you for playing")