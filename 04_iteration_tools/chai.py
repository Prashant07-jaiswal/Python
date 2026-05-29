import time 
print("hello brother ")
username = "WTF"
print(username)

#In a file __next__() raise exception at the end of file reading of:-
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration

#readline() handle this exception by returning empty string (" "):-
# >> f = open('chai.py')
# >>> f.readline()
# 'import time \n'
# >>> f.readline()
# 'print("hello brother ")\n'
# >>> f.readline()
# 'username = "WTF"\n'
# >>> f.readline()
# 'print(username)\n'
# >>> f.readline()
# ''

#we can use different iteration tools in file:-
# >>> for line in open('chai.py'):
# ...     print(line, end=" ")    
# ... 
# import time 
#  print("hello brother ")
#  username = "WTF"
#  print(username)

# >>> f = open('chai.py')   
# >>> while True:        
# ...     line =f.readline()
# ...     if not line: break
# ...     print(line,end=" ")
# ... 
# import time 
#  print("hello brother ")
#  username = "WTF"
#  print(username)

#iter() is a manual way to check iteration of object:-
# >>> list = [1, 2, 3, 4]   
# >>> I = iter(list)         ->it give starting memory address of a iterable object
# >>> I
# <list_iterator object at 0x000001C3A63D05B0>
# >>> I.__next__()           ->it is used to start loop inside list and it does not change the "list_iterator" reference 
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     I.__next__()
#     ~~~~~~~~~~^^
# StopIteration

#In file only iter() already integrated in it:-
# >>> f = open('chai.py')    
# >>> iter(f) is f
# True