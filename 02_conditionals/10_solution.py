species = str(input("Enter pet's species: "))

if species.lower() == "dog":
    age = int(input("Enter the pet age: "))
    if age < 2:
        print("Puppy food")
    else:
        print("Dog food")
else:
    print("Don't have data for this pet")