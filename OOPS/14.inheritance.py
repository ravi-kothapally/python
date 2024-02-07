
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def display_car(self):
        return "This is a %s %s with %s MPG. " % (self.color, self.model, self.mpg)
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        Car.__init__(self, model, color, mpg)
        self.battery_type = battery_type
    def display_car(self):
        inherit_Str = Car.display_car(self)
        return inherit_Str + "It has a %s battery. " % (self.battery_type)
my_car = ElectricCar("Ford", "black", 95,"molten salt")
print (my_car.display_car())
