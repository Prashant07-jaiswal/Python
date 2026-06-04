class Car:
    total_car = 0    #this is class varibale                      
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        Car.total_car +=1    #this can be written as Self.total_car()                     
Car("tata","safari")
Car("tata","nexon")
print(Car.total_car)
