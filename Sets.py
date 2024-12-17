# Sets are Unordered collection of data. Every Element inside the set is unique and mutable.

# Sets are  written inside the curly brackets.
# The value inside a set is separated by coma(,).
# Mutable means once we created, they can be changed.

# Unique Collection
# Unordered
# Unindexed
# Mutable

s = {1,23,4,2,3,4,5}
print(s)
print(type(s))

# In the sets Elements are not Repeated.

# if we declare in sets common element so the element is not printed.

s2 = {"Jameel", "joy", 10, True}
for i in s2:
    print(i)
    
set1 = {1, 2, 4}
set2 = {4, 5, 6}
print(len(set1 + set2))    

sets = {3, 4, 5} 
sets = sets.union({1, 2, 3})
print(sets)

a={'Aurn', 'Nikhil', 'Seeta'}
a[0]= 'Arun'
print(a)    