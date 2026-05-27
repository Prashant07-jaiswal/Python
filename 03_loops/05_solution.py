book = "tgtgtgkhj"


for x in book:
    print(x)
    if book.count(x) == 1:
        print("First non repeated character is : ", x)
        break