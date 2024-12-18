# Q.1 Write a program to sort a dictionary in ascending/descending order by key and
# ascending/descending order by value.

di = {
    4:"b",
    3:"c",
    2:"a",
    6:"d",
    1:"e"
}
print("Keys in Ascending Order")
for i in sorted(di.keys()):
    print(i)

print("Keys in descending Order")
for i in sorted(di.keys(),reverse=True):
    print(i)

print("Values in Ascending Order")
for i in sorted(di.values()):
    print(i)  

print("Values in Descending Order")
for i in sorted(di.values(),reverse=True):
    print(i)        


# Q.2 Write a program to create three dictionaries and concatenate them to create
# fourth dictionary.

di1 = {
    "Name": "Jameel"
}
di2 = {
    "Age": 23
}
di3 = {
    "Salary" : 4000000
}

di4 = {}

di4.update(di1)
di4.update(di2)
di4.update(di3)

print(di4)

# Create three dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Initialize the fourth dictionary
dict4 = {}

# Concatenate the dictionaries using a loop
for d in (dict1, dict2, dict3):
    dict4.update(d)

# Print the resulting dictionary
print("Concatenated dictionary:", dict4)


# Q.3 Suppose there are two dictionaries called boys and girls containing names as
# keys and ages as values. Write a program to merge the two dictionaries into a third
# dictionary

boys = {
    "roy"  : 17,
    "joy"  : 18,
    "sam"  : 19
}

girls = {
    "riya" : 12, 
    "vanya" : 15, 
    "kasis" : 19 
}

merge = {}

merge = {**boys,**girls}
print(merge)

for key, value in boys.items():
    merge[key] = value

for key, value in girls.items():
    merge[key] = value

print(merge)    


# Q.4 Create a dictionary of 10 user names and passwords. Receive the user name and
# password from keyboard and search for them in the dictionary. Print appropriate
# message on the screen based on whether a match is found or not.

emp = {
    "User name" : ['a','b','c','d','e'],
    "Password" : ['12','311','22','1','3',]
}
user_name = input("Enter Your User Name : ")
password = input("Enter Your password : ")

if user_name in emp['User name'] and password in emp['Password']:
    print('Found',user_name)
else:
    print('Not Found')

# Q.5) In the following table check the box if a property is supported by the data types
# mentioned in columns?

# Property	             str	list	tuple	set	dict
# Object	              ✅	   ✅	  ✅	    ✅	✅
# Collection	          ✅	   ✅	  ✅	    ✅	✅
# Mutable	              ❌	   ✅	  ❌	    ✅	✅
# Ordered	              ✅	   ✅	  ✅	    ❌	✅ (since Python 3.7+)
# Indexed by position	  ✅	   ✅	  ✅	    ❌	❌
# Indexed by key	      ❌	   ❌	  ❌	    ❌	✅
# Iterable	              ✅	   ✅	  ✅	    ✅	✅
# Slicing allowed	      ✅	   ✅	  ✅	    ❌	❌
# Nesting allowed	      ✅	   ✅	  ✅	    ✅	✅
# Homogeneous elements	  ✅	   ❌	  ❌	    ❌	❌
# Heterogeneous elements  ✅	   ✅	  ✅	    ✅	✅

