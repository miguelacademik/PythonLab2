#! /usr/bin/env python3
import math

# Part 1: Variables and Assignments.
# 1.1.1 Create variables:----------------------------------------------------------

name = "Miguel"
age = 35
height = 5.9
favorite_color = "Grey"

# 1.2.0 Printing Techniques for variable values:------------------------------------

#1.2.1 Print one variable at a time:
#Print the value of each variable individually using separate print statements.

print(name)
print(age)
print(height)
print(favorite_color)

#1.2.2 Print with one print statement and commas:
#Print the values of all variables in a single print statement, separating them with commas.

print(name, age, height, favorite_color)

#Does it add a space between the variables?

# Yes, it printed everything in a single line and it added spaces.

#1.2.3 Print with Python formats or format specifiers:
#Use Python's string formatting capabilities to print the variables in a more structured way.
#Here's an example with only 2 of your variables.

print(f"Hello: {name}, my age is {age}, my height is {height}, and my favorite color is {favorite_color}!")

print(f"Hello: {name}, my age is {age:03d}, my height is {height:.2f}, and my favorite color is {favorite_color}!")

print("Hello: {}, my age is {:03d}, my height is {:.2f}, and my favorite color is {}!"
      .format(name, age, height, favorite_color)) # I asked a chatbot to show me a different way to do thi, and it suggested to use the str.format()

print(
    f"Hello: {name:^15}, " #^= Aligned to the center, and with width 15 spaces
    f"Age: {age:03d}, " # 3 digits
    f"Height: {height:6.2f}, " # width 6 spaces, and 2 decimals
    f"Color: {favorite_color:>10}" #Right aligned, and width 10 spaces
)

#1.2.4 Print with format specifiers within a multi-line string:
# A multi-line string is a string that spans multiple lines. It is defined using triple quotes (""").
# Use format specifiers within a multi-line string to create a formatted output.
# Here's an example with 2 of the variables you previously defined, you need to include them all:

print(f"""
Name: {name}
Age: {age}
Height: {height}
Color: {favorite_color}
""")

# Test what happens if you add extra spaces at the beginning of the lines of multi-line strings?
# Answer: Python keeps all the spaces, and it looks like is indented once printed.
print(f"""
    Name: {name}
    Age: {age}
    Height: {height}
    Color: {favorite_color}
""")

#1.3 Create a new variable:------------------------------------------------------------

#Similar to last week, calculate the area of a circle with a radius of 5, but this time store the result in a variable named circle_area.
r = int(input("Enter circle radius: " ))
circle_area = math.pi * math.pow(r,2)
print(f"Circle area with radius {r} is: {circle_area:.1f}")


#Part 2: Statements and Modules ---------------------------------------------------------
# 2.1 Import the math module:

#Use the import statement to import the math module.
# Note! Already done on the previous steps.

# 2.2 Calculate the square root:
#Use the sqrt function from the math module to calculate the square root of age.
#Print the result.

print(f"Square Root of my Age is: {math.sqrt(age)}")

# 2.3 Calculate the sine and cosine:
#Use the sin and cos functions from the math module to calculate the sine and cosine of height.
#Print the results.

print(f"sin of my height: {math.sin(height)}, and cos of my height: {math.cos(height)}")

# Part 3: Expressions and Operators --------------------------------------------------------
#Arithmetic operations:

#Use arithmetic operators (+, -, *, /, //, %, **) to perform calculations.
#Calculate the following:
#Print the results:
#Use print to display the results of each calculation.
#Choose your preferred print formatting from the previous exercise.

# 3.1 The sum of age and 5.
print(f"The sum of age and 5 is: {age + 5}")

# 3.2 The difference between height and 4.
print(f"The difference between my height and 4 is:{height - 4:.2} " ) # I decided to round the result too :)

# 3.3 The product of age and height.
print(f"The product of my age by my height is: {age * height}")

# 3.4 The quotient of height and 2.
print(f"The quotient of my height and 2 is: {height / 2}")

# 3.5 The remainder of age divided by 3.
print(f"The remainder of my age divided by 3 is: {age % 3}")

# 3.6 age raised to the power of 2.
print(f"My age raised to the power of 2 is: {age ** 2}")

# Part 4: Temperature Conversion.---------------------------------------------
#Create a temperature conversion program:

#Write a program that converts Fahrenheit to Celsius.
#Prompt the user to enter a temperature in Fahrenheit.
#HINT: the input function will be necessary, and it takes the prompt string as the first argument.
#Convert the temperature to Celsius using the formula: Celsius = (Fahrenheit - 32) * 5/9.
#Print the converted temperature and see if you can print the degree symbol.

temp_fahrenheit = float(input(f"{name} enter a temperature in Fahrenheit: "))
celsius = (temp_fahrenheit - 32) * 5 / 9
print(f"Temperature Fahrenheit {temp_fahrenheit}°F in Celsius is: {celsius}°C")
