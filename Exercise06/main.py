# For_loop, Range and Membership Operators Practice session 

# Task 1: List Creation and Printing 

fruits = ["Apple", "Banana", "orange", "mango", "tomato"]
print(fruits)

print("---")
print(f"First Fruit: {fruits[0]}, Last Fruit: {fruits[-1]}")
print("---")

mixed = [25 , 19.5, "Ashmita", True]
print(mixed)




# Task 2: Membership Operators

students = ["ram","hari","krishna","sita","gita","shyam","binod"]
user_ip = input("Enter you name: ")
print("----------")
if user_ip in students:
    print("Student Found!")
else:
    print("Student Not Registered!")
print("----------")




# Task 3: Membership on String vs List

sentence = "apple banana mango orange"
fruit_name = input("Enter a friut name: ")

if fruit_name in sentence:
    print("Exist")
else:
    print("Not Found")

fruit_list = ["apple", "banana", "mango", "orange"]
if fruit_name in fruit_list:
    print("in the list")
else:
    print("not in the list")



# Task 4: range() Practice

five_multiple = []
for i in range(5,51,5):
    five_multiple.append(i)

print(five_multiple)




# Task 5: for loop patterns

for i in range(0,15):
    print("Python is Fun!")

for i in range(10,0,-1):
    print(i)

for i in range(1, 11):
    j =  i*i
    print(f"{i} squared = {j}", end =" , ")



# Task 6 

nums = [10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 ]

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print(f"{nums[i]} is even!")
    else:
        print(f"{nums[i]} is odd!")

another_num = int(input("Enter any number: "))
if another_num in nums: 
    print("this number exist in the list.")
else:
    print("this numbers don't exist in the list")