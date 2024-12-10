# Whenever we have multipal condition in the program then we use conditional statement.
# conditional statement basically check the conditions in the code.
# 
# Types of Conditional statements: 
# If the Statement
# If-else Statement
# If-elif-else Statement
# Nested Statement
# Short Hand if Statement 

marks = 100

if marks >= 90 and marks <= 100:
    print("Merit")

elif marks >= 60 and marks < 90:
    print("I Division")  

elif marks >= 45 and marks < 60:
    print("II Division")

elif marks >= 33 and marks < 45:
    print("III Division")

else:
    print("Fail")

color = "Yellow"
print("Right Color") if color == "Yellow" else print("Wrong Color")