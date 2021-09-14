# There may be cases like when you have two variables of the same name but in different regions or scopes.
# In that case, python assumes that these variables are totally different from each other and if you make changes in one variable then that change will not affect the other scope variable.

var = "I m outside function"
def parentFun():
    var = "I m inside function"
    print(var)
parentFun()
print(var)