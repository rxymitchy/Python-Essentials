#lists part 2
#2D lists- each item in the list is another list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Item in the first row, second column is:")
matrix[0][1] = 20#changes from 2 to 20
print(matrix[0][1])

matrix[0][1] = 20#changes from 2 to 20
print(matrix[0][1])


for row in matrix:
    for item in row:
        print(item)

#Unpacking

coordinates = (1, 2, 3)
x, y, z = coordinates #assigns items to tuple according to place values
print("Unpacking items as follows: x, y, z")
print(x)
print(y)
print(z)

#Dictionaries = maps a key to a value
customer = {
    "name": "John Smith",
    "age": 30,
    "its_verified": True
}
print("Dictionaries are used in this section:")
print(customer["name"])
print(customer["age"])
print(customer.get("birthdate", "Jan 1 1960"))
customer["name"] = "Jack Smith"
print(customer["name"])

#phone number example
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"

}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#emojis
message = input(">")
words = message.split(' ')
emojis = { }

print(words)

#Functions & parameters & keyword arguments
def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
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

