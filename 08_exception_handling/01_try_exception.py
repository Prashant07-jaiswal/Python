a = int(input("enter your no.: "))

#try keyword is used to handle exception . try must used along with except
try:
    print(10/a)

#excpt keyword is used to store exception in variable like 'err' and print statement 
except Exception as err:
    print(f"Sorry!You can't perform this operation as error is raised as {err}")

#else keyword is used to run code if no exception occur
else:
    print("there is no exception")
    
#finally keyword is used to run code no matter what happend whether there is exception or not
finally:
    print("Thanks for using it")


print("Work is done")
