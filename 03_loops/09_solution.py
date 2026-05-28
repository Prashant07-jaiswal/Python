items = ["apple", "banana", "orange", "apple", "mango"]
unique = set()

for i in items:
    if (i in unique):
        print(i, "Not unique element")
        break
    unique.add(i)
    
    # if items.count(i) == 2:
    #     print(i, "is not unique element in a")
    #     break
