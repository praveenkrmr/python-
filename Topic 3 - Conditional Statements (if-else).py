#Python Conditional Statements (if, elif, else)
'''
print(" Q1. Number Positive है या नहीं?")

num = int(input("Enter number: "))

if num > 0:
    print("Positive Number")


print() #for enter blank  line

#------------------------------------------------------------
print("Q2. Number Negative है या नहीं? ")
num = int(input())

if num < 0:
    print("Negative Number")


print() #for enter blank  line


#------------------------------------------------------------

print("Q3. Number Zero है या नहीं?")
num = int(input())

if num == 0:
    print("Zero") 




print() #for enter blank  line
#------------------------------------------------------------
print("Q4. Even Number Check करें ") 

num = int(input())

if num % 2 == 0:
    print("Even")


print() #for enter blank  line



#------------------------------------------------------------
print("Q5. Odd Number Check करें")
num = int(input())

if num % 2 != 0:
    print("Odd")

print() #for enter blank  line


#------------------------------------------------------------

print("Q6. Age 18 से बड़ी है या नहीं")

age = int(input())

if age >= 18:
    print("Adult")

print() #for enter blank  line


#------------------------------------------------------------

print("Q7.Marks Pass हैं या नहीं? (33 या अधिक)")

marks = int(input())

if marks >= 33:
    print("Pass")

print() #for enter blank  line


#------------------------------------------------------------

print("Q8. Number 100 से बड़ा है या नहीं? ")

num = int(input())

if num > 100:
    print("Greater than 100")

print() #for enter blank  line

#------------------------------------------------------------
print("Q9.  Salary 50000 से अधिक है")

salary = int(input())

if salary > 50000:
    print("High Salary")

print() #for enter blank  line
#------------------------------------------------------------

print("Q10. Character vowel है या नहीं? ")

ch = input("Enter character: ")

if ch in "aeiouAEIOU":
    print("Vowel")


print() #for enter blank  line
#------------------------------------------------------------



print("Q11. Positive, Negative या Zero ")

num = int(input())

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print() #for enter blank  line
#------------------------------------------------------------

print("Q12. Pass / Fail ")

marks = int(input())

if marks >= 33:
    print("Pass")
else:
    print("Fail")

print() #for enter blank  line

#------------------------------------------------------------



print("Q13. Voting Eligibility ")
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


print() #for enter blank  line


#------------------------------------------------------------

print("Q14.  Largest of Two Numbers ")

a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)
print() #for enter blank  line


#------------------------------------------------------------



print("Q15. Leap Year Check ")  

year = int(input())

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")


print() #for enter blank  line

#------------------------------------------------------------

print("Q16. Divisible by 5 ")  

num = int(input())

if num % 5 == 0:
    print("Divisible")
else:
    print("Not Divisible")

print() #for enter blank  line

#------------------------------------------------------------

print("Q17. Grade Calculator ")  

marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")


print() #for enter blank  line


#------------------------------------------------------------

print("Q18. Largest of Three Numbers ")  

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

print() #for enter blank  line





#------------------------------------------------------------


print("Q19. Check Number in Range   ")

num = int(input())

if 1 <= num <= 100:
    print("In Range")
else:
    print("Out of Range")

print() #for enter blank  line





#------------------------------------------------------------

print("Q20. Password Validation ")  
password = input()

if password == "python123":
    print("Login Success")
else:
    print("Wrong Password")



print() #for enter blank  line




#------------------------------------------------------------

print("Q21. Nested If Example")  

age = int(input())

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")


print() #for enter blank  line


#------------------------------------------------------------

print("Q22. BMI Calculator")  

weight = float(input("Weight: "))
height = float(input("Height: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

print() #for enter blank  line





#------------------------------------------------------------
print("Q23. Electricity Bill Category")  

units = int(input())

if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
else:
    print("High Usage")

print() #for enter blank  line





#------------------------------------------------------------


print("Q24.  Calculator Using if-elif")  

a = int(input())
op = input()
b = int(input())

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid Operator")

print() #for enter blank  line


#------------------------------------------------------------
print("Q25. Triangle Validity Check ")  

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

print() #for enter blank  line

#------------------------------------------------------------
print("Q26.Character Type Check")  
ch = input()

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")


print() #for enter blank  line


#------------------------------------------------------------

print("Q27. Login System")

username = input()
password = input()

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")
print() #for enter blank  line



#------------------------------------------------------------

print("Q28. ATM Withdrawal Check")  

balance = 5000
amount = int(input())

if amount <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")


print() #for enter blank  line





#------------------------------------------------------------


print("Q29. Year Century Check")  

year = int(input())

if year % 100 == 0:
    print("Century Year")
else:
    print("Not Century Year")

print() #for enter blank  line





#------------------------------------------------------------

print("Q30. Discount Calculator")  
amount = float(input())

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

print("Final Amount =", amount - discount)


print() #for enter blank  line





#------------------------------------------------------------

Practice Assignment :- 
ATM Machine Program
Student Grade Management System
Railway Ticket Fare Calculator
Income Tax Calculator
Mobile Recharge Offer Checker
Online Shopping Discount System
Bank Loan Eligibility Checker
Hotel Room Booking Cost Calculator
Employee Bonus Calculator
Voting System Simulation

'''