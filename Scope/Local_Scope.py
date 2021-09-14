# These are the variables that are created and accessible inside the function. These variables belong to local scope for the function inside which they are created.

def aFun():
    var = "I m a local variable"
    print(var)
aFun()
# print(var) // Error