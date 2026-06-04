class Battery:
    def battery_info(self):
        return "This is batrrey"
class Engine:
    def engine_info(self):
        return "This is engine"
class ELectricCar(Battery,Engine):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

#multiple inheritance is possible.
my_tesla = ELectricCar("tesla", "Model S")
print(my_tesla.battery_info())
print(my_tesla.engine_info())

