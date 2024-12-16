# When we tuple value assign a particular variable its call unpacking.

# example

t = (1,2,3,4)
a,b,c,d = t

print(a,b,c,d)

#  this process is known as unpacking

elements = (10, 20, 30, 40, 50, 60, 70, 80)
print(elements[2:5], elements[:4], elements[3:100])

name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)

fruits = ("Orange")
print(type(fruits))
