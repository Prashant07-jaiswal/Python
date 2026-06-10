def debug(func):
    def wrapper(*args, **kwagrs):
        arg_value = ', '.join(str(x) for x in args)
        kwarg_value = ', '.join(f"{k}:{v}" for k,v in kwagrs.items())
        print(f"calling {func.__name__} with agrs value {arg_value} and kwargs value {kwarg_value}")
        result = func(*args, **kwagrs)
        return result
    return wrapper

@debug
def greet():
    print("hello")

@debug
def greetings(name, greet):
    print(f"{greet} {name}")


greet()
greetings("PJ" , "hello sir!")