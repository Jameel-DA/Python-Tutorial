""" 
Tuple are the collection of un-mutable data.

For tuples no brackets are mandatory. By choice one can use parentheses.

The value inside a Tuple is saparated by coma(,).

Once Created. Tuple cannot be changed.

Multiple Datatypes can be written inside a tuples.

We can Create Tuple using parentheses or without parentheses.
"""

t = "Jameel","Joy",1,2,3
print(t)
print(type(t))



t1 = ("Ok", "Hey", "Thank You")
print(t1)
print(type(t1))

# if we want to create a only one element tuple then we can use coma(,) 

t2 = "Hasan",
print(type(t2))

# Slicing and itration on Tuple.

tup = "Jameel", "Hasan", "Sakir", "Ajaz"

print(tup[0:2])
print(tup[0:4])
print(tup[::-1])

# Using for Loop
# for i in tup:
#     print(i)

# Using While Loop
j = 0
while j < len(tup):
    print(tup[j])
    j+=1

# Using short Hand for Loop
(print(i) for i in tup)


# Create list inside Tuple 

tup = ([1,2,3], "joy", "a")
print(tup)
print(type(tup))
print(type(tup[0]))

tup[0][0] = 5
print(tup)

# When we created list inside tuple we can change element of list

joy = "jameel",
print(type(joy))