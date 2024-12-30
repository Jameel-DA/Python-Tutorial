# A Constructor is a special method of a class
    
# This method is defined in the class 

# the Contructor is executed automatically at the time of object creation.

# We can create a contructor using double under Score


class Animal:
    def __init__(self, name, age):
        print("This will always executed")
        self.name = name
        self.age = age
        print(f"Name : {name}, \nAge : {age}")

Dog = Animal("Jameel",23) 

print(Dog.name)
print(Dog.age)