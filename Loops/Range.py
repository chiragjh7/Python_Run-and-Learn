"""
"range()" is an in-built function in Python which takes three integers as parameters and returns a sequence of numbers.
range(start, stop, step)
*start : optional, default is 0
*stop : required, top-most position(stop-1)
*step : optional, this is the increment in value, default by 1
"""

for x in range(5):
    print(x) # start with 0(default)
             # 5 not included (5-1 = 4)

for x in range(1,5):
    print(x) # start with 1

for x in range(2, 11, 3):
    print(x) # starts with 2
              # ends on 11-1=10
              # 2+3=5
              # 5+3=8
              # 8+3=11(not included)             

myList = ["This", "is", "my", "list"]
for x in range(len(myList)):
    print(myList[x])