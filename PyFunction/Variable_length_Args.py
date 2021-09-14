'''
Sometimes, we may not know the number of arguments going to be passed in the function, in that case, we can use variable-length arguments.

Variable-length Arguments are defined using star(*) before the argument during the defining of the function. Usually, we use *args for this purpose.

The arguments we pass as Variable-length Arguments are treated as tuple.
'''

def addAll(*args):
    result = 0
    for x in args:
        result = result + x
    return result
print("Sum is", addAll(1, 2, 3, 4, 5))

def addAll(*args):
    print(type(args))
    return sum(args)
print("Sum is", addAll(1, 2, 3, 4, 5))