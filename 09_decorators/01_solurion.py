import time

#timer decorator only accept function as parameter 
def timer(func):
    #wrapper is used to wrap the modification that we want to do in funtions it accept main function's parameter
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args)   #main function is executed
        end = time.time()
        #__name__ is used to give name of main function 
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(*args):
    sum = 0
    for i in args:
        sum += i 
    print(sum)

example_function(1,2,10,3,1,)

@timer
def example_function2(n):
    time.sleep(n)

example_function2(2)