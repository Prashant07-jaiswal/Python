age = int(input("enter the age: "))
day = str(input("enter the day: "))
price = 8 if age < 18 else 12

if day.lower() == "wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $", price) 
   