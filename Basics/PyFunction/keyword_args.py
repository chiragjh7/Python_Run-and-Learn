'''
Python allows us to send arguments in key=value format.
During this type of arguments, the order of arguments does not matter.
Keyword’s name should match the argument’s name in the function definition. If matches found then the keyword values get copied to the arguments, else python interpreter will give the error.
'''
def addAll(val1, val2, val3):
    return val1+val2+val3
print(addAll(val1=4, val2=5, val3=6))