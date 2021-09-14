def factorial(n):
    if n==1:
        return n
    else:
        return factorial(n-1) * n
number = int(input("Enter a number:"))
if number<0:
    print("Enter a non-negative number")
else:
    print(factorial(number))