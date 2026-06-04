class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    #fuel_type() is used in both classes with different value return.   
    def fuel_type(self):  
        return "pertrol and diesal"
class ELectricCar(Car):
    def __init__(self, brand, model,batter_size):
        super().__init__(brand, model)
        self.battery_size = batter_size
    def fuel_type(self):
        return "Electric Charge"
    
my_safari = Car("tata", "safari")
my_tesla = ELectricCar("Tesla", "Model S", "85Kwh")
print(my_safari.fuel_type())
print(my_tesla.fuel_type())