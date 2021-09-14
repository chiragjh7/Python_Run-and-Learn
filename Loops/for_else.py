# for loop without break
for x in range(5):
    print(x)
else:
    print("else block")
    
# for loop with break
for x in range(5):
    print(x)
    if x == 3:
        break
else:
    print("else block will not executed")