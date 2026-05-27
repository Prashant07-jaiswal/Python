numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_positive = 0
count_negative = 0
count = 0
for x in numbers:
    if x > 0:
        count_positive += 1
    elif x < 0:
        count_negative += 1
    else:
        count += 1

print(count_positive, "Positive numbers")

