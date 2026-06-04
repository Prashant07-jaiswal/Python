class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model

    #@property is a decorator which is used not to over-write any property 
    @property
    #In model() "model" is compulsury to give otherwise @property decorator won't use  
    def model(self):
        return self.__model

my_car = Car("tata","safari")
# my_car.model = "city" - this will give error
print(my_car.model)
