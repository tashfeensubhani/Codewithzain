##### Operators

###types:

#1. Arithmetic operators:
# + adds two numbers
# - substracts 2 number
# * multipies two numbers
# / divides two numbers and give answer in float
# // divides two nmber and give answer in integer
# ** it is used to calculate power of any number
# % it gives the remainder

a = 12
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)

#2. Comparison operators:
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b) # checks whether they both are equal
print(a != b) # checks whether they both are not equal
print(a >= b)
print(a <= b)

# 3. Assignment operator:
# It assigns the value on right to any thing or variable present on left(=)
number = 10

#4. Logical Operators:
# Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

# The precedence of Logical Operators in Python is as follows:

# Logical not
# logical and
# logical or
print("Logical operators")
print()
a = True
b = False
print(a and b)
print(a or b)
print(not a)