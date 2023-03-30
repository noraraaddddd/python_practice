
#We define a tuple of questions
questions = ("What are the longest living cells in the human body?",
             "What percentage of the human body is made up of water?",
             "In an average lifetime, how many times does the skin replace itself?",
             "How many galaxies is the known universe made up of?",
             "How many more chromosones do potatoes have than humans?")
#A 2D tuple of answers for each question
options = (("A. Bone cells", "B. Stem cells", "C. Platelets", "D. Brain cells" ),
           ("A. 50%", "B. 60%", "C. 70%", "D. 80%"),
           ("A. 100 times ", "B. 95 times ", "C. 300 times ", "D. 900 times"),
           ("A. 300 million ", "B. 50 billion ", "C. 400 billion ", "D. 350 million "),
           ("A. One ", "B. Two ", "C. Three ", "D. Four "))

#We define a tuple of the correct answers
answers = ("D", "B", "D", "B", "B")
#We define an empty list for the guesses and store the user's input as we move forward
guesses = []
#Set the score to zero and add to it each time that a question gets answered correctly
score = 0
#Set the question number to zero and add to it each timer we loop over the questions
question_num = 0


for question in questions:
    print("----------------")
    print(question)
    
    for option in options[question_num]:
     print(option)
     
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
     score += 1
     print("CORRECT")
    else:
      print("INCORRECT")
      print(f"The correct answer is {answers[question_num]}")

    question_num += 1


print("----------------")
print("     RESULTS    ")
print("----------------")

print("Answers: ", end = " ")
for answer in answers:
  print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
  print(guess, end = " ")
print()

score = int(score/len(questions)*100)
print(f"Your score is %{score}")