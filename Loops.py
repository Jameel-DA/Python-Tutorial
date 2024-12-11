# Repeatation of any task is called Loop
# A Loop Means to repeat something in the exat same way.

# Types of Loop
# For loop
# while loop
# while true - It is an Infinite loop. to break a while true loop, break statement is used.
# Nested loop - Loop Inside a loop is called as nested loop. Nested lopp are also used for pattern problems.

n = 2
for i in range(1,11):
    print(n , "x" , i , "=",n*i)

i = 1
n = 5
while i <= 10:
    print(n, "x", i, "=", n*i)
    i+=1

while True:
    n = 1
    print(n)
    n += 1
    break;

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = " ")
    print()
    
n = 5
for i in range(1, 11):
    print(n ,"*", i, "=", n*i)

