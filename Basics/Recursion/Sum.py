def naturalSum(n):
    if n==1:
        return n
    else:
        return naturalSum(n-1) + n
number = int(input("Enter a number:"))
if number<=0:
    print("Enter a natural number")
else:
    print(naturalSum(number))