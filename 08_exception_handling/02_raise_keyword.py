age = int(input("Enter your age: "))
if age<10 or age>18:
        #raise keyword make erorr
        raise ValueError("Your age must be in between 10-18")
else:
        print("welcom to club")

print("club is coming soon")
