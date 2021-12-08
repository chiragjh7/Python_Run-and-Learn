# Python provides global keyword to create a variable that can be accessed globally.
# We should use global keyword to create a global variable inside a function.
def myFunc():
    global x
    x = "A global variable"
    print(x)
myFunc()
print(x)
# Use the global keyword to make changes or to use a global variable inside a function.
x = "A global variable"
print(x)
def myFunc():
    global x
    x = "I m a variable"
    print(x)
myFunc()
print(x)
