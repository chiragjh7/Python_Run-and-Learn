# len() function
myList = [34, 12, 10, 50, 45, 13]
print(len(myList))
# sort() function
myList = [34, 12, 10, 50, 45, 13]
myList.sort()
print(myList)
myList2 = ["d", "c", "a", "b", "B", "A"]
myList2.sort()
print(myList2)
# min() method
myList = [34, 12, 10, 50, 45, 13]
print(min(myList))
myList1 = ["d", "c", "a", "b", "B", "A"]
print(min(myList1))
# max() method
myList = [34, 12, 10, 50, 45, 13]
print(max(myList))
myList1 = ["d", "c", "a", "b", "B", "A"]
print(max(myList1))
# list() method 
myTuple = (1, 2, 3, 4)
myList1 = list(myTuple)
myString = "Hello"
myList2 = list(myString)
mySet = {1, 2, 3, 4}
myList3 = list(mySet)
print(myList1)
print(myList2)
print(myList3)

# append() method
myList = [1, 2, 3, 4]
myList.append(5)
print(myList)

# clear() method
myList = [1, 2, 3, 4]
myList.clear()
print(myList)

# copy() method
myList1 = [1, 2, 3, 4]
myList2 = myList1.copy()
print(myList2)

# reverse()
myList = [1, 2, 3, 4]
myList.reverse()
print(myList)

# sum() function
myList = [1, 2, 3, 4, 5, 6, 7]
addition1 = sum(myList)
print(addition1)
addition2 = sum(myList, 3)
print(addition2)

# range() function
myList1 = [*range(15)]
myList2 = [*range(4, 15)]
myList3 = [*range(4, 15, 3)]
print(myList1)
print(myList2)
print(myList3)

# pop() function
myList = [4, 5, 6, 7, 8, 9, 10, 11] 
print(myList.pop())  # 11
print(myList)
print(myList.pop(3))  # 7
print(myList)
print(myList.pop(0))  # 4
print(myList)
print(myList.pop())  # 10
print(myList)

# remove() method
myList = [4, 5, 6, 7, 8, 9, 10, 11]
print(myList.remove(4))  # removes 4 and returns nothing
print(myList)
myList.remove(7)
print(myList)
myList.remove(11)
print(myList)
print(myList.remove(3))  # 3 not present
myList = [4, 5, 6, 7, 4, 8, 9, 4, 10, 11]
myList.remove(4)
print(myList)
myList = [4, 5, 6, 7, 4, 8, 9, 4, 10, 11]
while 4 in myList: myList.remove(4)
print(myList)

# index() function
myList = [4, 5, 6, 7, 4, 8, 9]
print(myList.index(5))
print(myList.index(4))
print(myList.index(4, 2, 5))
print(myList.index(4, 2, 3))

# insert()
myList = [4, 5, 6, 7, 4, 8, 9]
myList.insert(0, 1)
print(myList)
myList.insert(1, 2)
print(myList)
myList.insert(10, 12)
print(myList)