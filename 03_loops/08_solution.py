prime = int(input("Enter  a number: "))
is_prime = True
if prime>1:
    for i in range(2,prime):
        if prime%i == 0:
            is_prime = False
            break
else:
    print("Not prime number")
    
if is_prime == True:
    print("Prime number")
else:
    print("Not prime number")