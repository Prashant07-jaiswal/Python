fruit = "Banana"
color = str(input("Enter the color of fruit(green or yellow or brown):"))

if fruit.lower() == "banana":
    if color.lower() == "green":
        print("Unripe")
    elif color.lower() == "yellow":
        print("Ripe")
    elif color.lower() == "brown":
        print("Overripe")
    else:
        print("Didn't recognize condition of fruit")
else:
    print("Don't have methode to check")    #if there is different fruit we can made different methode to check