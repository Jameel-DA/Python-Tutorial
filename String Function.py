a = "hello"
b = "hello123"
c = "12345"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"

"""isalnum - Retuurn true if all character in the String are alphanumeric.

isalpha - Return true if all character in the String are in the alphabet.

isdecimal - Return True if all the charcter in the String are decimal.

isdigit - Return True if all the character in the String are digit.

isnumeric - Return true if all the character in the String are numeric.

islower - Check if the String is lowercase or not.

isupper - Return true if all character in the string are upper case.

isspace - Return true if all character in the string are whitspaces.

istitle - Return true if the string follows the rules of title.
"""

print(a, a.isalnum())
print(a, a.isalpha())
print(b, b.isalpha())
print(b, b.isdecimal())
print(g, g.isdecimal())
print(c, c.isdigit())
print(d, d.isdigit())
print(c, c.isnumeric())
print(e, e.islower())
print(d, d.isupper())
print(e, e.isspace())
print(g, g.istitle())


