try:
    a=10
    b='9'
    c=0
    print(a/c)
    print(a+b)
except TypeError:
    print('Type error encountered')
except ZeroDivisionError:
    print('Tried to divide the number by zero')