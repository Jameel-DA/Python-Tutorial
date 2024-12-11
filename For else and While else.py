l = ["apple", "manogo", "orange", "papaya"]

s = input("Enter Your Item : ")

for i in l:
    if i == s:
        print("Item Found")
        break
else:
    print("Item not Found")

j = 0
while j < len(l):
    if l[j] == s:
        print("Item Found")
        break
    j += 1
else:
    print("Item Not Found")       

