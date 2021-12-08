# If a function is inside another function then it can access the variable which is created inside the parent function but outside the child function.
def parentFun():
    var = "I m a variable"
    print(var)
    def childFun():
        print(var)
    childFun()
parentFun()