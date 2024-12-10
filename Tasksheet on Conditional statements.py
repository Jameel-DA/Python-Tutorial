# 1. Write a program that checks if a given number is positive. If it is positive, print 
# "Number is positive"; otherwise, print "Number is not positive." 

n = 6.9
if n > 0:
    print("Positive")
elif n == 0:
    print(n)
else:
    print("Negative")

# 2. Write a program that checks if a given number is even. If it is even, print "Number is 
#    even"; otherwise, print "Number is odd.

num = eval(input("Enter Number : "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# 3. Write a program that checks if a given number is divisible by both 2 and 3. If it is, 
# print "Number is divisible by 2 and 3"; otherwise, print "Number is not divisible by 
# both 2 and 3."

num = 12
if num % 2 == 0 and num % 3 == 0:
    print("Number is Divisible by 2 and 3")
else:
    print("Number is Not Divisible by 2 and 3")

# 4. Write a program that checks if a given year is a leap year. If it is a leap year, print "Year 
# is a leap year"; otherwise, print "Year is not a leap year." (Hint: A leap year is divisible 
# by 4 but not by 100, except if it is divisible by 400. 

lp = 2100
if (lp % 4 == 0) and (lp % 100 != 0 or lp % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 5. Write a program that calculates the grade based on a student's score. If the score is 
# above 90, print "Grade: A"; if it is between 80 and 90, print "Grade: B"; if it is between 
# 70 and 80, print "Grade: C"; if it is between 60 and 70, print "Grade: D"; otherwise, 
# print "Grade: F." 

grade = 80

if grade >= 90:
    print("A")

elif 80 <= grade < 90:
    print("B")

elif 70 <= grade < 80:
    print("C")

elif 60 <= grade < 70:
    print("D")

else:
    print("Fail")


# 6. Write a program that checks if a given string, is a palindrome. If it is, print "String is a 
# palindrome"; otherwise, print "String is not a palindrome." (Hint: A palindrome is a 
# word, phrase, number, or other sequence of characters that reads the same forward 
# and backward.) 

s = "ok"
s1 = "racecar"

if s == s[::-1]:
    print("String is Palindrom")
else:
    print("String is not Palindorom")


# 7. Write a program that checks if a given character, is a vowel. If it is a vowel, print 
# "Character is a vowel"; otherwise, print "Character is not a vowel." 

ch = 'n'
if ch in 'aeiouAEIOU':
    print("Vowel") 
else:
    print("Consonant")

# 8. Write a program that determines the largest of three given numbers. Print the largest 
# number. 

a = 10
b = 20
c = 5
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# 9. Write a program that checks if a given number, is a prime number. If it is a prime 
# number, print "Number is prime"; otherwise, print "Number is not prime." (Hint: A 
# prime number is a number greater than 1 that is divisible only by 1 and itself.)

n = 8
if n == 1:
    print("Number is not Prime")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Number is Not Prime")
            break
        i+=1 
    else:      
        print("Number is Prime") 

# 10. Write a program that determines the number of days in a given month. The 
# program should ask the user to input the month number (1 for January, 2 for 
# February, etc.) and print the number of days in that month. If an invalid month 
# number is entered, print "Invalid month number."

mon_num = int(input("Enter Your Month Number Between 1 To 12: "))

if mon_num == 1 or mon_num == 3 or mon_num == 5 or mon_num == 7 or mon_num == 8 or mon_num == 10 or mon_num == 12:
    print(f"31 Days in month {mon_num}")
elif mon_num == 4 or mon_num == 6 or mon_num == 9 or mon_num == 11:
    print(f"30 Days in month {mon_num}") 
elif mon_num == 2:
    print(f"28 days in month {mon_num}")
else:
    print("Invalid month number.")


# 11. Write a program that determines the cost of a movie ticket based on the age of the 
# person. If the age is 12 or below, the ticket cost is $5; if the age is between 13 and 
# 17 (inclusive), the ticket cost is $7; if the age is 18 or above, the ticket cost is $10.
            
age = eval(input("Enter Your Age : "))

if age <= 12:
    print("the ticket cost is $5")
elif 13 <= age <= 17:
    print("the ticket cost is $7")
else:
    print("the ticket cost is $10")

# 12. Write a program that determines the season based on a given month. If the month is 
# December, January, or February, print "Winter"; if it is March, April, or May, print 
# "Spring"; if it is June, July, or August, print "Summer"; if it is September, October, or 
# November, print "Autumn."

mon_name = input("Enter Your Month Name : ")

if mon_name in "December January February":
    print("Winter")
elif mon_name in "March April May":
    print("Spring")
elif mon_name in "June July August":
    print("Summer")
elif mon_name in "September October November":
    print("Autumn")
else:
    print("Enter Valid Month Name")

# 13. Write a program that determines the discount amount based on a customer's
# membership level. If the level is "Gold", apply a 20% discount; if it is "Silver", apply a
# 15% discount; if it is "Bronze", apply a 10% discount; otherwise, no discount is applied.

level = "Gold"

if level == 'Gold':
    print(r"20% discount")
elif level == 'Silver':
    print(r"15% discount")
else:
    print(r"15% discount")
    
# 14. Write a program that simulates a vending machine. Ask the user to enter the amount
# of money they have, and display a menu of items with their prices. Prompt the user
# to select an item by entering its corresponding number. If the user has enough
# money, deduct the price from their balance and display the item's name along with
# their remaining balance. If the user does not have enough money, display a message
# indicating the insufficient funds.    

print("""
Welcome to the Vending Machine!
Here are the available items:      
Enter 1 for Tv - ₹30000
Enter 2 for Cooler - ₹10000
Enter 3 for AC - ₹40000
Enter 4 for Mobile - ₹50000
""")

choice = input("select an item by entering its corresponding number : ")
amount = int(input("Enter the Amounmt : "))

if choice == '1' and amount >= 30000:
    print(f"You Can Buy This Item with price 30000 and Your Remaining Balance is {amount-30000}")

elif choice == '2' and amount >= 10000:
    print(f"You Can Buy This Item with price 10000 and Your Remaining Balance is {amount-10000}")

elif choice == '3' and amount >= 40000:
    print(f"You Can Buy This Item with price 40000 and Your Remaining Balance is {amount-40000}")

elif choice == '4' and amount >= 50000:
    print(f"You Can Buy This Item with price 50000 and Your Remaining Balance is {amount-50000}")
else:
    print("insufficient funds")

# 15. BMI Calculator
# Write a Python program that calculates a person's Body Mass Index (BMI) category based
# on their weight and height. The program should prompt the user to enter their weight in
# kilograms and their height in meters. It should then calculate the BMI using the formula:
# Once the BMI is calculated, the program should determine the BMI category based on the
# following ranges:
# • "Underweight" for BMI less than 18.5
# • "Normal weight" for BMI between 18.5 and 24.9
# • "Overweight" for BMI between 25 and 29.9
# • "Obesity" for BMI 30 or greater

weight,height = map(float,input("Enter weight in kilograms and height in meters : ").split())

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi}")    

if bmi < 18.5:
    print("Under weight")
elif 18.5 <= bmi <= 24.9:
    print("Normal Weight")
elif 25 <=bmi <= 29.9:
    print("Overweight")
else:
    print("Obesity")

# 16. Write a program that assists a customer in selecting a suitable mobile phone plan.
# Ask the user to enter the number of minutes they anticipate using per month and
# display the plan options: "Basic," "Standard," and "Premium." If the user enters less
# than 200 minutes, recommend the "Basic" plan. For 200-500 minutes, recommend the
# "Standard" plan. For more than 500 minutes, recommend the "Premium" plan.

minutes = int(input("Enter the Number of Minutes : "))

if minutes < 200:
    print("Basic Plan")
elif 200 <= minutes <= 500:
    print("Standard")
else:
    print("Premium Plan")

# 17. Write a program that calculates the shipping cost based on the weight and
# destination of a package. Ask the user to enter the weight in kilograms and the
# destination: "Domestic" or "International." For domestic shipping, charge $2 per
# kilogram. For international shipping, charge $5 per kilogram. Display the total
# shipping cost.

weight = int(input("Enter Your Weight in KG : "))
destination = input("Enter Your Destination : ")

if destination == "Domestic":
    print(f"Total Shipping Charge : ${weight*2}")
else:
    print(f"Total Shipping Charge : ${weight*5}")


# 18. Write a program that determines the eligibility of a person to apply for a driver's
# license based on their age and the type of license. Ask the user to enter their age and
# the type of license they are applying for: "Car" or "Motorcycle." If the age is 18 or
# above for a car license or 16 or above for a motorcycle license, print "Eligible to apply
# for a [license type] license"; otherwise, print "Not eligible to apply for a [license type]
# license."

age = int(input("Enter Your Age : "))
license_type = input("Enter Your License Type : ")
if age >= 18:
    print(f"Eligible to apply for a {license_type} license")
elif age >= 16 and license_type == "motorcycle":
    print(f"Eligible to apply for a {license_type} license")
else:
    print(f"Not eligible to apply for a {license_type} license.")


# 19. Write a program that helps a user choose the right clothing for the weather. Ask the
# user to enter the current temperature in Celsius. Based on the temperature, provide
# suggestions for clothing: if the temperature is below 10 degrees, suggest "Winter
# jacket, hat, and gloves"; if it is between 10 and 20 degrees, suggest "Sweater or light
# jacket"; if it is above 20 degrees, suggest "T-shirt and shorts."

temp = int(input("Enter the current temperature in Celsius : "))

if temp < 10:
    print("Winter Jacket, hat and gloves")

elif 10 <= temp <= 20:
    print("Sweater or Light jacket") 

else:
    print("T-shirt and shorts.")


# 20. Write a program that determines the discount amount for a customer's online
# purchase. Ask the user to enter the total order amount. If the order amount is above
# $100, apply a 20% discount; if it is between $50 and $100, apply a 10% discount; if it
# is below $50, apply a 5% discount. Print the discounted amount.

# Program to calculate the discount on an order

# Input: Total order amount
order_amount = float(input("Enter the total order amount: $"))

# Initialize discount rate
if order_amount > 100:
    discount_rate = 0.20
elif 50 <= order_amount <= 100:
    discount_rate = 0.10
else:
    discount_rate = 0.05

# Calculate discount amount
discount_amount = order_amount * discount_rate

# Calculate final amount after discount
final_amount = order_amount - discount_amount

# Output results
print(f"Order Amount: ${order_amount:.2f}")
print(f"Discount Applied: {discount_rate * 100}%")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Amount to Pay: ${final_amount:.2f}")
