from pathlib import Path

def showfile():
    path = Path("")
    items = list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i} : {items}")





def creatfile():
    showfile()







print("choose 1 for Creating a file")
print("choose 2 for Reading a file")
print("choose 3 for Updation a file")
print("choose 4 for Deletion a file")

option = int(input("Enter what operation you want to perform"))

if option == 1:
    creatfile()