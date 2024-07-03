# Custom Exception Handling
# example2:
class FundsInsufficient(Exception):
    def __init__(self,amount,balance):
        self.amount = amount
        self.balance = balance
        self.message =(f"attempt to withdraw {self.amount} with account balance {self.balance}")





# Note : Defining a custom exception you just need to define the class then the custom error
"""
class CustomError(Exception):
    # Custom Exception for specific error cacses

def __init__(self,message):
    super().__init__(message)
    self.message=message

# Raising the custom exceptio
def check_value(value):
    if value is <0 or value:
        raise CustomError("Value can not be negative.")
    return value

    

# Handle 
"""


# Excercise 2:  create a custom exception InvalidAgeError and write a function that raises
# this exception if the given age is negative . Handle this custom exception when calling the function.

class InvalidAgeError(Exception):
    def __init__(self,message):
        self.message=message
        # self.age = age
        super().__init__(message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(f"Age can not be negative {age}")
    return age

try:
    age = check_age(-10)
    print(f"Hai your age is :{age}")
except InvalidAgeError as e:
    print(e.message)
finally:
    print("Age check completed.")


# Soil Prediction that triggers irrigation, Using AI in Django Web Based application!!