# HW3.py
# Author:jonathan welch 

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
input("Question 1: ")
def square(num):
    return num ** 2
print(square(3))
# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
input("Question 2: ")
def replace(string, letter, number):
    return string[:number] + letter + string[number + 1:]
print(replace("Hello World", "a", 3))

# Question 3:
# Write a function that takes in a number, a lower bound, and an upper bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
input("Question 3: ")
def bounds(num, lower, upper):
    return lower <= num <= upper
print(bounds(5, 1, 10))

# Question 4:
# Write a function that asks the user for their name, age, and favorite color. Then write a function that accepts those three parameters and prints them out in a sentence
# IE. If the user inputs "John", 20, and "blue", the function should print "Hello, my name is John. I am 20 years old. My favorite color is blue."
# Hints: You will need to use the input() function to get the user's input. You will also need to use the str() function to convert the age to a string
# This is a two part question. You will need to write two functions
# remember in class we learned you can return miltiple values from a function
# also remember in class you can pass in pultiple variables into a function
input("Question 4: ")
def get_info():
    name = input("What is your name? ")
    age = input("What is your age? ")
    color = input("What is your favorite color? ")
    return name, age, color
def print_info(name, age, color):
    print("Hello, my name is " + name + ". I am " + age + " years old. My favorite color is " + color + ".")
name, age, color = get_info()
print_info(name, age, color)

# Question 5:
# import the random module and use it to generate a random number between 1 and 100
import random
input("Question 5: ")
print(random.randint(1, 100))

# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math
input("Question 6: ")
print(math.sqrt(16))
# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as s
input("Question 7: ")
print(s.version)

# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
import os
input("Question 8: ")
print(os.getcwd())
