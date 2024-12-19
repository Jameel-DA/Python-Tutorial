# Function are a set of code, which once created, they can be used throughout the program.

# Function helps break our program into smaller parts and helps it look more organized and manageable.

# Parameters: Parameters are the variables written inside the parantheses with the name of function.

# Arguments: Arguments are the values passed to the parameters while calling the funtion.

# Return keyword in python is used to exit a funtion and return the value of the function.

# Recursion Means a function can call itself, giving us a benefit of looping through data in order to get a result.

# Funtion is a user define piece of code it works only when its called by user. it helps reusability of code and helps in reducing errors in your code. 
 
# helps in reusability of code.
# make code manageble and organized.

# Functions are two types
# user define
# built ins

def rectArea(l,b):
    return l * b

print("Area of rectangle is : ",rectArea(2,3))

def joy(*name):
    print(name)
joy("Jameel","joy","Hasan")
joy(1,2,3)

# Find Factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(6))

def num():
    for i in range(1,11):
        print(i)

# what is Docstring 


def convert(t):
    return t*9/5 + 32

print(convert(20))

def fun(name,age = 25):
    print(name,age)

fun("mohit",23)    