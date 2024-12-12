# endswith() - Return true if the string ends with specified value

a  = "harry porter"
print(a.endswith("r"))

# startswith() - Return true if the string starts with specified value

b = "Jameel Joy"
print(b.startswith("e"))

# swapcase() - swap cases, lower case become upper case and vice versa

c = "My Name is Jameel JOY"
print(c.swapcase())

# strip() - Return a Trimmed version of the string

d = "        i am Joy"
print(d)
print(d.strip())

# split() - split the string at the specified saparator and return a list

e = "#jnsaj#bbh#bbh##hvh"
print(e.split("#"))

# ljust() - Return a left justified version of string

f = "Hello"
x = f.ljust(20)
print(x,"My name is joy")

# rjust() - Return a right justified version of string

g = "Hey"
y = g.rjust(20)
print(y,"My name is joy")

# replace - Return a string where a specified value is replaced with a specified value

h = "My Name is Joy"
print(h.replace("Joy", "hasan"))

# rindex - Searches the string for a specified value and return the last position of where it was found
 
i = "Ok I am Joy"
print(i.rindex("Joy"))

# rfind - Searches the string for a specified value and return the last position of where it was found

j = "I am MBA student"

print(j.rfind("MBA"))