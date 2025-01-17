# Try Block

# This Block handles the error in your code if any of it exists

# Except Block

# This Block Gives the output that you want to show if your code is faulty

# Finally Block

# This Block will be executed in any case

# It is helpful when you want to de-allocate resources

# Like closing a File or db connection

a = 5
b = 0

try:
    f = open("new.txt")
    print(f.read())
    print(a/b)

except Exception as e:
    
    print("error : ",e)

finally:
    print("It is always Executed")        