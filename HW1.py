# HW1.py
# Author:Jonathan Welch 

# Question 1:
# Print Hello World like we did in class
print("Hello World")
# Question 2:
# Print the following:
# Your name
print("Jonathan Welch")
# Your age
print("26")
# Your favorite color
print("red")
# Your favorite animal
print("lion")
# Question 3:
# Create a variable called "myName" and set it equal to your name
myname="Jonathan Welch"
# Create a variable called "myAge" and set it equal to your age
myage="26"  
# Create a variable called "myColor" and set it equal to your favorite color
mycolor="red"   
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal="lion" 
# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>
print("Hello, my name is",myname)
print("I am",myage,"years old") 
print("My favorite color is",mycolor)   
print("My favorite animal is",myAnimal)

# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2+2)
# 3 * 4
print(3*4)
# 5 - 6
print(5-6)
# 8 / 2
print(8/2)
# Question 5:
# Create a variable called "num1" and set it equal to 2
num1=2  
# Create a variable called "num2" and set it equal to 3
num2=3  
# Create a variable called "num3" and set it equal to 4
num3=4
# Create a variable called "num4" and set it equal to 5
num4=5  
# Calculate the following and print the result:
# num1 + num2
print(num1+num2)
# num3 * num4
print(num3*num4)
# num4 - num1
print(num4-num1)
# num2 / num1
print(num2/num1)
# Question 6: Write a program that asks the user for their name and then prints the following:

# Hello, <name>. Please enter three numbers.
name= input("Enter your name: ")
print(name)
# The program should then ask the user for three numbers (floats) and print the following:


# 1. The sum of the three numbers is <sum>
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
num3= float(input("Enter third number: "))  
print(num1+num2+num3)
# 2. The product of the three numbers is <product>
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
num3= float(input("Enter third number: "))
print(num1*num2*num3)
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 
round((num1+num2+num3)/3)
print(round((num1+num2+num3)/3))
# 4. The average of the three numbers is <average>
average=(num1+num2+num3)/3
print(float(average))

# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
print("    *     |")
print("   ***    |")    
print("  *****   |")
print(" *******  |")
print("  *****   |")
print("   ***    |")
print("    *     |")
#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
