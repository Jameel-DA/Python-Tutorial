# 1. Write a program to check whether a given string is palindrome or not.

st = "121"
if st == st[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 2. Email Validation: Write a program to check whether a given email address is valid or not
# a. An email is valid if following conditions are met.
# b. It must contain a single "@" symbol.
# c. It must contain a domain name (e.g., "example.com").
# d. The domain name must have at least one "." (e.g., "com", "co.uk", "org").
# e. There should be no spaces in the email.    


email = input("Enter Your Email : ")
email = "jameeljoy68@gmail.com"
if '@' not in email or email.count("@")!=1 or '.' not in email\
or " " in email:
    print("Email Address Not Valid")
else:
    print("Valid Email")    


# 3. Write a program to check whether a password is weak, medium or strong.
# a. Weak: Password length is less than 6 characters.
# b. Medium: Password length is 6 to 10 characters and contains at least one number.
# c. Strong: Password length is 10 or more characters and contains at least one uppercase
# letter, one lowercase letter, and one special character (e.g., !, @, #, $).

password = "Jameeljoy@123"

print(len(password))

if len(password) < 6:
    print("Weak Password")
elif 6 <= len(password) <= 10: 
    print("Medium Password")   

elif len(password) >= 10:
    upper = False 
    lower = False 
    special = False 
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch in "!@#$":
            special = True
    if upper==True and lower==True and special==True:
        print("Strong Password")

    else:
        print("Medium password")    

# 4. Write a program to encrypt a message a message and print it?


# 5. Write a program to find frequency (count) of vowels and consonant into a string.

vowel = 0
consonent = 0
st = "jameeljoy"

for ch in st:
    if ch in "aeiouAEIOU":
        vowel+=1
    else:
        consonent+=1

print(f"Available Vowel in string : {vowel}")        
print(f"Available Consonent in string : {consonent}")   


# 6. Write a Python program Count all letters, digits, and special symbols from a given string.

letter = 0
digit = 0
specialSymbol = 0

st = "jamelll123@@"
for ch in st:
    if ch.isalpha():
        letter+=1
    elif ch.isdigit():
        digit+=1
    else:
        specialSymbol+=1
print(f"Letter : {letter}\nDigit : {digit}\nSpecial Symbol : {specialSymbol}")   


# 7. How can you remove all whitespace characters from a string?

#Ans. The replace() method can be used to remove spaces by replacing them with an empty string ("").


st = "jameel joy nc"

print(st.replace(" ",""))    


# 8. How can you concatenate two or more strings in Python?

# Using + operator

st1 = "Jameel"
st2 = "Joy"
print(st1+st2)

words = ["Hello", "World", "from", "Python"]
result = " ".join(words)
print(result)


# 9. How do you check if a string starts or ends with a specific substring?

#Ans. you can check if a string starts or ends with a specific substring using the string methods .startswith() and .endswith().

st = "I am Ok"
if st.startswith("I") and st.endswith("Ok"):
    print("Start With I and endwith Ok")
else:
    print("does not startwith I and does not endwith Ok")


# 10. How can you replace a substring in a string with another substring?

st = "My name is Jameel Joy"
print(st.replace("Jameel Joy", "Hasan"))


# 11. How can you check if a string contains only numeric digits?

# Ans. To check if a string contains only numeric digits in Python, you can use the .isdigit()

st = "12323"
st1 = "1a2b"
print(st.isdigit())
print(st1.isdigit())

# 12. How do you find the index of a particular substring in a string?

#Ans.The .find() method returns the lowest index of the substring if it is found, or -1 if it is not found.

st = "jameel"
print(st.index('e',4))
print(st.find('k'))

#13. What are escape characters in Python strings, and how are they used?

# #Ans. Escape Character	Description	Example Output
#       \'	    Single          quote	'Hello'
#       \"	    Double          quote	"Hello"
#       \\	    Backslash	    \
#       \n	    Newline	        Starts a new line
#       \t	Tab	Adds a horizontal tab
#       \r	Carriage return	Moves to line start
#       \b	Backspace	Deletes the previous character
#       \f	Form feed	Moves to the next page (less common)
#       \v	Vertical tab	Vertical whitespace
#       \0	Null character	Used in low-level strings
#       \xhh	Hexadecimal character (ASCII code)	\x48 → H
#       \uXXXX	Unicode character (16-bit)	\u03A9 → Ω
#       \UXXXXXXXX	Unicode character (32-bit)	\U0001F600 → 😀


# 14. How do you format strings using f-strings or format () method?

a = "5"
b = 6 

print(f"a = {a} | b = {b}")
print("a = {} | b = {}".format(a,b))


# 15. How do you remove leading and trailing whitespace from a string?

# Ans. Using Strip Function

st = "    Hello         "
print(st.strip())


# 16. What is the use of the join () method for strings in Python?

#Ans. The join() method is used to combine the elements of an iterable (e.g., list, tuple, set) into a single string, with each element separated by a specified string.

li = ['jameel','joy']
print(" ".join(li))


