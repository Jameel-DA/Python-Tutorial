# Parameters - the values We pass while defining a function

# Arguments - the actual value of we pass when calling a function

def joy(name): #Parameter
    return name

print(joy("jameel")) #Argument

# Positional Arguments - The value you pass when calling a funtion are matched according to their position.

def intro(name,hobby):
    print(f"my name is : {name}")
    print(f"my hobby is : {hobby}")

intro("jameel", "cricket")   


# Types of Argument in python

# Positional Argument : pass exat argument

# Default Argument : Pass Default Argument 

# Arbitrary Argument : *args(Return Tuple) and **kwargs(Return Dictionary)

