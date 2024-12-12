x = "hello"
print(id(x))
x = 'hey'
print(id(x))
print(x)

try:
    x[0] = 'c'
except Exception as e:
    print(e)

l = [1,2,3,4,5,6]
print(id(l))
l[0] = 7
print(l)
print(id(l))