print("1: For Small size coffee\n2: For Medium size coffee\n3: For Large size coffee")

option = int(input("Enter/click option: "))
print("1: for extra shot of espresso\n0: for no extra shot")
extra = int(input("Enter/Click option: "))

if option == 1:
    if extra == 1:
        print("Small size coffee with extra shot of espresso")
    else:
        print("Small size coffee")
elif option == 2:
    if extra == 1:
        print("Medium size coffee with extra shot of espresso")
    else:
        print("Medium size coffee")
    
elif option == 3:
    if extra == 1:
        print("Large size coffee with extra shot of espresso")
    else:
        print("Large size coffee")
else:
    print("Kindly enter/click correct option")
