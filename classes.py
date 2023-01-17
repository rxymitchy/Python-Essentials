#classes
class Point:
    def ___init___(self, x, y):#constructors are set ie creates an object, init enables one to assign values
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






