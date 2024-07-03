# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""Summary
Disctionaries in python are a collection of keys and values.
-They can be unordered
-Are mutable
-indexed by keys
"""

# Example 1: Creating a dictionary
# Creat a dictionary for a student pursuing Software Engneering , key must be your name ,
# age, technology interest,course and year of study
student_dict = {
    "name": "Hillal Sserunjogi",
    "age": 23,
    "Course": "Software Engineering",
    "technology": "Python",
    "year": 3
}

# Accessing the dictionary values
print("Student name : ",student_dict["name"])

# modifying the dictionary
student_dict["age"] = 30
print("Student's new  age : ",student_dict["age"])
student_dict["technology"] = "Java"
print("New technology : ",student_dict["technology"])

#Example2: Adding a new key value pair
student_dict["email"]="hillal@duckgo.com"
print("Student's email : ",student_dict["email"])

# Exercise 2 : Remove a key value pair from the dictionary
print("")
print("Removing a key value pair from the dictionary")

# by the pop method
student_dict.pop("year")
print("Student's dictionary without a  year : ",student_dict)
# also can use the del key word

del student_dict["age"]
print(student_dict)

# Using the update and get methods
print(student_dict.get("name"))
student_dict.update({"age":67})
print(student_dict["age"])

# Exercise : Check if the age exists and if it does then return the value of the age
if 'age' in student_dict:
     print(student_dict.get('age'))
else :
    print("Does not exist.")

# Keys , values and items methods
print(student_dict.keys()) #returns a view of objects that displays a list of all the keys
print(student_dict.values()) #returns a view of objects that displays a list of all the values
print(student_dict.items()) #returns a view of objects that displays a list of all the key value turple pairs

# Exercise : Use the update method to change the course and add a new key "WhatsApp" number to the dictionary
student_dict.update({"Course":"Computer Science","WhatsApp": "0783649274"})
print("Student's  number : ",student_dict["WhatsApp"])