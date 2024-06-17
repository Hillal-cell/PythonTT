# Defining Functions

# Function syntax and parameters
# Return values
# Lambda functions



# Functions in Python are defined using the 'def' keyword follwed by the functin name 
# then the paranthesis () , inside the paranthesis we can pass parameters to the function and then a colon

# Example 1:
def multiply(x, y):
    return x * y

# Example 2:
def get_cordinates():
    return 12,6

x,y =get_cordinates()
print(x,y)

# Exercise 1 : Define a function with a parameter name,set to Guest and print a message 
# iam a software programmer
def programmer(name ="Guest"):
    print(f"I am a software programmer and I am ",name )

programmer("Hillal")

# Retruning multiple values from a function
def get_name_and_position():
    name ="Hillal"
    position ="Software Engineer"
    return name,position

name,position = get_name_and_position()
print(name,position)

# Exercise 2: Return multiple values of your name and age
def get_name_and_age():
    name ="Hillal"
    age = 23
    return name,age

name,age = get_name_and_age()
print(name,age)


# Notes
"""
def : Is basically a key word to define a function
function_name : This is the name of the function
parameters : These are the values passed to the function  and they are optional
Docstrings : Optional documentation string that describes what the function does
return : Optional returns a value from a function
"""


# Lambda functions
# Lambda functions are small anonymous functions that are defined using the lambda keyword
# Lambda functions can have any number of arguments but only one expression
# Lambda functions can be used to return functions

# Example 1: Syntax of a lambda function
# lambda parameter : expression

f = lambda x: x + 10
print(f(5))


# Example 2: Lambda function with multiple arguments
f = lambda x, y :  x + y
print(f(5, 6))


# Example 6 : Use cases of lambda functions for sorting
coordinates = [(1,2),(2,3),(3,1),(5,0)]
coordinates.sort(key=lambda x: x[1])
print(coordinates)

# Map,Filter and Reduce
# Example 7: Get the squares of 1 to 5 using map,filter and reduce
number_squares = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2,number_squares))
print(squared_numbers)

# Exercise 4: Define a function to get user info that accepts arbitrary keyword arguments and prints
# each key value pair
def get_user_info(**gh):
    for key,value in gh.items():
        print(f"{key} : {value}")

get_user_info(name="Hillal",age=23,position="Software Engineer")


# def get_info(**jkk):
#     print(jkk.items())    
    
# get_info(name="Hillal",age=23,position="Software Engineer")

