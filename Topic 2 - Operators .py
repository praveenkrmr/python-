'''

print(" Q1. store two numbers and print it's sum ?")

a = 10
b = 20
print(a + b)
print() #for enter blank  line

#------------------------------------------------------------

print("Q2. store ur name in Name variable and print it?")
name = "Praveen kumar mishra"
print(name)
print() #for enter blank  line


#------------------------------------------------------------


print("Q3. Check type") # Q15 me length find ka hai 

x = 100
print(type(x))
print() #for enter blank  line


#------------------------------------------------------------


print("Q4. Create Float variable") 
price = 99.99
print(price)
print() #for enter blank  line



#------------------------------------------------------------


print("Q5. Create Boolean variable")
is_student = True
print(is_student)
print() #for enter blank  line


#------------------------------------------------------------


print("Q6. Print String and Integer")
name = "Praveen"
age = 31
print(name, age)
print() #for enter blank  line


#------------------------------------------------------------

print("Q7. Input from User?")
name = input("Enter name: ")
age = int(input("Enter age: "))
print(age)
print(name)
print() #for enter blank  line


#------------------------------------------------------------

print("Q8. swap two variables ")
a = 5
b = 10

a, b = b, a

print(a, b)
print() #for enter blank  line

#------------------------------------------------------------

print("Q9. convert Celsius to Fahrenheit")
c = int(input("enter Celsius between 0 to 100 :-  "))
f = (c * 9/5) + 32
print(f)
print() #for enter blank  line
#------------------------------------------------------------


print("Q10. Find area of square")
n = int(input("enter side of square :-  "))
print(n*n)
print() #for enter blank  line
#------------------------------------------------------------


print("Q11. Find area of Circle")
r = int(input("enter radius of circle :-  "))
area = 3.14 * r * r
print(area)
print() #for enter blank  line
#------------------------------------------------------------
 

print("Q12. Average of 3 number")

a,b,c = 10,20,30
avg = (a+b+c)/3
print(avg)
print() #for enter blank  line

#------------------------------------------------------------


print("Q13. Average of 3 number by uning input")

a= int(input("enter the value of a or first no. :-  "))
b=int(input("enter the value of b or second no. :-  "))
c= int(input("enter the value of c or third no. :-  "))

avg = (a+b+c)/3
print(avg)
print() #for enter blank  line
#------------------------------------------------------------



print("Q14. convert Seconds to minutes  by uning input")

seconds = int(input("enter second :-  "))
minutes = seconds / 60
print(seconds,"seconds is = ",minutes,"minutes")
print() #for enter blank  line


#------------------------------------------------------------

print("Q15. to find String length")  #Q03. me type find ka hai 

name = "Python"
print(len(name))
print() #for enter blank  line

#------------------------------------------------------------

print("Q16. 15% increment in salary")  

salary = int(input("what is ur current salary:-  "))
salary += salary * 0.15
print("After 15% increment in your salary , ur salary will be",salary)
print() #for enter blank  line

#------------------------------------------------------------

print("Q17. odd even number")  
n = int(input("Enter number :-  "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
print() #for enter blank  line


#------------------------------------------------------------

print("Q18. Convert KM TO M")  
km = int(input("Enter km :-  "))
print(km,"KM =",km * 1000,"M")

print() #for enter blank  line





#------------------------------------------------------------

print("Q19. to convert Integer to String  ")
x = 100
y = str(x)
print(type(y))
print() #for enter blank  line





#------------------------------------------------------------

print("Q20. Dynamic type conversion ")  

value = "123"
value = int(value)
print(value + 10)

print() #for enter blank  line




#------------------------------------------------------------

print("Q21. Multiple assignment")  
a,b,c = 10,20,30
print(a,b,c)

print() #for enter blank  line


#------------------------------------------------------------

print("Q22. Complex number")  
x = 2 + 3j
print(type(x))
print() #for enter blank  line





#------------------------------------------------------------

print("Q23. Memory address ")  
x = 10
print(id(x))
print() #for enter blank  line





#------------------------------------------------------------

print("Q24. Type casting ")  
x = float(10)
print(x)
print() #for enter blank  line


#------------------------------------------------------------

print("Q25. User input sum ")  
a = int(input())
b = int(input())
print(a+b)
print() #for enter blank  line



#------------------------------------------------------------

print("Q26. Binary representation")  
x = 10
print(bin(x))
print() #for enter blank  line


#------------------------------------------------------------




print("Q27. Hexadecimal representation")
x = 255
print(hex(x))  

print() #for enter blank  line



#------------------------------------------------------------

print("Q28. Unicode value")  
print(ord('A'))

print() #for enter blank  line



'''


#------------------------------------------------------------

print("Q29. Character from Unicode")  
print(chr(65))
print() #for enter blank  line




#------------------------------------------------------------