# modules
import Greeting as g
import datetime

date = datetime.datetime.now() # this is the datetime module which is one of the built-in function of python
print(date)
print(g.hello_greet("Santosh Adhikari."))


# Task 1: Create and import your own module
import string_utils as V

vowels = V.count_vowels("a","b","d","e","p","q","s","t","u")
print(f"The number of vowels in the given strings are: {vowels}")

reverse = V.reverse_string("apple")
print(f"The reverse string is: {reverse}")

check_palindrome = V.is_palindrome("banana")
print(check_palindrome)


# Task 2: Explore standard library
# --1-- 
import math as M
print(M.sqrt(144))
print(3.14*M.sqrt(7))
print(M.gcd(48),M.gcd(18))

# --2--
import random as ran
 
for i in range(5):
    print(ran.randrange(1, 100), end= " ")
print()
names = ["ram", "hari", "gita", "sita", "joe", "steve"]
name = ran.choice(names)
ran.shuffle(names)
print(name)
print(names)



#------------------------------------------------------------------------------------------------------

# Higher Order Function : that takes fuction as an argument and may also return a fuction 
def double(num):
    return 2 * num

def higher_order(func, value):
    return func(func(value))

result = higher_order(double, 5)
print(result)


#---------------------------------------------------------------------------------------------------------------
# Lambda Function 

numbers = [12,5,4,8,6,20,45,80]
new_list = list(map(lambda num : num*num, numbers))

print(numbers)
print(new_list)



# # Task 3: Lambda Practice

positive_num = lambda num: num > 0
print(positive_num(-1))

last_ch = lambda string : string[-1]
print(last_ch("Avishek"))

max_num = lambda a , b : a if a > b else b
print(max(11 , 14))

vowels = lambda string : "First letter is vowel" if string[0].lower() in "aeiou" else "First letter isn't vowel" 
print(vowels("krish"))



## Task 4 : Lambda as Key in Sorting
# --1--
names = ["ram", "sita", "hari", "gita", "shyam"]
sorted_by_length = sorted(names, key = lambda name : len(name))
soted_by_lastchar = sorted(names, key = lambda name : name[-1])
sorted_by_no_of_vowels = sorted(names, key = lambda name: sum(1 for char in name.lower() if char in "aeiou"), reverse = True)
print(sorted_by_length)
print(soted_by_lastchar)
print(sorted_by_no_of_vowels)

#--2--
import math
points = [(1 , 2), (3 , 1), (5 , 0), (2 , 4)]
sort_by_ycoordinate = sorted(points, key = lambda point : point[1])
sort_by_distance = sorted(points, key = lambda point: math.sqrt(abs(point[0] ** 2 - point[1] ** 2)), reverse = True)
print(sort_by_distance)
print(sort_by_ycoordinate)


#--------------------------------------------------------------------------------------------------------------
# map():a crazy higher order function

def square(num):
    return num * num

numbers = [12,5,4,8,6,20,45,80]
new_list = list(map(square, numbers))

print(numbers)
print(new_list)

def reverse(string):
    reverse = ""
    for i in range(len(string)-1, -1, -1):
        reverse += string[i]
    
    return reverse

names = ["ram", "hari", "joe", "steve", "tom", "jerry"]
reverse_names = list(map(reverse, names))

print(names)
print(reverse_names)


# # Task 5 : map() with lambda

def if_greater(num):
    if num > 3:
        return True
    else: 
        return False
numbers = [1,2,3,4,5]
cube_list = list(map(lambda num: num*num*num, numbers))
string_list = list(map(lambda num: f"Number: {num}", numbers))
boolean_list = list(map(if_greater, numbers))
print(boolean_list)
print(string_list)
print(cube_list)

# Task  6 : map() with Multiple List

 #--1--
prices = [100, 200, 300]
quantities = [2, 3, 1]

def total_price(prices, quantities):
    return prices * quantities
    
new_list = list(map(total_price, prices, quantities))
print(new_list)

#--2--
test_one = [50,45,96]
test_two = [55,82,59]
test_three = [45, 86, 78]

def average(one, two, three):
    return (one+two+three)/3

average_list = list(map(average, test_one, test_two, test_three))
print(average_list)


#----------------------------------------------------------------------------------------------------------------
# FILTER

numbers = [12,5,4,8,6,20,45,80]
even_num = list(filter(lambda num : num%2 == 0, numbers))
print(numbers)
print(even_num)

# Task 7: filter() practice
import math 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False    
    return True
 
numbers = []
for i in range(1,51):
    numbers.append(i)
print(numbers)
divisible_by_3 = list(filter(lambda num : num % 3 == 0, numbers))
perfect_square = list(filter(lambda num : math.sqrt(num).is_integer(), numbers))
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)
print(perfect_square)
print(divisible_by_3)


# Task 8: filter() on string
words = ["apple", "", "banana", None, "cherry", "" , "date"]
remove_empty = list(filter(lambda word: word != "" and word is not None, words))
start_with_vowel = list(filter(lambda word : word is not None and word != "" and word[0] in "aeiou", words))
longer_than_5 = list(filter(lambda word: word is not None and word != "" and len(word) >= 5, words))
print(longer_than_5)
print(start_with_vowel)
print(remove_empty)

#-----------------------------------------------------------------------------------------------------------------
# Sorting 

numbers = [12,5,4,8,6,20,45,80]
sort_num = sorted(numbers, reverse = True)
print(numbers)
print(sort_num)

students = {
    "Avishek" : 50,
    "Steve" : 55,
    "Jhonatha" : 60,
    "Elon Musk" : 53,
}
sort_std = sorted(students, key=students.get, reverse = True )
print(students)
print(sort_std)

infos = [
    {"name": "avishek", "age" : 23},
    {"name": "shrawan", "age" :  30},
    {"name": "pawan", "age" : 25},
    {"name": "gajendra", "age" : 40},
]

sort_info1 = sorted(infos, key = lambda info : info.get("name"))
sort_info2 = sorted(infos, key = lambda info : info.get("age"))

print(infos)
print(sort_info1)
print(sort_info2)



# Task 9: custom sorting 

products = [
    {"name": "Laptop", "price": 80000, "rating": 4.5},
    {"name": "Phone", "price": 50000, "rating": 4.8},
    {"name": "Tablet", "price": 30000, "rating": 4.2},
    {"name": "Monitor", "price": 25000, "rating": 4.7}
]

by_price = sorted(products, key = lambda product : product.get("price"))
print(by_price)

by_rating = sorted(products, key = lambda product : product.get("rating"), reverse= True)
print(by_rating)

by_name = sorted(products, key = lambda product : product.get("name"))
print(by_name)



# Task 10: Complex Sorting 
sentences = [
    "Python is greate", 
    "I love codin",
    "hello world"
]
sort_by_no_of_words = sorted(sentences, key = lambda sentence: len(sentence))
sort_by_last_word = sorted(sentences, key = lambda sentence : sentence[-1])
print(sort_by_last_word)
print(sort_by_no_of_words)

students = [
    ("ram", 11, "A"),
    ("hari", 13, "A+"),
    ("gita", 15, "B+"),
]
grade_descending = sorted(students, key = lambda student : student[2], reverse = True)
name_alphabetical = sorted(students, key = lambda student : student[0])
age_ascending = sorted(students, key = lambda student: student[1])
print(name_alphabetical)
print(age_ascending)
print(grade_descending)


# #-------------------------------------------------------------------------------------------------------------------
# # Recursion: the function that calls itself 

def factorial(n):
    if n <=1:
        return 1
    
    return n * factorial(n-1)

num = int(input("Enter any number to calculate it's factorial : "))
fact = factorial(num)
print(f"The factorial of {num} is {fact}") 


# Task 14: Data Processing Pipeline

numbers = []
for i in range(1, 101):
    numbers.append(i)

pipeline_1 = list(filter(lambda num : num % 3 != 0 and num % 5 != 0, numbers))
pipeline_2 = list(map (lambda num: num*num, pipeline_1))
pipeline_3 = list(filter(lambda num: num > 1000, pipeline_2))
pipeline_4 = sorted(pipeline_3, reverse = True)
print(f"The initial list is : \n{numbers}")
print(f"The result for the first step in pipeline is : \n{pipeline_1}")
print(f"The result for the second step in pipeline is : \n{pipeline_2}")
print(f"The result for the third step in pipeline is : \n{pipeline_3}")
print(f"The result for the final step in pipeline is : \n{pipeline_4}")