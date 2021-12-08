def myFun(arg):
    print("Passed argument is==>", arg)
myFun("I am a argument")

def myFun(name, age, roll, likes):
    print("My name is", name)
    print("My age is", age)
    print("My roll no is", roll)
    print("I like", likes[0], "and", likes[1])
myFun("John", 22, 12, ["Music", "Dancing"])

def addThree(num1, num2, num3):
    return num1+num2+num3
addition = addThree(1, 2, 3)
print(addition)