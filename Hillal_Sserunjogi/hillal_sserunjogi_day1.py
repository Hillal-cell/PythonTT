 #variables 
x = 5
y = 10
print("sum = " , x + y)

#bool(False)
#to enable users input data and print it on the screen 
#the input function helps users to input data to the program
#name = input("enter name ")
#color = input("enter color ")
#print(name , " likes " , color)



#Boolean functions
#these boolean functions return a false because the variables  entered in the bool() function have no  value
print(bool(False))
print(bool({}))
print(bool(0))
print(bool(""))

#these boolean functions return a true because the variables  entered in the bool() function has a value
m = 15
s = "Hello"
print(bool(m))
print(bool(s))


#This function portrays the use of boolean values in functions

def myFunction() :
        return True
if myFunction():
    print(1)

else:
    print(0)

#Strings 
# string declaration (using double quotes and single quotes) && string concation (using a comma , and using a plus sign)
x = "Come early"
y = 'you late '

print("I told you to " , x , "but " , y)

print("I told you to " + x + "but " + y)

# string declaration && string conceration
x = "Come early"
y = 'you late '

print("I told you to " , x , "but " , y)