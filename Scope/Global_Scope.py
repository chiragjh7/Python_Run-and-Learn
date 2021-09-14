# These are the variables that are created in the main body of the python code and not inside a function. These variables belong to the global scope.
# These variables are available within any scope, local and global.

var = "I m a global variable"
def aFun():
    print(var)
aFun()
print(var)