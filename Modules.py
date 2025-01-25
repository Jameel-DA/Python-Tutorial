# Modules are the (.py) files. that contains set of function you want to include in your program.

# In-built Module in python
# Datetime 
# Random
# Math

import datetime
x = datetime.datetime.now()
print(x)

y = datetime.datetime(1919,10,10)

print(y.strftime("%A"))

import random

z = random.randint(1,10)
print(z)

l = ["Jameel", "Joy", "Hasan"]
s = random.choice(l)
print(s)

import math
m = max(1,5,2)
print(m)

m1 = min(3,4,1)
print(m1)

p = pow(2,4)
print(p)

sq = math.sqrt(256)
print(sq)

ab = abs(-123.88)
print(ab)

f = math.floor(22.9)
print(f)

c = math.ceil(2.2)
print(c)