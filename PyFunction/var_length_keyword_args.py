'''
Python provides us the flexibility to pass Variable-length Keyword Arguments.

These are those keyword arguments that do not have fixed length i.e. during defining a function we do not know the number of keyword arguments are going to be passed.

These are represented using **kwargs. Unlike *args, which are treated as tuples, these are treated as a dictionary.
'''
def addAll(**kwargs):
    print(type(kwargs))
    print(kwargs)
    result = 0
    for x in kwargs:
        result = result + kwargs[x]
    print(result)
addAll(key1=1, key2=2, key3=3)