mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
print(type(mydict))

# We can also use "dict()"method to create a dictionary.
myDict = dict(key1="value1", key2="value2",key3="value3")
print(type(myDict))
print(myDict)

# Accessing values
# We can access dictionary values using a "key name" or using "get()" method.
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
print(mydict["key1"])
print(mydict.get("key2"))

# Update dictionary
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
mydict["newkey1"] = "newvalue1"
mydict["key1"] = "updatedvalue1"
print(mydict)
mydict["userinput"] = input("Enter value: ")
print(mydict)

# length of dict
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(len(mydict))

#delete keyword
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
del mydict["key1"]
print(mydict)
del mydict
print(mydict)

# pop() method
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
mydict.pop("key1")
print(mydict)
mydict.pop("key2")
print(mydict)

# popitem() deletes random value
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
mydict.popitem()
print(mydict)
mydict.popitem()
print(mydict)

# clear()
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
print(mydict)
mydict.clear()
print(mydict)

# copy()
mydict = {
    "key1" : "Value1",
    "key2" : "Value2",
    "key3" : "Value3"
}
newdict = mydict.copy()
print(newdict)
mydict["key1"] = "newvalue"
print(mydict)
print(newdict) # newdict will not be effected