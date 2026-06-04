class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model

    #@staticmethod is a decorator which removes access of a function from object
    @staticmethod 
    def genral_description():  #self is not written because we dont want to link with object
        return "Car is a means of transport"
    
my_car = Car("tata","safari")

# print(my_car.genral_description()) - this will give error
print(Car.genral_description())