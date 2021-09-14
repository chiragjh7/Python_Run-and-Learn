# print("Hello I am a String")
# print('Hello I am also a String')
# Assigning String to a variable
a = "hello"
b =  """I am multiline
string"""
c = '''I am also a 
multiline 
string'''
print(a)
print(b)
print(c)
# String Slicing
mystr = "I am a string"
print(len(mystr))  # 13
print(mystr[0])  # 'I'
print(mystr[1])  # ' '  blank space
print(mystr[0:len(mystr)])  # full string
print(mystr[:])  # here python automatically assigns 0 and value of length of string
print(mystr[-2:-1])  # 'n'
print(mystr[-14:-1])  # full string excluding 'g'
print(mystr[:100])  # full string (no errors)

# String Concatenation
m = "2"
n = "4"
print("12.3" + "34.6")  # string concatenation
print(m + n)  # string concatenation
print(int(m) + int(n))  # simple addition

# Comma in print statement
print("This name is", "Harry")
print("My roll number is", 21)
# end inside print() statement
print("Hello")
print("World")
print("Hello", end="")  # no line change will happen
print("World")
print("Hello", end=" ")  # no line change only space will be inserted
print("World")
print("Hello", end=" my ")  # inserting my between Hello and World
print("World")

# Format() method
print("Name:{name} and age:{age}".format(name="Harry", age=30))
print("Name:{0} and age:{1}".format("Harry", 30))
print("Name:{1} and age:{0}".format("Harry", 30))
print("Name:{} and age:{}".format("Harry", 30))
# Fast string
name = "Harry"
age = 30
print(f"Name:{name} and age:{age}")
print(f"Addition:{5+4}")
print(f"Multiplication:{eval('1+2//4-20*9')}")
''' eval() is a built-in function
    used to calculate a string 
    which contains some arithematic
    calculations of numbers'''

# String length
a = "Hello"  
b = """This is 
a multiline
string"""
c = '''This is
also a multiline
string'''
print(len(a))
print(len(b))
print(len(c))

# lower() method
mystring = "I Am A String"
print(mystring.lower())
# upper() method
mystring = "I Am A String"
print(mystring.upper())

# Escape characters
print("I am \"a\" String")
print("Printing in \nNew Line")
print("Printing with a \ttab space")
print("Printing a single quote\'")