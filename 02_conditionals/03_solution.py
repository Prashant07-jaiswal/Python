score = int(input("Enter marks out of 100 :"))

if score > 100:
    print("!Enter correct marks out of 100")
    exit()    #used to terminate upcoming operations

if  score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:  
    grade = "D"
else:
    grade = "F"

print("Your grade is :", grade)
          