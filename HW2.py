# HW2.py
# Author:Jonathan Welch 


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."
inputAge = int(input("Enter your age: "))
if inputAge < 13:
    print("You are a child.")
elif inputAge >= 13 and inputAge <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
whileLoop = 1
while whileLoop <= 5:
    print(whileLoop)
    whileLoop += 1

# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.
whileLoop = 1
while whileLoop <= 5:
    print()
    whileLoop += 1
    forLoop = 1
    for forLoop in range(1, whileLoop):
        print(forLoop, end="")
        breakpoint
    print(whileLoop)
    whileLoop += 1
# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

