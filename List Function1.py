a = ["Hulk", "Spiderman", "Iron man", "Captain America", "Thor"]

print(a)

# to find the length of List
print(len(a))

# to count an occurance of a particular element
print(a.count("Hulk"))

# to add to the list in the last
a.append("joy")
print(a)

# to add to a specific location
a.insert(2,"Jameel")
print(a)

# to remove from a list
a.remove("Hulk")
print(a)

# to remove from a certain location
print(a.pop(1))

b = [1,2,3,4]
a.extend(b)
print(a)

l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in i:
        print(j)