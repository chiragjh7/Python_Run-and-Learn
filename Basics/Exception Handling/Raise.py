try:
    a=10
    b=-2
    if b<0:
        raise ValueError
    else:
        print(a/b)
except ValueError:
    print(' Don’t divide by negative number... it will give negative result')