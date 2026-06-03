class Car:
    def __init__(self, brand,model):                 #this is constructor built desire atrributes inside class
        self.brand = brand
        self.model = model

    def full_name(self):                             #this is function inside class
        return f"{self.brand}-{self.model}"

class ElectricCar(Car):
    def __init__(self, brand , model, battery_size):
        super().__init__(brand,model)                 #super() used to initialize other classes attributes to inheritant class 
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.full_name())
