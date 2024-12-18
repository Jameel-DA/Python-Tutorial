# Dictionary allows user to write the data in the form of keys and values.

# Dictionaries are enclose inside curly brackets{} 

# Keys and Values are separeted by colon.

# Every Key Value pair is Separated by a coma(,).

# Does not support indexing

# Data can be access using key

# Dictionary are collection of ordered data

# Creation of Dictionary

Emp = {"Name" : "Jameel Joy", "Age": 25, "Gender" : "Male"}
print(Emp)
print(Emp["Gender"])
print(type(Emp))

# Iteration in Dictionary
std = {"Name" : "Jameel", "Father Name" : "Sher Mohammed", "Age" : 24, "City" : "Jodhpur"}

# Printing all the key Names one by one 
for i in std:
    print(i)

# Printing all the values Names one by one
for j in std:
    print(std[j])

# Using Value Function
for k in std.values():
    print(k)

#Using Keys Function
for l in std.keys():
    print(l)

# Using Item Function
for m in std.items():
    print(m) 
    
     

d = {"name" :  "jameel", "age": 23, "salary": 2500000}

for i in d.values():
    print(i)
for i in d.keys():
    print(i)
for i in d.items():
    print(i)
for i, j in d.items():
    print(i,j)


# check frequemcy of items in dictionary

name = "Jameel Joy"
frequ = {}
for i in name:
    if i not in frequ:
        frequ[i] = 1
    else:
        frequ[i]+=1
print(frequ)