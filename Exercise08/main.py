#day06 - Dictionary and While loop 
# Task 1 : Create and access dictionary 

# phone_book = {
#     "ram" : 9812345675,
#     "hari" : 9845451245,
#     "shyam" : 9845157634,
#     "sita" : 9845824672,
#     "gita" : 9812345677,
# }

# print(phone_book.get("joe", "not found"))

# print(phone_book.keys())
# print(phone_book.values())



# Task 2: Modify Dictionary 

# phone_book["krishna"] = 9845721637
# phone_book.update({"sita" : 9812122212})
# print(phone_book.pop("shyam")) 
# phone_book.popitem()
# print(phone_book)



# Task 3: Dictionary Iteration 

# scores = {
#     "ram" : 85,
#     "sita" : 92,
#     "hari" : 78,
#     "gita" : 95,
#     "shyam" : 88,
# }

# highest_score = 0
# std = None
# for key,value in scores.items():
#     if value > highest_score:
#         highest_score = value
#         std = key
# print(f"{std} has height score of {highest_score}")

# total = sum(scores.values())
# avg = total / len(scores)
# print(f"The average score is {avg}")

# for key,value in scores.items():
#     if value > 85:
#         print(key)


# Task 4:  Nested Dcitrionary 
# students = {
#     "joe" : {
#         "age" : 11,
#         "marks" : [70, 80, 90],
#         "grade" : 7
#     },
#     "harry" : {
#         "age" : 12,
#         "marks" : [72, 83, 85],
#         "grade" : 7
#     },
#     "steve" : {
#         "age" : 11,
#         "marks" : [92, 95, 98],
#         "grade" : 7
#     }
    
# }

# for key,value in students.items():
#     total = sum(value.get("marks"))
#     percentage = (total/300)*100
#     print(f"-----'{key}'-----")
#     print(f"age: {value.get("age")}")
#     print(f"Obtained marks: {total}")
#     print(f"Grade: {value.get("grade")}")
#     print(f"Precentage : {percentage}%")
#     print("-----")

# Task 5 : word frequency Counter

# user_input = input("Enter repeated words of you choice:  ")

# word_list = user_input.split(" ")   ## this split() is a method of list which is used to split the sentence by specifying the seprater
# words= {}
# for word in word_list:
#     if not words.get(word):
#         words[word] = 1
#     else:
#         words[word] += 1
# print(words)

# While Loop Practice Session 

#Task 6: Countdown Timer
# import time
# user_input = int(input("Enter starting number for countdown: "))
# while user_input > 1:
#     user_input -= 1 
#     time.sleep(0.5)
#     print(user_input)
#     time.sleep(0.5)
# else:
#     print("🚀 Blast Off! ")

# Task 7: Password Login System 

# username = "admin"
# password = "admin123"

# attempt = 3 
# while True:
#     user_input = input("Enter password: ")
#     attempt -= 1
#     if attempt >= 0:
#         if user_input == password:
#             print("--Login Sucessfull!--")
#             break
#         else:
#             print(f"--Invalid Password. Yor have {attempt} attempts left.--")
#     else:
#         print("Account Blocked!!")
#         break

# Task 8 : Sum until zero 
sum = 0
while True:
    user_input= int(input("Enter a number for sum: "))
    if user_input != 0:
        sum += user_input 
    else:
        break

print(sum)