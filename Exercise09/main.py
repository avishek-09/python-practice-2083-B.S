# --------functions in python----------- 
# parameter
# arguemnt 
# positional argument  :: means some defualt value rahkdini in parameter defination 
# keyword argument     :: not positional i.e. keyword sanga define garney with argument so position doesn't matter
# default argument     :: means giving a default value to the parameter so that if we don't pass an argument it will show that default value 

def function(name , age):
    print(f"Hello {name}!")
    print(f"I heard you are {age} years old")

function("avishek" ,23 )


#----- a simple send email program to understnad mutiple arguments in the fuction -----------

def send_email(to , subject, body= None, cc=None, bcc= None, priority= "Normal"):
    print(f"To: {to} \nSubject: {subject} \nBody: {body} \ncc: {cc} \nbcc: {bcc} \npriority: {priority}")

send_email(
    to = "Ram",
    subject = "Files attaced..",
    body = "This email contains the documents of the previous meeting that we had last week.",
    priority="High"
)


# ---------- Understanding *args and **kargs to use in function 

def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

sum (10,5,4,2,10,56,85,74,525,45,12,5)

def profile(**infos):
    for key,value in infos.items():
        print(f"{key} -> {value}")
              
profile(name = "Avishek", age = 20, address = "kathmandu", occupation = "python developer")

def random(name, *numbers, **infos):
    print(f"Hey {name}!")
    print("---The numbers are:")
    for number in numbers:
        print(number)
    print()
    for key,value in infos.items():
        print(f"{key} : {value}")

random("avishek", 10,20,30,40,50, age = 23, address = "Kathmandu", grade = "A+")


#------return statement in the function-----------

def factorial(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1
    return fact

number = int(input("Enter any number to calculate factorail: "))     
result = factorial(number)
print(f"The factorial is {result}")



# Task 1: Simple Fuction with return 
#--1--
def square(n):
    result = n * n
    return result

result1 = square(3)
result2 = square(4)
result3 = square(8)

print(result1)
print(result2)
print(result3)

#--2--
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Enter any number: "))
check = is_even(num)
print(check)

#--3--
def greet_user(name):
    return f"Namaste, {name}!"

user = greet_user("avishek")
print(user)

#--4--
def rectangle_area(l, w):
    return l * w

area = rectangle_area(2,3)
print(area) 



# Task 2: Default Parameters
#--1--
def power(base, exponent = 2):
    return base ** exponent

P = power(6,4)
print(P)

# --2--
def create_greeting(name, greeting = "Hello", punctuation = "!"):
    return f"{greeting} {name} {punctuation}"

greet = create_greeting("Ram")
print(greet)

#--3--
def calculate_tax( amount, tax_rate = 0.13):
    tax = amount * tax_rate
    total = amount + tax
    return tax, total 

tax, total  = calculate_tax(12000)
print(f"Tax : {tax} \nTotal pay : {total}")