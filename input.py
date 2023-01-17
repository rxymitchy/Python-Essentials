#Receiving input
name = input("What is your name? ")#space enables entering of values
print("Hello " + name)#string combination/ concatenation
age = 20
is_online = True
first_name = "Mitchelle"
print(first_name)
print(age)
print(is_online)
birth_year = input("Enter birth year: ")

age = 2020-int(birth_year)#converts birth year from string to integer to avoid errors
print(age)
first = input("First: ")
second = float(input("Second: "))#both ways of declaration work
sum = float(first )+ (second)
print("Sum: " + str(sum))#converts sum into string so as python can combine
course = 'Python for beginners'
print(course.upper())#creates a new statement does not tamper with course
print(course)
print("Return index of y:")
print(course.find('y'))#index for y in statement
print(course.replace('for', '4'))#replaces for with 4 in the statement
print("Index of the first letter in python:")
print(course.find('Python'))#index of first letter
print("indicates if python is present:")
print('Python' in course)#uses in operation to find words , returns boolean values
#control shift home- selects stuff from bottom to top
#control / - comments stuff
#control A - selects stuff from top to bottom
#control D - selects similar words(press D according to the no of words present)