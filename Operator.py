"""Oprater is symbol that is used perform a paticular task.
   
Operator Indicates what opeartion is to be performed while oprands indicates on what the action or operation should be performed.

In python there are 7 types of operators
1. Airthmetic Oprator
2. Comparision Operator
3. Logical Operator
4. Assignment Operator
5. Identity Opearator
6. Membbership operator
7. Bitwise Oprator
"""
# Airthmetic Operators

print(5+5) #Addition
print(5-5) #Subtraction
print(5*5) #Multiplication
print(6/5) #Division
print(8//5) #Floor Division
print(3**3) #Exponentiation
print(5%3) #Modulus

#Comparision Operators

print(5<3); #Less Than
print(3<=3); #Less Than or Equal To
print(5>3); #Greater Than
print(5>=3); #Greater Than or Equal To
print(5!=3); #Not Equal To
print(5==5); # Equal To

# Logical Operators

print(5 > 4 and 5 > 5) #Logical And
print(5 > 4 or 5 > 5)  #Logical Or 
print(not 5 > 4 or 5 > 5) #Not

# Assignment Operators

a = 5 #Equal to
a+=2 #Plus Equal to
print(a)
a-=2 #Minus Equal to
print(a)
a*=2 #Multiply Equal to
print(a)

#Identity Operators - Identity Operator are used to compare item to see if they are the same object with the same memory address.

#There are two types of identity operator
#1. Is 
#2. Is not

a = 123
b = "123"
print(a is b)
print(a is not b)

# Bitwise Operators - These Operator are used to compare binary number

# Types 
# AND operator
# OR operator
# XOR Operator
# << zero fill left shift
# >> zero fill right shift

x = 10
y = 8

print(x&y)
print(x|y)
print(x^y)
print(x<<1)
print(x>>1)

# Membership Operator - Membership Operator are used to check the present of the sequence in an object

# There are two types of membership operator
# 1. In
# 2. Not in

name = "Jameel"
print("j" in name)
print("J" in name)
print("a" not in name)
