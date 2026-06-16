# #if_else statement practice session
# # Task 1: Simple Calulator 

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# op = input("Choose the operator(= , -, *, /): ")

# print("------")
# if op == "+":
#     print(f"Sum is {num1 + num2}")
# elif op == "-":
#     print(f"Substract is {num1 - num2}")
# elif op == "*":
#     print(f"Product is {num1 * num2}")
# elif op == "/":
#     if num2 == 0:
#         print("Math Error!")
#     else: 
#         print(f"Division is {num1 / num2}")
# else:
#     print("INVALID CHOICE!") 
# print("------")   




# # Task 2: WAP to checke even or odd

# user_ip = int(input("Enter the number you want to check wheather even or odd: "))
# print("----------")
# if user_ip % 2 == 0:
#     print("EVEN :) ")
# else:
#     print("ODD :)")
# print("----------")



# # Task 3: Find the largest among the three numbers

# num1 = float(input("Enter a = "))
# num2 = float(input("Enter b = "))
# num3 = float(input("Enter c = "))

# print("-----------")
# if num1>num2 and num2>num3: 
#     print("a is largest")
# elif num2>num1 and num1>num3: 
#     print("b is largest")
# else: 
#     print("c is largest")
# print("-----------")


# Task 4: Grade Calculator

# result = int (input("Enter your marks(1- 100): "))

# print("----------")
# if result >= 90 and result <=100:
#     print("Your Scored A+ grade.")
# elif result >= 80 and result <=90:
#     print("Your Scored A grade.")
# elif result >= 70 and result <=80:
#     print("Your Scored B+ grade.")
# elif result >= 60 and result <=70:
#     print("Your Scored B grade.")
# elif result >= 50 and result <=60:
#     print("Your Scored A grade.")
# elif result >= 40 and result <=50:
#     print("Your Scored A grade.")
# elif result < 40:
#     print("No Grade")
# else:
#     print("INVALID RESULT !")
# print("----------")



# # Task 5: BMI Calculator

# weight = float(input("Enter weight in kg : "))
# height = float(input("Enter height in metres: "))
# bmi = weight / (height ** 2)
# print(f"Your BMI is {bmi:.2f}")
# if bmi < 18.5:
#     print("Category: Underweight")
# elif bmi < 25:
#     print("Category: Normal weight")
# elif bmi < 30:
#     print("Category: Overweight")
# else:
#     print("Category: Obese")



# # Task 6: Eletricity Bill Calculator 

# unit_consumed = float(input("Enter the total units consumed: "))

# if unit_consumed <= 100:
#     Total = unit_consumed * 5
# elif unit_consumed > 100 and unit_consumed<300:
#     Total = 100*5 + (unit_consumed-100) * 7
# elif unit_consumed>= 300:
#     Total = 100*5 + 200*7 + (unit_consumed-300) * 10

# print("-----")
# print(f"You have consumed {unit_consumed} units. So you total is Rs.{Total}")
# print("-----")




# # Task 7: Positive Negative or Zero 

# print("Check for posistve Negative or zero ??")
# num = int(input("Enter a number:"))
# print("----------")
# if num > 0 :
#     print("POSITIVE!")
# elif num == 0 :
#     print("ZERO!")
# else:
#     print("NEGATIVE!")
# print("----------")



# # Task 8: Leap Year Checker 

# print("Leap Year Checker?")
# year = int(input("Enter Year: "))

# print("------")
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print("LEAP YEAR!")
# else:
#     print("NOT A LEAP YEAR!") 
# print("------")
