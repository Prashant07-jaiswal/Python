import time

def cache(func):
    #to store value of the function's code cache_value is declare as dict "it is easy to get access by dict"
    cache_value = {}
    print(cache_value)
    def wrapper(*agrs):
        #it checks is value of args present in cache_value (args stores tuple of parameter "(2,3)"")
        if agrs in cache_value:
            #that tuple (2,3) used as a key in dict because tuple is immutable 
            return cache_value[agrs]
        result = func(*agrs)
        #resutl store compute value and it stored as a value in key args(2,3)
        cache_value[agrs] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a*b

print(long_running_function(2,3))
print(long_running_function(2,3))
