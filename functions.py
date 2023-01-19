#Functions & parameters & keyword arguments
def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')#used with dictionaries
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")#positional argument
greet_user(last_name= "Wright", first_name= "Mary") #Keyword arguments
print("Finish")

#Return statement by default all functions in python return none
def square(number):
    return number * number
print("square of 3:")
print(square(3))

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

#Anonymous functions

# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Mitchelle')

#changing  global variable
# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print("Global variable is now: " + str(c))

add()
