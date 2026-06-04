class Car:
    def __init__(self, brand, model):
        self.__brand = brand              #"__brand" make the attributes private i.e obejct cant acces that attributes and we have to make function to get it
        self.model = model
    def get_brand(self):
        return self.__brand

my_car = Car("toyota", "supra")
# print(my_car.__brand)                  #this show error
print(my_car.get_brand())