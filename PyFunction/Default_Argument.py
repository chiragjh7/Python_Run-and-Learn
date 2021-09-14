def myFun(name, roll, likes, age=32):
    print("Name:", name)
    print("Age:", age)
    print("Roll No:", roll)
    print("Likes:", likes[0], "and", likes[1])
myFun("John", 12, ["Music", "Dancing"])
print()
myFun("John", 12, ["Music", "Dancing"], 22)