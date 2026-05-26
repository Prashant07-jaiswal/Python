weather = str(input("Enter the weather condition:"))

if weather.lower() == "sunny":
    print("You can go for walk")
elif weather.lower() == "rainy":
    print("Read a book")
elif weather.lower() == "snowy":
    print("Build a snowman")
else:
    print("can't suggest")
    