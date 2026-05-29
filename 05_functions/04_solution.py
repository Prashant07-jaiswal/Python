import math

def circle_stats(r):
    # area = 3.14*r**2
    area = math.pi*(r**2)
    # circumference = 2*3.14*r
    circumference = 2*math.pi*r
    return area, circumference

a, b = circle_stats(2)
print("Area:", round(a, 2), "Circumference: ", round(b, 2)) # round() is used to handle precision value for decimal places
                                                            #Area: 12.57 Circumference:  12.57