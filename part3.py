#classes
class Point:
    def ___init___(self, x, y):#constructors are set ie creates an object
        self.x = x#self references itself
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10#assigning values attributes(x, y)
point1.y  = 20#point1 is an object
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

# #Constructors
# print("Using constructors:")
# point3 = Point(15, 25)
# point3.x = 10
# print(point3.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()#john and bob are objects and talk is an attribute

bob = Person("Bob Michael")
bob.talk()

#inheritance
class Mammal:
       def walk(self):
        print("walk")
class Dog(Mammal):
    def ark(self):
        print("bark")
    

class Cat(Mammal):
    def scratch(self):
        print("scratch")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.scratch()

#Modules - importing functions stored in another file
import converters
from converters import lbs_to_kg
print("importinng specific funtio in the module: lbs to kg")
print(lbs_to_kg(500))

print("Importing the whole module: converters Example kg to lbs function is used")
print(converters.kg_to_lbs(70))

from list import find_max
numbers = [3, 6, 2 ,8, 4, 10]
maximum = find_max(numbers)#avoid using ax as it is an inbuilt function
print("The largest number in the list is:")
print(maximum)

#Radom values
import random
for i in range(3):
    print(random.random())
    

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Mitchelle', 'Bob']
leader = random.choice(members)
print(leader)

#DICE
import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return(first, second)


dice = Dice()
print(dice.roll())

from pathlib import Path
#Absolute path - start from root path
#Relative path - start from current
#Linux - forward slash

# path = Path("practice")
# print(path.mkdir())

# path = Path("eccomerce")
# print(path.mkdir())

# path = Path("eccomerce")
# print(path.rmdir())

path = Path()
for file in (path.glob('*.py')):#gets all python files int the curent directory
    print(file)
