#exceptions (error handling)
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print('Invalid value')

try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
  
except IndexError:
    print("Index Out of Bound.") #since we are trying to access 5

# program to print the reciprocal of even numbers & uses else

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

#Opening a certain file
try:
  f = open("intro.py")
  try:
    f.write("Hi, I finally have access")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()#is executed always in the try block sequence
except:
  print("Something went wrong when opening the file") 

#raising exceptions
y = int(input('Type in y: '))
try:
    if y < 0:
        raise Exception("Sorry, no numbers below zero") 
    elif y == 0:
        print("The number is zero")
    else:
        print("Number is above zero")
except:
    print("Invalid input")


x = int(input('Type in x: '))
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed") 
    else:
        print("Integer received")
except: 
    print("Something else went wrong")


#User defined exceptions
#Example 1
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

#Example 2
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

try:
    salary = int(input("Enter salary amount: "))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)
    else:
        print("Good! You're within range")
except:
    print("Enter different salary amount")

z = "defined"
try:
  print(z)
except NameError:
  print("Variable z  is not defined")
