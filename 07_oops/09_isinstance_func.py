class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
class ElectricCar(Car):
    def __init__(self,brand,model,):
        super().__init__(brand,model)

my_tesla = ElectricCar("tesla","Model S")
print(isinstance(my_tesla, Car)) #it gives true because ElectricCar class inherit Car class
print(isinstance(my_tesla, ElectricCar))
