def even_genarator(limit):
    for i in range(0,limit+1,2):
        yield i

for x in even_genarator(10):
    print(x)




# import itertools

# def even_number_generator(limit):
#     even=[]
#     for num in itertools.count(0):
#         if num == limit:
#             break
#         else:
#             if num %2 == 0:
#                 even.append(num)
#     return even

# print(even_number_generator(11))