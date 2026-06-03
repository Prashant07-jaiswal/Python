username = "pj"
def func():                #The sapce where the definition of function delclared is called scope 
    username = "Yash"

print(username)            #Inside function same variable do not affect global variable 

name = "victor"
def func2():
    # name = "dimitri"
    print(name)

func2()                       #Inside function print() also clime up for values and can use global variable
print(name)

x = 99
def func3(y):
    z = x+y
    return z                   #before alter() , z = 100 ; after alter() , z = 89
def alter():
    global x                   #global keyword manipulate glabal variable's value  
    x = 88 

alter()
print(func3(1))