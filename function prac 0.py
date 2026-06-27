
'''
FUNCTION 

Types of Function Arguments
1. Required arguments (Single/Multiple arguments) 
2. Default argument 
3. Keyword arguments (named arguments) 
4. Arbitrary arguments (variable-length arguments *args and **kwargs) 


'''

#1. Required arguments (Single/Multiple arguments)
print ("SCENARIO - 1")
def greating():
    print ("hello praveen")

greating()

print()
print ("SCENARIO - 2")
def greating(name):
    print ("hello",name)

greating("jittu")


print()
print ("SCENARIO - 3")
def greating(name,city):
    print ("hello",name,"are u from ",city)

greating("jittu","bihar")

print()
print ("SCENARIO - 4")
def greating(name,city,skill):
    print ("hello",name,", are u from ",city,"?\n""u have a knowledge about",skill)

greating("jittu","bihar","python")



#---------------------------------------------------------

'''
2. Default argument:-
Default Argument- here (country="India") is a default argument
'''

def person(name, country="India"):
    print(name, country)

person("jittu")
person("John", "USA")
person("nandan")
person("edward","UK")


#---------------------------------------------------------

'''

3. Keyword arguments (named arguments)
'''

def divide(a, b):   # a,b are 2 parameters 
    return a / b

result1 = divide(10, 20)    # positional arguments
result2 = divide(b=10, a=20)  # with keyword arguments 

print ("SCENARIO - 1")
print(result1)    
     

print()

print ("SCENARIO - 2")   
print(result2)    
   


 #---------------------------------------------------------

'''
4. Arbitrary arguments 
(variable-length arguments *args and **kwargs)


Arbitrary Positional Arguments (*args) :-  
1. If you're unsure how many arguments will be passed, 
use *args to accept any number of positional arguments.  

2. Purpose: Allows you to pass a variable number of positional 
arguments. 

3. Type: The arguments are stored as a tuple. 

4. Usage: Use when you want to pass multiple values 
that are accessed by position.  
'''


def add_numbers(*args):  # Any number of arguments 
    return sum(args) 

result = add_numbers(1, 2, 3, 4)  
print("sum is ",result) # Output: 10
# Here, *args collects all the passed arguments into a tuple, 
# & sum() function adds them.


def greetings(*names): 
    print("Hello, ",names,"!") 
greetings("Madhav", "Rishabh", "Visakha")

print ()


def greetings(*names): 
    for name in names:
        print("Hello, ",name,"!") 
greetings("Ram","jittu", "atul", "praveen")


#---------------------------------------------------------


'''
using **kwargs insert details of Student 
'''

def details(**data):
    print(data)

details(name="jittu", age=31, )

details(name="praveen", age=31, city="Patna" )

details(name="atul", age=28, city="darbhanga", state="bihar" )


def details(**kwargs):
    for iteam,price in kwargs.items():
        print(iteam,":",price)

details(iteam="apple" , price=100 )
details(iteam="mango" , price=120 , city="Patna" )
details(iteam="orange" , price=50 ,city="darbhanga", state="bihar" )














#---------------------------------------------------------

'''


'''











#---------------------------------------------------------

'''


'''








#---------------------------------------------------------

'''


'''










#---------------------------------------------------------

'''


'''










#---------------------------------------------------------

'''


'''








#---------------------------------------------------------

'''

'''
