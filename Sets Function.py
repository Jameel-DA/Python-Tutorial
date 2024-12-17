# Types of Set Function 

s = {1,2,3,4,"jameel", "joy"}

# add
s.add("Hasan")
print(s)

# pop - remove random element. we are not sure what is it
s.pop()
print(s)

# remove - removes particular element
s.remove("Hasan")
print(s)

# discart
s.discard("jameel")
print(s)

# copy
s1 = s.copy()
print(s1)

# update
s.update("1")
print(s)

a = {1,2,3,4,5}
b = {6,7,8,9,10}
c = {2,3,8,9}

# Union
print(a.union(c))

# Difference
print(a.difference(c))

# Intersection
print(a.intersection(c))

# Symmectric
print(a.symmetric_difference(c))

# find the unique element in a sentence

sent = "my name is jameel joy and my hobby is playing cricket"
print(type(sent))

s = set(sent.split())
print(s)

print(len(s))

# split method is used to convert string into list

st = "ok hii ok hii hello"
print(set(st.split()))
