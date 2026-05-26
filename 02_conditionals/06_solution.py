distance = float(input("Enter the distance in km:"))

if distance <= 3:
    print("walk")
elif distance <= 15:
    print("Bike")
else:
    print("car")

