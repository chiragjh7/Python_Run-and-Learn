'''
Python have another way to create functions.
In this way, python uses lambda keyword to create a function.
Lambda function can take any number of arguments and it evaluates the expression and return the result which we can store using a variable.
#? lambda arguments : expression
'''
x = lambda y : y * 2
print(x(5))

x = lambda y,z :y * z + 2
print(x(5,10))

a = lambda x,y,z : x + y * z + 2
print(a(5,10,12))