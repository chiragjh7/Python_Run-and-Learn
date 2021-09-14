try:
    a=10
    b=0
    c=4
    print(a/c)
except ZeroDivisionError:
    print('Tried to divide the number by zero')
else:
    print('No exception found.. Entered else part')