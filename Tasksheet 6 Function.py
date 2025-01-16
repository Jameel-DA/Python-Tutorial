# 1. Create a simple function that takes two parameters and returns their sum.

def add(a,b):
    return a + b

print(add(2,5))


# 2. Explain the concept of a "return" statement within a function.

# Return keyword in python is used to exit a funtion and return the value of the function.
# 1 Returning a value.
# 2 Terminating the function.
# 3 Returning none If no value is specified in the return statement.

# 3. Create a function that calculates the area of a circle based on its radius and returns the result.

def area(radius):
    return 3.14*radius*radius

cal = area(4)
print(f"The Area of Circle is : {cal}")


# 4. Create a recursive function that calculates the factorial of a positive integer.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(f"The factorial : {result}")


# 5. Write a Python function called calculate_average that takes a list of numbers as a parameter and
# returns the average of those numbers.

def calculate_average(li):
    summ = sum(li)
    avg = summ/len(li)
    return avg

print(calculate_average([1,2,3,4,5]))


# 6. Create a function which checks whether a give number is prime or not.

def prime(num):
    if num == 1:
        print("Number is not Prime")
    else:
        for i in range(2,num):
            if num % i == 0:
                print("Number is not Prime")
                break
        else:        
            print("Number is Prime") 

prime(8)           

# 7. Create a function which check whether a given number is even or not.

def iseven(n):
    if n % 2 == 0: 
        return "Number is Even"
    else:
        return "Number is odd"
    
print(iseven(6))    

# 8. Create a function which takes a number as a value and find out its factorial, with recursion and
# without recursion.

def fact(n):
    ch = 0
    if ch == 1:
        print("Factorial without recursion")
        f = 1
        for i in range(1,n+1):
            f*=i
        return f
    else:
        if n == 0 or n == 1:
            return 1
        else:
            return n * fact(n - 1)

n = fact(6)
print(f"Factorial : {n}") 

# 9. Create a function named verify_email, which takes email as an argument and return True if an
# email is valid, else it returns False.

def verify_email(mail):
    if '@' not in mail or mail.count("@")!=1 or '.' not in mail\
    or " " in mail:
        return False
    else:
        return True

print(verify_email("jameeljoy68@gmail.com"))


# 10. Create a function named vowel_count which takes string as an input argument and return count
# of vowels inside that string.

def vowel_count(strr):
    count = 0
    for i in strr:
        if i in "aeiouAEIOU":
            count+=1
    return count

result = vowel_count("Jameel Hasan")
print(f"Total Vowels Available in String : {result}")


# 11. Write a program that defines a function sanitize_list( ) to remove all duplicate entries from the
# list that it receives.

def sanitize_list(li):
    # new_li = set(li)
    # return new_li

    new_li = []
    for i in li:
        if i not in new_li:
            new_li.append(i)
    return new_li

result = sanitize_list(['a','b','a','c','b'])
print("Sanitize List : ",result)
