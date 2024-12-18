# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def display_info(self):
        return f"Smartphone Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours"

    def charge(self):
        self.battery_life = 100  # Assume 100% battery after charging
        return "Phone is fully charged!"

# Child class: SmartphoneWithCamera (Inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_quality):
        super().__init__(brand, model, battery_life)  # Initialize parent class attributes
        self.camera_quality = camera_quality

    # Polymorphism: Override the display_info method
    def display_info(self):
        return f"{super().display_info()}, Camera Quality: {self.camera_quality} MP"

    # Additional method specific to this child class
    def take_picture(self):
        return "Taking a picture!"

# Example usage
smartphone = Smartphone("Apple", "iPhone 13", 18)
smartphone_with_camera = SmartphoneWithCamera("Samsung", "Galaxy S22", 20, 108)

# Display info for both objects
print(smartphone.display_info())
print(smartphone.charge())
print(smartphone_with_camera.display_info())
print(smartphone_with_camera.take_picture())

#POLYMORHISM
# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # To be overridden by child classes

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "The car is driving 🚗"

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "The plane is flying ✈️"

vehicles = [Car(), Plane()]
for vehicle in vehicles:
    print(vehicle.move())