n = int(input("Enter the numbers: "))
sum = 0

for x in range(1, n+1):
    if x%2 == 0:
        sum += x

print("The sum of even numbers is: ", sum)    