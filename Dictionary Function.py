student = {"Name" : "Jameel", "Class" : "First", "Grade" : "A", "Age" : 23}
print(student)

# get - it is used for accessing a particular element if element not found we can display msg. 
print(student.get("Name", "not found"))

# Items
print(student.items())

# Keys
print(student.keys())

# Values
print(student.values())

# Copy
std = {}
std = student.copy()
print(std)

name = ["apple", "mango", "banana", "papaya"]
price = [120,50,100,200]

fruits = dict(zip(name,price))

print(fruits)