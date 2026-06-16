# list, Tuple and Set Practice session 
# Task 1 : List Basic

movies = ["3 idiots", "inception", "shawsahank redemption", "shutter island", "fight club"]
movies.append("unko sweater")
movies.insert(2, "luck")
print(movies.pop())
print(movies.sort())


# Task 2: Tuple Practice

date = (2026, 0o6 , 15 )
for sep in date:
    print(sep)

dup_tuple = ("ram", "shyam", "hari", "gita", "ram" , "ram")
print(dup_tuple.count("ram"))

dup_tuple.insert(2,"joe")  #AttributeError: 'tuple' object has no attribute 'append'

age = (24,)
print(type(age))




# Task 3 : Set Operations

colors = {"red", "brown", "purple", "yellow", "white"}
# colors.update(["black","silver","yellow"])
# print(colors)
new_colors = {"black", "silver", "green", "blue", "red", "yellow"}

color = colors.union(new_colors)
color1 = colors.intersection(new_colors)
color2 = colors.difference(new_colors)

print(color)    
print(color1)   
print(color2)   

my_list = [7,3,7,1,3,9,3]
my_list = list(set(my_list))
print(my_list)

my_tuple = (2 , 3 , 6, 3, 5, 4, 2)
my_tuple = list(my_tuple)
print(my_tuple)




# Task 4 : Type conversion between List, Tuple and set 

my_list = [10,20,30,20,10,40]
my_list = list(tuple(my_list))
my_list = list(set(my_list))
my_list.sort()
print(my_list)




# Task 5: Real World Scenario

Scenario A: Days of a week is fixed so we need to use a non-mutable data structure. So, I am using Tuple
days_in_week = ("sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

for day in days_in_week:
    print(day) 

Scenario B: For storing unique registered email we need a data structure that is mutable and should remove duplicates. So, I am using Set
emails = {"avishek09@gmail.com", "ashmita08@gmail.com", "ram01@gmail,com", "avishek09@gmail.com"}

for email in emails:
    print(email)

Scenario C; To store students record that shouldn't be accidentally changes we use non mutable. So, I am usinf Tuple 

students = ("avishek", 20 , "A" )

try:
    students[1] = 21
except TypeError:
    print("students age cannot be modified!")

print (students)




# Task 6 : Challenge: Membership and iteration

my_list = [2,5,2,4,6,8,7,9]

for num in my_list:
    if num % 2 == 0:
        print(f"{num} is Even!")
    else:
        print(f"{num} is Odd!")

my_tuple = ("joe", "zayn", "harry", "krishna", "santosh")

name = input("Enter your name: ")

if name in my_tuple:
    print(": )")
else:
    print(": (")

vowels = ["a", "e", "i", "o", "u"]

letter = input("enter a letter of you choice: ")

if letter in vowels:
    print("That is a vowel you can use 'an' infront of it.")
else:
    print("Not a vowel.")