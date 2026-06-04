class Car:
    def __init__(self, brand,model):  #this is constructor built desire atrributes inside class
        self.brand = brand
        self.model = model

    def full_name(self):   #this is function inside class
        return f"{self.brand}-{self.model}"
    
my_car = Car("toyota","supra")
print(my_car.full_name())
