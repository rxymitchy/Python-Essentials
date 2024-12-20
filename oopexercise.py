class Person:
    def __init__(self, name, gender, country):
        self.name = name
        self.gender = gender
        self.country = country
    
    #methods
    def display(self):
        return f"Name: {self.name}, Gender: {self.gender}, Country: {self.country}"
    
    def message(self):
        return f"Hello {self.name} Welcome to the Program"
    


person1 = Person("Jude", "Male", "Ugandan")
person2 = Person("April", "Female", "Kenyan")
print(person1.display())
print(person2.display())
print(person1.message())
print(person2.message())
#child class (inheritance)
class CourseTaken(Person):
    def __init__(self, name, gender, country, course):
        super().__init__(name, gender, country) #intialize parent class attributes
        self.course = course

    #polymorphism(message overidden)
    def display(self):
        return f"{super().display()}, Course: {self.course}"
    def message(self):
        return f"{self.name},You are now familiar with the program" 

course1 = CourseTaken("Jude", "Male", "Ugandan", "Web Development")
course2 = CourseTaken("April", "Female", "Kenyan", "Mobile App Development")
print(course1.display())
print(course2.display())
print(course1.message())
print(course2.message())