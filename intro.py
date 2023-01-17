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
print(course.find('y'))#index for y in statement
print(course.replace('for', '4'))#replaces for with 4 in the statement
print(course.find('Python'))#index of first letter
print('Python' in course)#uses in operation to find words , returns boolean values
print('This secion is for operators, between 10 and 3')
print(10+3)#addition
print(10-3)#subtration
print(10*3)#multiplication
print(10/3)#division(ingle slash, returns float
print(10//3)#divisio double slash, returrns integer
print(10%3)#modulus, returns remainder
print(10**3) #exponential, power(multiplies 10, 3times)
#augmented assignment operator
print('This secion is for augmented assignment operators, 20 & 3')
x = 20
#x = x + 3
x += 3 #augmented assignment operator
print(x)
x //= 3
print(x)
x %= 3
print(x)
#Operator precedence in python
x= 10 + (3 * 2)
print(x)
x = (10 + 3)* 2
print(x)
#Comparison operator
print('This secion is for comparison operators between 3 and 2')
print('Equal:')
x = 3 ==2
print(x)#returns boolean, either true or false
print('Not Equal:')
x = 3 !=2
print(x)
print('Greater, Equal:')
x = 3 >=2
print(x)
print('Less , Equal:')
x = 3 <=2
print(x)
print('Greater:')
x = 3 >2
print(x)
print('ELess than:')
x = 3 <2
print(x)

#Logical Operators
print('This secion is for logical operators , price is 25 & 5')
price = 25
print('And:')
print(price > 10 and price < 30) #returns true if both are correct
price = 5
print('or:')
print(price > 10 or price < 30) #returns true if at least one is correct
print('And:')
print(price > 10 and price < 30) #returns true if both are correct
price = 5
print('Not:')
print(not price >10) #disagrees with our statement, will return true since we disagree

#If statements
print("If Else Statements")
temperature = float(input("Enter Temperature:"))
if temperature > 30:#executed if true, 
    print("It's a hot day")
    print("Drink plenty pf water")#uses indentstion to show block of code
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("done")#not part of the if else chain
weight=float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " +str(converted))

#while loops
print("This section uses while loops")
i = 1
while i <= 5:
    print(i)
    i = i + 1#ensures program terminsates and doesnt run forever
j = 1
print("Ateriks:")
while j <= 10:
    
    print(j * '*')#in python you can multiply a number with a string, the asteriks give the values of the number
    j = j + 1

#lists
print("This section uses lists")
names = ["John", "Jane", "Mitch", "Jace","Ren"]
print("First name:")
print(names[0])#first element in list
print("Last name:")
print(names[-1])#last element in list
print("Change spelling of John:")
names[0]= "Jon" #changes the spelling of John
print(names[0:3])#python excludes the last index
print(names[2:])#prints from Mitch

#list methods
print("This section uses list methods")
numbers =[1, 2, 3, 4, 5]
print(numbers)
numbers.insert(-1,6)
print("Insert 6:")
print(numbers)
numbers.remove(3)
print("Remove 3:")
print(numbers)
print("Search for 1:")
print(1 in numbers)#returns boolean
print("No of elements in list:")
print(len(numbers))
numbers.clear()
print("Clear numbers:")
print(numbers)

#for loops
print("This section uses for loops:")
numbers =[1, 2, 3, 4, 5]
print("For loops")
for item in numbers:#shorter listing method
    
    print(item)

i = 0

print("While loops")
while i < len(numbers):#longer listing method $ complex
   
    print(numbers[i])
    i = i + 1

#range in for loops
print("this section uses range:")
numbers = range(5, 10)
print(" numbers from 5 to 10")
for number in numbers:
    print(number)
print("Jumps two numbers from 5 to 10")
numbers = range(5, 10, 2)#Jumping 2 umbers
for number in numbers:
    print(number)
print("Dispalys from 0 to 4")
for number in range(5):
    print(number)

#TUPLES, cannot be changed once created
print("This section uses tuples,  cannot be changed once created, parenthesis defines tuples")
this_is_an_example_tuple =(1, 2, 3, 3)#parenthesis defines tuples, brackets define list
this_is_an_example_tuple.count(3)#occurences of 3 in the list
print("occurences of 3:")
print(this_is_an_example_tuple)
this_is_an_example_tuple.index#returns index of first element
print("returns index of first element:")
print(this_is_an_example_tuple)

a = {}#dictionaries
b =()#tuple
c= []#lists

c.insert(0,"mitchele")
print(c)
c.append("Jane")
print(c)
print(c[0])
#control shift home- selects stuff from bottom to top
#control / - comments stuff
#control A - selects stuff from top to bottom
#control D - selects similar words(press D according to the no of words present)