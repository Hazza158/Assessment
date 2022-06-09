from random import choice
def easy():
   CorrectQuestions = 0
   IncorrectQuestions = 0
   #I want 3 easy questions
   easyQuestions = {'Question':'answer','Question':'answer','Question':'answer','Question':'answer'}
   Q1 = choice(easyQuestions)
   Q2 = choice(easyQuestions)
   Q3 = choice(easyQuestions)
   print("Question 1:\n")
   answer = input(Q1)
   if answer == easyQuestions[Q1]:
      print("Correct")
      CorrectAnswers += 1
   else:
      print("Incorrect")
      IncorrectAnswers +=1
   print("Question 2:\n")
   answer2 = input(Q2)
   if answer2 == easyQuestions[Q2]:
      print("Correct")
      CorrectAnswers += 1
   else:
      print("Incorrect")
      IncorrectAnswers += 1
   print("Question 3:\n")
   answer3 = input(Q3)
   if answer3 == easyQuestions[Q3]:
      print("Correct")
      CorrectAnswers += 1
   else:
      print("Incorrect")
      IncorrectAnswers += 1
   results = f="You got {str(CorrectAnswers)} answers correct and {str(IncorrectAnswers)} answers wrong."
def medium():
   #code
    def hard():
   #code
        diff = {'easy':easy,'medium':medium,'hard':hard}
        Difficulty = input("Enter Difficulty:")
        for i in diff:
            if Difficulty == diff[i]:
                diff[i]()
                else:
                continue