# Write a program to print following patterns.

# i)
#  *
#  **
#  ***
#  ****
#  ***** 

for i in range(1,6):
    print("*" * i)


# ii)
#  *****
#  ****
#  ***
#  **
#  *

for i in range(5,0,-1):
    print("*" * i) 


# iii)
#  1
#  12
#  123
#  1234
#  12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()    


# iv)
#  1
#  23
#  456
#  78910

count = 0
for i in range(1,5):
    for j in range(1,i+1):
        count+=1
        print(count,end="")
    print() 


# v)
#  1
#  22
#  333
#  4444
#  55555

for i in range(1,6):
     for j in range(1,i+1):
         print(i,end="")
     print() 


# vi)
#    *
#   ***
#  *****
# *******

for i in range(1,5):
    print(" "*(4-i), "*"*(2*i-1))


# vii)
#  *******
#   *****
#    ***
#     *

for i in range(4,0,-1):
    print(" "*(4-i), "*"*(2*i-1))


# viii)
#     *
#    ***
#   *****
#  *******
#  *******
#   *****
#    ***
#     *

for i in range(1,5):
    print(" "*(4-i), "*"*(2*i-1))
for i in range(4,0,-1):
    print(" "*(4-i), "*"*(2*i-1))


# ix)
#  a
#  bc
#  def
#  ghij

ch = 97
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch+=1
    print()    


# x)
#  a
#  bb
#  ccc
#  dddd
#  eeeee

for i in range(97,102):
    for j in range(97,i+1):
        print(chr(i),end="")
    print() 


# xi)
#  *****
#  *****
#  *****
#  *****
#  *****   

for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()    


# xii)
#  ******
#  *   *
#  *  *
#  * *
#  *

for i in range(1,6):
    for j in range(1,6):
        if i == 1 or j == 1 or j == 6-i: 
            print("*",end="")
        else:
            print(" ",end="")    
    print()    


# xiii)

#  *******
#  ******

#  ****
#  ***
#  **
#  *

for i in range(7,0,-1):
    if i == 5:
        print()
        continue
    print("*"*i)


# xiv)
#  *
#  **
#  ***

#  *****
#  ******

for i in range(1,7):
    if i == 4:
        print()
        continue
    print("*"*i)


# xv)
# *****
# *   *
# *   *
# *   *
# *****

for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end="")
        else:
            print(" ",end="")
    print()    