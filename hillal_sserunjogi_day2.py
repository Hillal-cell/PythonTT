age = int(input("Enter your age: "))
price = 2000
if(age <13):
    print( "You're discount is : shs 1000 so you're to pay :"+str(price-1000))
elif(age >=13 and age <= 18):
    print("You're discount is : shs 500 so you're to pay :"+str(price-500))
elif(age > 18 and age <= 90):
    print("You are to pay : shs "+str(price))
else:
    print("You are to pay : shs "+str(price+3000))    



#Exercise 2
my_favourite_colors = []
while len(my_favourite_colors) < 3:
    my_favourite_colors.append(input("Enter your favourite color: ")) 

print("Your list of favourite colors is : ",my_favourite_colors)


numbers = [1,2,3,4,5]
index = len(numbers) - 1
reversed_numbers = []
while index >= 0:
    reversed_numbers.append(numbers[index])
    index -= 1

print(reversed_numbers)



