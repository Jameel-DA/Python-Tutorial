# Continue Statement - continue statement is used when you want to skip a particular condition.

# Break Statement - break statement is used when you want to destroy a loop at a certain condition and come out of the loop.

#Pass - To avoid syntax Error

for i in range (1,10):
    if i == 5:
        continue
    else:
        print(i)

for j in range (1,10):
    if j == 4:
        break    
    else:
        print(j)   

for i in range(1,11):
    pass

def fun():
    pass