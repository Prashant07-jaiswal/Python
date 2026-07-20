def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fib(10):
    print(i)

def fib2(n):
    a,b = 0,1
    while n>0:
        yield a
        a,b = b , a+b
        n -= 1

for i in fib2(10):
    print(i)