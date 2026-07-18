card_details = {111:4783,222:4647}
user_detail = {4783:40000,4647:10000}
print("Choose Services")
print("1. Withdrawal")
print("2. Balance")
print("3. Change Password")
print("4. Exit")
while True:
    operation = int(input("Enter your option: "))
    if operation==1:
        try:
            pin = int(input("Enter your PIN NO.: "))
        except ValueError:
            print("INVALID PIN")
        found = False
        for k,v in card_details.items():
            if pin == v:
                found = True
                amt = int(input("Enter your Amount: "))
                if amt < 0:
                    print("Enter a positive amt")
                elif amt > user_detail[v]:
                    print("Insufficient Balance")
                elif amt == 0:
                    print("Enter a valid amt")
                else:
                    up = user_detail[v] - amt
                    user_detail[v] = up
                    print(f"{amt} has be successfully Withdrawal")
                break
        if not found:
            print("Invalid PIN!")


    elif operation==2:
        try:
            pin = int(input("Enter your PIN NO.: "))
        except ValueError:
            print("Invalid PIN!")
        found = False  
        for k,v in card_details.items():
            if pin == v:
                found = True
                for p,amt in user_detail.items():
                    if p == v:
                        print("Your Balance is: ",amt)
                        break

        if not found:
            print("Invalid PIN")

    elif operation==3:
        try:
            pin = int(input("Enter your PIN NO.: "))
        except ValueError:
            print("Invalid PIN!")
        found = False
        for k,v in card_details.items():
            if pin == v:
                found = True
                new_pin = int(input("Enter your new PIN NO.: "))
                new_pin2 = int(input("Confirm your new PIN NO.: "))
                if new_pin != new_pin2:
                    print("PIN NO. not match")
                    break
                else:
                    card_details[k] = new_pin
                    user_detail[new_pin] = user_detail.pop(v)
                    print("PIN NO. successfully changed")
                    break
        if not found:
            print("Invalid PIN")
    elif operation==4:
        print("Thank You")
        break  
    else:
        print("Invalid Input")