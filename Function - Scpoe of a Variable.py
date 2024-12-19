# There are two scope of a variable - Global and Local

# Global variable can be used anywhere in program

# Local variable can only be used locally inside a program

a = 20
def joy():
    a = 10
    print(a)
joy()
print(a)    

a = 10
def joy1():
    global a
    a = 5
    print(a)
joy1()
print(a)    


          