# Project1.py
# Author:Jonathan Welch


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game
print("Welcome to the quiz game!")
inputname = input("What is your name? ")
print("Hello " + inputname + "!")
print("Here are the rules of the game:")
print("You will be asked a series of questions and given 4 options to choose from.")
print("Type the letter of the answer you think is correct.")
print("Each question is worth 1 point.")
print("Good luck!")
# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:
print("Question 1: What is the capital of California?")
print("a. Los Angeles")
print("b. San Francisco")
print("c. Sacramento")
print("d. San Diego")
answer1 = input("Answer: ")
if answer1 == "c":
    print("Wrong! just kidding! You got it right!")
    score = 1
else:
    print("Incorrect. The correct answer is c.")
    score = 0

print("Question 2: What is the capital of Texas?")  
print("a. Houston")
print("b. Dallas")
print("c. Austin")
print("d. San Antonio")
answer2 = input("Answer: ")
if answer2 == "c":
    print("Got to be the smartest person ever!")
    score = score + 1
else:
    print("Incorrect. The correct answer is c.")
    score = score + 0
print("Question 3: What is the capital of New York?")
print("a. New York")
print("b. Albany")
print("c. Buffalo")
print("d. Syracuse")
answer3 = input("Answer: ")
if answer3 == "b":
    print("Wow you got the answer right!")
    score = score + 1
else:
    print("Incorrect. The correct answer is b.")
    score = score + 0
print("Question 4: What is the capital of Florida?")
print("a. Miami")
print("b. Orlando")
print("c. Tampa")
print("d. Tallahassee")
answer4 = input("Answer: ")
if answer4 == "d":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The correct answer is d.")
    score = score + 0
print("Question 5: What is the capital of Washington?")
print("a. Seattle")
print("b. Spokane")
print("c. Tacoma")
print("d. Olympia")
answer5 = input("Answer: ")
if answer5 == "d":
    print("Great job!")
    score += 1
    last_question_correct = True
else:
    print("Incorrect. The correct answer is d.")
    last_question_correct = False
# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:
if last_question_correct:
    print("Your score is " + str(score) + " out of 5.")
else:
    print("Your score is " + str(score) + " out of 5. Better luck next time!")
print("Thank you for playing!")



# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct

def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
    print(question)
    print("a. " + option_1)
    print("b. " + option_2)
    print("c. " + option_3)
    print("d. " + option_4)
    answer = input("Answer: ").lower()
    if answer == correct_answer:
        return True
    else:
        return False

question1 = ask_question("What is the best Nintendo game out right now?", "Super Smash Bros. Ultimate", "The Legend of Zelda: Breath of the Wild", "Animal Crossing: New Horizons", "Mario Kart 8 Deluxe", "b")
if question1:
    print("You made the right choice there!")
    score += 1
else:
    print("Incorrect. The correct answer is a.")


# Create a function to display the final score, which takes the score as a parameter and displays a message.
    def display_score(score):
        print("Your score is " + str(score) + " out of 5.")
        print("Thank you for playing!")

# Loops:
# Use a for or while loop to iterate through the questions
while True:
    print("Question 1: What is the capital of California?")
    print("a. Los Angeles")
    print("b. San Francisco")
    print("c. Sacramento")
    print("d. San Diego")
    answer1 = input("Answer: ")
    if answer1 == "c":
        print("Wrong! just kidding! You got it right!")
        score = 1
    else:
        print("Incorrect. The correct answer is c.")
        score = 0
    
    print("Question 2: What is the capital of Texas?")
    print("a. Houston")
    print("b. Dallas")
    print("c. Austin")
    print("d. San Antonio")
    answer2 = input("Answer: ")
    if answer2 == "c":
        print("Got to be the smartest person ever!")
        score = score + 1
    else:
        print("Incorrect. The correct answer is c.")
        score = score + 0
    print("Question 3: What is the capital of New York?")
    print("a. New York")
    print("b. Albany")
    print("c. Buffalo")
    print("d. Syracuse")
    answer3 = input("Answer: ")
    if answer3 == "b":
        print("Wow you got the answer right!")
        score = score + 1
    else:
        print("Incorrect. The correct answer is b.")
        score = score + 0
    print("Question 4: What is the capital of Florida?")
    print("a. Miami")
    print("b. Orlando")
    print("c. Tampa")
    print("d. Tallahassee")
    answer4 = input("Answer: ")
    if answer4 == "d":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect. The correct answer is d.")
        score = score + 0
    print("Question 5: What is the capital of Washington?")
    print("a. Seattle")
    print("b. Spokane")
    print("c. Tacoma")
    print("d. Olympia")
    answer5 = input("Answer: ")
    if answer5 == "d":
        print("Great job!")
        score += 1
        last_question_correct = True
    else:
        print("Incorrect. The correct answer is d.")
        last_question_correct = False
    
    stop = input("Would you like to play again? (y/n) ")
    
    if stop == "n":
        break
        
  
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d)
while True:
    try:
        answer1 = float(input("Answer: "))
        if answer1 == "c":
            print("Wrong! just kidding! You got it right!")
            score = 1
        else:
            print("Incorrect. The correct answer is c.")
            score = 0
    except ValueError: 
        pass

    try:
        answer2 = float(input("Answer: "))
        if answer2 == "c":
            print("Got to be the smartest person ever!")
            score = score + 1
        else:
            print("Incorrect. The correct answer is c.")
            score = score + 0
    except ValueError:
        pass
    
    try:
        answer3 = float(input("Answer: "))   
        if answer3 == "b":
            print("Wow you got the answer right!")
            score = score + 1
        else:    
            print("Incorrect. The correct answer is b.")
            score = score + 0
    except ValueError:
        pass
    
    try:
        answer4 = float(input("Answer: "))
        if answer4 == "d":
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect. The correct answer is d.")
            score = score + 0
    except ValueError:
        pass
        
    try:
        answer5 = float(input("Answer: "))
        if answer5 == "d":
            print("Great job!")
            score += 1
            last_question_correct = True
        else:
            print("Incorrect. The correct answer is d.")
    except ValueError:
        pass    
        
        break