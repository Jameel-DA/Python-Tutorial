# Updating a Dictionary

# using keys 
# update


# using keys
fruits = {"apple" : 120, "mango" : 90, "banana": 100,}

fruits["banana"] = {"1kg": 100, "2Kg": 200}

print(fruits)

# using update method
new = {"orange": 100, "berry": 200, "kiwi": 300}

fruits.update(new)
print(fruits)

# add new key and value in dictionary

fruits["guava"] = 80
print(fruits)

# Deleting data from dictionary
# pop - delete a specific value
# popitem - delete last element(Key,values)
# del - delete whole dictionary

print("apple" in fruits)
print(fruits.pop("apple"))
print(fruits)


fruits.popitem()
fruits.popitem()
fruits.popitem()
fruits.popitem()
fruits.popitem()

print(fruits)

del(fruits)


