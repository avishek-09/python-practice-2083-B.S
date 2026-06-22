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


# Higher Order Function : that takes fuction as an argument and may also return a fuction 
def double(num):
    return 2 * num

def higher_order(func, value):
    return func(func(value))

result = higher_order(double, 5)
print(result)

# map(): an crazy higher order function

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

# Lamda Function 

numbers = [12,5,4,8,6,20,45,80]
new_list = list(map(lambda num : num*num, numbers))

print(numbers)
print(new_list)