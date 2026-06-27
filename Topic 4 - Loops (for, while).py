# # Topic 4: Loops (for, while)
#------------------------------------------------------------

# Q1. 1 से 10 तक Print करें।


for i in range(1, 11):
    print(i)

# #------------------------------------------------------------

# # Q2. 1 से 20 तक Even Numbers Print करें।


# for i in range(2, 21, 2):
#     print(i)

# #------------------------------------------------------------

# # Q3. 1 से 20 तक Odd Numbers Print करें।


# for i in range(1, 21, 2):
#     print(i)

# #------------------------------------------------------------

# ## Q4. अपना नाम 5 बार Print करें।


# for i in range(5):
#     print("Rahul")


# #------------------------------------------------------------

# ## Q5. 10 से 1 तक Reverse Counting।


# for i in range(10, 0, -1):
#     print(i)


# #------------------------------------------------------------


# ## Q6. Number Table Print करें।


# num = 5

# for i in range(1, 11):
#     print(num * i)

# #------------------------------------------------------------

# ## Q7. while Loop से 1 से 10 तक Print करें।


# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# #------------------------------------------------------------

# ## Q8. 1 से 100 तक Numbers Print करें।


# for i in range(1, 101):
#     print(i)


# #------------------------------------------------------------


# ## Q9. 5 बार Hello Print करें।


# i = 1

# while i <= 5:
#     print("Hello")
#     i += 1


# #------------------------------------------------------------

# ## Q10. 1 से 50 तक Multiples of 5 Print करें।


# for i in range(5, 51, 5):
#     print(i)

# #------------------------------------------------------------



# # Q1. 1 से 100 तक Sum निकालें।


# total = 0

# for i in range(1, 101):
#     total += i

# print(total)

# #------------------------------------------------------------


# # Q2. User Input Number का Table Print करें।


# num = int(input("Enter Number: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

# #------------------------------------------------------------

# ## Q3. Factorial निकालें।


# num = int(input())

# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(fact)


# #------------------------------------------------------------

# # Q4. Count Digits in Number


# num = int(input())

# count = 0

# while num > 0:
#     count += 1
#     num //= 10

# print(count)

# #------------------------------------------------------------

# ## Q5. Reverse a Number


# num = int(input())

# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# print(rev)

# #------------------------------------------------------------

# ## Q6. Sum of Digits


# num = int(input())

# s = 0

# while num > 0:
#     s += num % 10
#     num //= 10

# print(s)

# ## Q7. Fibonacci Series (10 Terms)

# #------------------------------------------------------------
# a, b = 0, 1

# for i in range(10):
#     print(a)
#     a, b = b, a + b


# #------------------------------------------------------------

# ## Q8. Multiplication Tables (1 to 5)


# for num in range(1, 6):
#     print(f"\nTable of {num}")

#     for i in range(1, 11):
#         print(num * i)

# #------------------------------------------------------------

# ## Q9. Check Prime Number


# num = int(input())

# is_prime = True

# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break

# if is_prime and num > 1:
#     print("Prime")
# else:
#     print("Not Prime")


# #------------------------------------------------------------

# ## Q10. Count Even Numbers from 1 to 100


# count = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         count += 1

# print(count)


#------------------------------------------------------------










# # Q1. Armstrong Number Check


# num = int(input())

# temp = num
# digits = len(str(num))

# sum_val = 0

# while temp > 0:
#     digit = temp % 10
#     sum_val += digit ** digits
#     temp //= 10

# if sum_val == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# #------------------------------------------------------------



# ## Q2. Palindrome Number


# num = int(input())

# original = num
# reverse = 0

# while num > 0:
#     reverse = reverse * 10 + num % 10
#     num //= 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# #------------------------------------------------------------

# ## Q3. Print All Prime Numbers from 1 to 100



# for num in range(2, 101):

#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num)


# #------------------------------------------------------------

# ## Q4. Pattern Printing



# for i in range(1, 6):
#     print("*" * i)


# #------------------------------------------------------------

# ## Q5. Inverted Pattern


# for i in range(5, 0, -1):
#     print("*" * i)

# #------------------------------------------------------------




# ## Q6. Multiplication Table 1 to 10


# for num in range(1, 11):

#     print(f"\nTable of {num}")

#     for i in range(1, 11):
#         print(num * i)



# #------------------------------------------------------------



# ## Q7. Perfect Number Check


# num = int(input())

# sum_div = 0

# for i in range(1, num):
#     if num % i == 0:
#         sum_div += i

# if sum_div == num:
#     print("Perfect Number")
# else:
#     print("Not Perfect")




# #------------------------------------------------------------


# ## Q8. GCD (Greatest Common Divisor)

# a = int(input())
# b = int(input())

# while b:
#     a, b = b, a % b

# print(a)



# #------------------------------------------------------------



# ## Q9. LCM Find करें


# a = int(input())
# b = int(input())

# greater = max(a, b)

# while True:
#     if greater % a == 0 and greater % b == 0:
#         print(greater)
#         break

#     greater += 1


# #------------------------------------------------------------



## Q10. Guess the Number Game

# secret = 7

# while True:

#     guess = int(input("Guess: "))

#     if guess == secret:
#         print("Correct")
#         break

#     print("Try Again")


# #------------------------------------------------------------


'''
# Practice Questions (Homework)

1. Strong Number Check
2. Neon Number Check
3. Spy Number Check
4. Magic Number Check
5. Duck Number Check
6. Harshad Number Check
7. Pyramid Pattern
8. Diamond Pattern
9. Pascal Triangle
10. Floyd Triangle

'''