class Car:
    #self is use to build connection line between obejct and attributes like brand,models through class
    #__init__ is a constructor which always execute first whenever object create 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Supra")  #this is obeject
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Dodge challenger", "demon")
print(my_new_car.brand)
print(my_new_car.model)