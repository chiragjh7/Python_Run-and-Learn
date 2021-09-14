# Example 1:
myStr = "I am a string"
for x in myStr:
    print(x, end="")
# Example 2:
print(end="\n")
myList = ["I", "am", "a", "list"]
for x in myList:
    print(x, end = " ");
# Example 3: 
print(end= "\n")
myTuple = ("I", "am", "a", "tuple")
for x in myTuple:
    print(x, end = " ") 
# Example 4:    
print(end = "\n")
mySet = {1, 2, 3, 4, 5}
for x in mySet:
    print(x, end = " ")
# Example 5:
print(end = "\n")
myDict = {"key1": "value1", "key2" : "value2", "key3" : "value3"}
for x in myDict:
    print(x,":",myDict[x])    