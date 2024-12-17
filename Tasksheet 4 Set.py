# Q.1 You have been given 2 sets named engineers, phd_holders.
# engineers = {"Ram","Shyam", "Radha", "Mohan", "Geeta", "Sunita"}
# phd_holders = {"Krishna", "Ram", "Rakesh", "Mohan", "Annirudh","Geeta"}
# solve all below mentioned condition using set methods

# i) Find out a set of those who are engineers but not phd_holders
# ii) Find out a set of those who are phd_holders but not engineers
# iii)Find out a set of those who either phd_holders or engineers
# iv) Find out a set of those who are both phd_holders and engineers
# v) Generate a new set in which every engineer and phd_holder is present only once. 

engineers = {"Ram","Shyam", "Radha", "Mohan", "Geeta", "Sunita"}
phd_holders = {"Krishna", "Ram", "Rakesh", "Mohan", "Annirudh","Geeta"}

print(engineers.difference(phd_holders))
print(phd_holders.difference(engineers))
print(engineers.symmetric_difference(phd_holders))
print(engineers.intersection(phd_holders))

new_set = engineers.union(phd_holders)

print(new_set)


# Q. 2 Do the above question without using set methods. 

engineers = {"Ram","Shyam", "Radha", "Mohan", "Geeta", "Sunita"}
phd_holders = {"Krishna", "Ram", "Rakesh", "Mohan", "Annirudh","Geeta"}

# i) Find out a set of those who are engineers but not phd_holders
new_set = set()
for i in engineers:
    if i not in phd_holders:
        new_set.add(i)

print(new_set) 


# ii) Find out a set of those who are phd_holders but not engineers

new_set = set()
for i in phd_holders:
    if i not in engineers:
        new_set.add(i)

print(new_set)         

# iii)Find out a set of those who either phd_holders or engineers
print(engineers.symmetric_difference(phd_holders))
new_set = set()
for i in engineers:
    if i in engineers and i not in phd_holders:
        new_set.add(i)
for i in phd_holders:
    if i in phd_holders and i not in engineers:
        new_set.add(i)        

print(new_set)  


# # iv) Find out a set of those who are both phd_holders and engineers

new_set = set()
for i in engineers:
    if i in engineers and i in phd_holders:
        new_set.add(i)
print(new_set) 

# v) Generate a new set in which every engineer and phd_holder is present only once. 

new_set = set()
for i,j in zip(engineers,phd_holders):
    new_set.add(i)
    new_set.add(j)
print(new_set)   

concatenated_list = list(engineers) + list(phd_holders)
print(set(concatenated_list))
     
       


# Q. 3 What are properties of sets and how you can create an empty set.

# Properties of sets
# Mutable
# Iterable
# Unordered
# Unique
# Dynamic
# Faster

# Create Empty Set
s = set()
print(type(s))


# Q.4 Write a program to find sum, average of all elements inside a set. 

s = {1,2,3,5,6}
# print("sum of set:",sum(s))
# print("average of set:",sum(s)/len(s))

summ = 0
count  = 0
for i in s:
    count+=1
    summ+=i

print("Sum of set : ",summ)    
print("Average of set : ",summ/count)    


# Q.5 What is frozen set, explain with an example. 
 
# A frozenset in Python is an immutable version of a set. Like a set, it is an unordered collection of unique elements, but it cannot be modified once created. Since it is immutable, a frozenset can be used as a key in dictionaries or as an element of another set (unlike regular sets).


# Creating frozensets
frozenset1 = frozenset(["apple", "banana", "cherry"])
frozenset2 = frozenset(["orange", "grape"])

# Using frozensets as dictionary keys
fruit_dict = {
    frozenset1: "Tropical Fruits",
    frozenset2: "Citrus Fruits"
}

# # Accessing values using frozenset keys
print("Category of frozenset1:", fruit_dict[frozenset1])
print("Category of frozenset2:", fruit_dict[frozenset2])

fs = frozenset([1,2,3,4,5])
print(fs,type(fs))


# Q.6 Differentiate among list, tuple, set and dictionary property wise?

# Ans.  Use a list for ordered, mutable collections that allow duplicates.
# Use a tuple for ordered, immutable collections.
# Use a set for unordered collections of unique elements.
# Use a dictionary for storing data in key-value pairs with unique keys.


# Q.7 Can we make a nested set? 

# Ans. No, we cannot make a nested set in Python    because sets are mutable and unhashable, and only hashable objects can be added as elements to another set. Since a set itself is unhashable, it cannot be added to another set.

# Attempting to create a nested set
set1 = {1, 2, 3}
set2 = {4, 5, set1}  # Error: TypeError: unhashable type: 'set'


# Q.8 What do you mean by sub set and super set. Is A sub set of B?

A = {1, 2, 3, 4, 5}
B = {2, 3} 

# Subset
print(A.issubset(B))
print(B.issubset(A),"\n")

# Superset
print(A.issuperset(B))
print(B.issuperset(A))



