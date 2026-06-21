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




# Task 3: Keyword Arguments

def book_ticket(flight, passenger, date, seat="Economy"):
    print("-------------------")
    print(f"Flight No. {flight} \nPassenger : {passenger} \nDate; {date}\nSeat: {seat}")
    print("-------------------")

book_ticket("D03", 25, "15th June")
book_ticket(flight = "E02",passenger = 22 , date= "14th June", seat = "Business Class")
book_ticket("A03", 23, "17th June", seat = "PJ")




# Task 4: *args practice
#--1--
def multiply_all(*numbers):
    if len(numbers) == 0:
        return 0
    
    mul = 1
    for number in numbers:
        mul *= number
    return mul 

product = multiply_all()
print(product)

#--2--
def longest_word(*words):
    if not words: 
        return " "
    
    longest = words[0]
    for word in words: 
        if len(word) > len(longest):
            longest = word

    return longest

long = longest_word("avishek", "ranjan", "aeroplane", "ronaldo", "lakshman")
print(long)

#--3--
def average_grade(student_name, *grades):
    print("-----------")
    print(f"Namaste {student_name}.")
    total = 0 
    for grade in grades:
        total += grade
        avg = (total / len(grades))
    print(f"Your average grade is: {avg:2f}")
    print("------------")

average_grade("Steve", 85,65,90,72,63,88)



# Task 5: **kwargs practice 

#--1--
def build_profile(**infos):
    print("--------")
    print(f"Type : {type(infos)}")
    for key,value in infos.items():
        print(f"{key} : {value}")
    print("--------")
build_profile(name = "ram", age =30, city = "pokhara", profession = "teacher")
build_profile(name = "hari", age =32, city = "kathmandu", profession = "doctor")



# Task 6: Combined *args and **kwargs
def restaurant_order(waiter_name, *dishes, **speical_instruction):
    print("-------")
    print(f"Hello {waiter_name}!")
    print("I want to order: ")
    for dish in dishes:
        print(dish)
    print("where")
    for key, value in speical_instruction.items():
        print(f"{key} : {value}")
    print("------")

restaurant_order( "Jonathan", "Milk Tea","Sandwitch","Jhol MOMO","Pizza", tea = "No sugar",MOMO = "less sour", Pizza = "Extra Cheese" )
    



# Task 7: Multiple Return Values 

# ---1---
def statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum , maximum

total, average, minimum , maximum = statistics([25,45,5,2,8,4,1])
print(total)
print(average)
print(minimum)
print(maximum)

# --2--
def string_infos(s):
    length = len(s)
    first_character = s[0]
    last_character = s[-1]
    return length, first_character, last_character

length, first_character, last_character = string_infos("Aeroplane Flies High")
print(length)
print(first_character)
print(last_character)



# Task 8: Early return/guard clauses

#--1--
def safe_divide(a,b):
    if b == 0:
        return "Not Divisible by 0"
    
    div = a / b
    return div

division = safe_divide(10, 0)
print(division)

#--2--
def get_grade(score):
    if score < 0 or score > 100:
        return "INVALID!"
    
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
grade = get_grade(102)
print(grade )



# Task 9: Variable Scope 

total_calls = 0
def call_increment():
    global total_calls 
    total_calls += 1

call_increment()
call_increment()
call_increment()
call_increment()
call_increment()

print(total_calls)



# Task 10 : Calculator Formation

def calculator(a , b, operation):
    if operation == "add":
        return a + b
    elif operation == "substract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else: 
        return "INVALID OPERATION!"
    
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
op = input("Enter which operation you want to perform(add, substract, multiply , divide): ")

result = calculator(num1, num2, op)
print(f"The result of {op} is : \n{result}")



# Task 11 : Flexible Filter Function
def filter_students(**kwargs):
    students = [
        {"name": "avishek", "grade": "A", "age": 20, "city": "kathmnadu"},
        {"name": "krishna", "grade": "B", "age": 20, "city": "Hetuda"},
        {"name": "Ghanashyam", "grade": "A", "age": 20, "city": "Chitwan"},
        {"name": "Steve", "grade": "A", "age": 21, "city": "Dharan"},
    ]
    result = []
    for student in students: 
        match = True
        for key,value in kwargs.items():
            if student.get(key) != value:
                match = False
                break
            
            if match == True:
                result.append(student)

    return result

print(filter_students(grade = "A", age = 20))


# Task 12: Fucntion Documnetation 
def temperature_converter(value, to ="C"):
    """
    this function has two parameters
    one parameter takes value for conversion 
    and the other parameter specifies which conversion is needed to be done
    """
    if to == "C":
        return ((value-32)/1.8)
    elif to == "F":
        return ((value*1.8)+32)
    else:
        return "INVALDI CONVERSION!"
    
print(temperature_converter(30,"A"))


