# in this we will see how to use inheritance in python.

class car: # car is a parent class
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        print(f"Car Name: {self.name}, Model: {self.model}")

class electric_car(car): # electric_car is a child class that inherits from the car class
    def __init__(self, name, model, battery_capacity):
        super().__init__(name, model)  # Call the constructor of the parent class
        self.battery_capacity = battery_capacity

    def display(self):
        super().display()  # Call the display method of the parent class
        print(f"Battery Capacity: {self.battery_capacity} kWh")
# Create an instance of the electric_car class
my_electric_car = electric_car("Tesla Model 3", "2021", 75)
# Display the details of the electric car
my_electric_car.display()  

