"""
Tuples are sequential data types in Python.
A Tuple is an immutable data type in Python i.e. once defined it can not be changed.
Use round brackets"()" to define a Tuple in Python and comma(,) to separate elements.
We can access Tuple elements using the index value of the element.
Like lists, there is both side indexing in Tuples in Python i.e. from start indexing starts with “0” and from the end, indexing starts with “-1“.
"""

myTuple = (1, 2, 3, 4, "Hello", "World")  # defining a list
print(myTuple)  # printing a list
print(myTuple[0])  # printing first element
print(myTuple[1])  # printing 2nd element
print(myTuple[5])  # printing last element
print(myTuple[-1])  # printing last element
print(myTuple[-2])  # printing last 2nd element

# One element tuple
myTuple = (1) # int
myTuple1 = ("1") # str
myTuple2 = (1,) # tuple
print(type(myTuple))
print(type(myTuple1))
print(type(myTuple2))

# Range of Indices
myTuple = (1, 2, 3, 4, "Hello", "World")  # index starts with 0
print(myTuple[0:3])  # 0 to 3-1=2(excluding last value)
print(myTuple[4:5])
print(myTuple[-6:-1])  # negative indexing similiar to list
print(myTuple[-3:-2])

# Tuple length
myString = "I am a String"
myList = ["I", "am", "a", "List"]
myTuple = ("I", "am", "a", "Tuple")
print(len(myString))
print(len(myList))
print(len(myTuple))

# Joining two tuple
myTuple1 = (1, 2, 3, 4)
myTuple2 = (5, 6, 7, 8)
myTuple3 = (9, 10, 11, 12)
add1 = myTuple1 + myTuple2
add2 = myTuple1 + myTuple2 + myTuple3
print(add1)
print(add2)

# Tuple contructor
myStr = "1234"
myList = [1, 2, 3, 4]
myTuple1 = tuple((myStr))
myTuple2 = tuple((myList))
emptyTuple = tuple()
print(emptyTuple)
print(myTuple1)
print(myTuple2)
