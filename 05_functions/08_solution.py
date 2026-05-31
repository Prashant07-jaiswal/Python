def key_value(**kwargs):
    print(kwargs)
    result = []
    for key, Value in kwargs.items():
        print(f"{key}: {Value}")
    #     result.append(f"{key}: {Value}")   #used when we want to store value and use it later
    # return result


key_value(name= "Superman", position= 1, power="laser")