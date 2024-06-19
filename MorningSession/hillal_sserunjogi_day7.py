# Inheritance and polymorphism
"""_Sumarry_
Inheritance and method overriding
Polymorphism and method resolution order
Abstract classes and interfaces
"""

# Inheritance and method overriding
"""
Inheritance and method overriding allowsa class (child class) to inherit attributes and methods from another class (parent 
class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class .
Derived class (child class): Class that inherits attributes and properties from another base class.
"""

# Example 1 : Syntax create a class where a dog inherits from Animal and overides with a speak method
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
# Implementation of inherited classes
animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())


# Polymorphism
"""
Polymorphism allows abjects of different classes to be treated as objects of a common superclass. 
Method resolution order (MRO) is the order in which python searches for methods in a hierarchy of classes.
"""
# Example 2: How polymorphism works in python
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())
make_animal_speak(Cat())

# Exercise 1: Create a simple application to manage different types of vehicles. Implement derived class
# to demonstrate polymorphism.
"""
Requirements:
1.Base class (Vehicle) 
Attributes: make, model, year
Methods: display_info()

2.Derived classes:
Car: inherit from vehicle
Attributes : number_of_doors
Overrides : display_info()

Motorcycle: inherit from vehicle
Attributes : type_of_bike (cruiser,sport,touring)
Overrides : display_info()
"""

# Exercise 2:
# Create  a function that accepts a list of vehicle objects and call their display_info() method
# to print details of each vehicle.

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        return f"{self.make} {self.model} {self.year}"
    
class Car(Vehicle):
    def __init__(self,make,model,year,number_of_doors):
        super().__init__(make,model,year)
        self.number_of_doors = number_of_doors
        
    def display_info(self):
        return f"{self.make} {self.model} {self.year} {self.number_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self,make,model,year,type_of_bike):
        super().__init__(make,model,year)
        self.type_of_bike = type_of_bike
        
    def display_info(self):
        return f"{self.make} {self.model} {self.year} {self.type_of_bike}"

def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())

vehicles = [Car("Toyota","Corolla",2019,4),Motorcycle("Honda","CBR",2020,"Sport")]
display_vehicle_info(vehicles)



"""
Working with text files
Handling CSV files
JSON and XML file processing
"""

# Working with text files,open,read,write,close
# NOTE: Python provides inbuilt functions to handle text files.
"""
Key concepts
Opening a file: open() function with file mode (r,w,a,r+)
Reading a file: read() function
Writing to a file: write() function
Closing a file: close() function

"""

# Example 3: Write a file and read a file

# Writing to a text file
with open("sample.txt","w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This is a second line in the file.\n")

# reading from a text file
with open("sample.txt","r") as file:
    content = file.read()
    print(content)


# Handling CSV files
"""
CSV (Comma Separated Values) file widely for data exchange. 
Key Concepts
Reading a CSV file: csv.reader() function
Writing to a CSV file: csv.writer() function
DictReader and DictWriter : These classes allow you to read and write CSV files using dictionaries.
"""

# Example 4: Reading and writing CSV files
import csv
# Writing to a CSV file
with open("sample.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Alice",25,"New York"])
    writer.writerow(["Bob",30,"San Francisco"])

# Reading from a CSV file
with open("sample.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# JSON and XML file processing
"""
JSON (JavaScript Object Notation) and XML (Extensible Markup Language) are popular formats used to structure data.
Key concepts
Loading JSON data: json.load() function for reading JSON file
Dumping JSON data: json.dump() function for writing JSON file
Parsing JSON data: json.loads() function for handling JSON string
"""

# Example 5: Reading and writing JSON files
import json

# Writing to a JSON file
student_data = {
    'name':'Hillal',
    'course':'BSE',
    'year':'Year 2'
}

# Open the file in write mode
with open("student.json","w") as file:
    json.dump(student_data,file)

# Reading from a JSON file
with open("student.json","r") as file:
    data = json.load(file)
    print(data)



# Exercise 2: Write and read xml file
import xml.etree.ElementTree as ET

# Writing an XML file
def write_xml(file_name):
    # Create the root element
    root = ET.Element("root")

    # Create a child element
    child = ET.SubElement(root, "child")
    child.text = "Hello, Iam Nakanwagi Vanesa"

    # Create a tree and write the XML file
    tree = ET.ElementTree(root)
    tree.write(file_name)

# Reading an XML file
def read_xml(file_name):
    # Parse the XML file
    tree = ET.parse(file_name)

    # Get the root element
    root = tree.getroot()

    # Access the child element's text
    print(root.find("child").text)

# Example usage
file_name = "example.xml"
write_xml(file_name)
read_xml(file_name)


# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle
from abc import ABC 
class Shape(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)

rectangle = Rectangle(10,5)
print(f"The area of the rectangle is : {rectangle.area()}")
print(f" The perimiter of the rectangle is : {rectangle.perimeter()}")
