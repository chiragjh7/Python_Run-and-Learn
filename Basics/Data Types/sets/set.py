# Sets are "mutable" datatypes i.e. we can modify them after their creation.
mySet = {1, 2, 3, 4, 5}
yourSet = {"This", "is", "your", "set"}
print(mySet)
print(yourSet)
# Sets contain single elements i.e. there are no duplicate elements.
# We are free to declare sets with duplicate elements but Python will count only one time with no errors.
mySet = {1, 2, 3, 4, 5, 1, 2, 3}
print(mySet)

# Check an element
mySet = {1, 2, 3, 4, 5}
print(1 in mySet) # will return True if present else False
print(5 in mySet)
print(6 in mySet)
print(100 in mySet)

# We can add more items to a set using "add()" and "update()".
# "add()" is used to add one element and "update()" is used to add any number of elements.
mySet = {1, 2, 3, 4, 5}
mySet.add(6)
print(mySet)
mySet.update([7, 8, 9])
print(mySet)

# set() method
# We can use "set()" method to create sets.
myString = "I am a String"
myList = [1, 2, 3, 4]
myTuple = (5, 6, 7, 8)
set1 = set(myString)
set2 = set(myList)
set3 = set(myTuple)
print(set1)
print(set2)
print(set3)

# len() method
set1 = {1, 2, 3, 4, 5}
set2 = {"I", "am", "a", "set"}
print(len(set1))
print(len(set2))

# Delete or clear()
# Use "clear()" to clear the elements of a set i.e. to delete the elements inside a set.
# Use "del" keyword to delete a set permanently.
mySet = {1, 2, 3, 4, 5}
mySet.clear()
print(mySet)
del mySet
print(mySet)

# remove() and discard()
mySet = {1, 2, 3, 4, 5}
mySet.remove(1)
print(mySet)
mySet.discard(2)
print(mySet)

# pop() method
mySet = {1, 2, 3, 4, 5}
returnValue = mySet.pop()
print(mySet)
print(returnValue)

