# python best practises
# 1. use snake_case for variable names
# 2. use camelCase for function names
# 3. use PascalCase for class names
# 4. use 4 spaces for indentation
# 5. use single quotes for strings
# 6. use docstrings for functions and classes
# 7. use comments to explain code
# 8. use meaningful variable names
# 9. use meaningful function names
# 10. use meaningful class names
# 11.Maxmimum of 79 characters per line

# Python operators
"""
Addition: +
Subtraction: -
Multiplication: *
Division: /
Modulus: %
Exponentiation: **
Floor division: //
"""

"""
Comparison operators
Equal: ==
Not equal: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=
"""

# Logical operators
"""
Name of operator  |  Syntax  
and                 and 
or                  or 
not                 not 
NB: These dont have symbols 
"""

# Membership operators
"""
Name of operator  |  Syntax
in                 x in y
not in             x not in y
"""

# Bitwise operators
"""
Name of operator  |  Syntax
AND                &
OR                 |
XOR                ^
NOT                ~
Left shift         <<
Right shift        >>


# Python cases
1. snake_case
2. camelCase
3. PascalCase
4. kebab-case
5. UPPERCASE
"""

# Comprehensions (list, dictionary)
"""
Comprehensions provide a concise way to create lists and dictionaries.
Symbols used:
lists      [] square brackets //used to store multiple items in a single variable
dictionaries {} curly brackets //used to store key value pairs
"""

# Example 1 : List comprehension
#  creating a list of squares in range of 10
squares = [i**2 for i in range(10)]
# print(squares)

# Exercise 1 : Create a list of even-squares  in range of 20
even_numbers = [i**2 for i in range(20)  if  i % 2 == 0]
# print(even_numbers)

# Example 2 : Dictionary comprehension
# Create a ditctionary comprehension for favourite cars and count the lengths of characters
favourite_cars = ['Toyota', 'Benz', 'BMW', 'Subaru']
car_lengths = {car: len(car) for car in favourite_cars}
# print(car_lengths)


#  Exercise 2 : Create a list of tuple where each tuple contains a number and its cube for numbers
#  between 1 and 10 using a dictionary comprehension

numbers = {i: i**3 for i in range(1, 11)}
result = [(key, value) for key, value in numbers.items()]
print(result)
