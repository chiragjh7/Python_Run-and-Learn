f=open("sample.txt", "r")
print(f.read())
f.seek(20)
print(f.tell())