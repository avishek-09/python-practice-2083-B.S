# _____________________FILE HANDLING____________________________
 #---Write Method in File handling---
with open("random.txt", "w") as file:
    file.write("Hello There! I am file handling.\n")
    file.write("Hello python! I am having fun.")

## ---writing from a Loop------
with open("random.txt", "w") as file:
    for random in ["Avishek", "ram", "hari", "ashmita", "shyam"]:
        file.write(random + "\n")

##---Append Method in File handling---
with open("random.txt", "a") as file:
    file.write("\nI am an Engineering graduate studing python.")

##---Read Method in File handling---
with open("random.txt", "r") as file:
    print(file.read())

#----Read line in the file using loop----
with open("random.txt", "r") as file:
    for line in file: 
        print(line)


#---------------------------------------
# Q.no.1 : Student Registration System
with open("students.txt", "w") as file:
    num = int(input("Enter how many entries you want to make: "))
    for i in range(num):
        name = input("enter you name: ")
        roll_no = input("enter your roll no: ")
        course = input("enter which couese you want to enroll(Physics, Biology, Mangement): ")
        
        file.write(f"{name}, {roll_no}, {course}\n")


#---------------------------------------
#Q.no 2: Daily Expense Logger
with open("expenses.txt", "w") as file: 
    num = int(input("Enter No. of Expences you want to enter: "))
    for i in range(num):
        description = input("Enter the description: ")
        amount = input("Enter the amount: ")

        file.write(f"Description: {description}, Amount: Rs.{amount}\n")
 

#---------------------------------------
# Q.no.3: Read Student Record
with open("students.txt", "r") as file:
    print(file.read())


#---------------------------------------
# Q.no.4: Count lines in file
count = 0 
with open("expenses.txt", "r") as file: 
    for line in file:
        count += 1
    print(count)


#---------------------------------------
# Q.no.5 Seaarch in Log File 
with open("log.txt", "w") as file:
    file.write("ERROR: Disk full\nINFO:Backup completed\nERROR: Connection Timeout\nWARNING: Low memory")

with open("log.txt", "r") as file:
    keyword = input("Enter a keyword you want to search in log.txt file: ").lower()
    for line in file: 
        if keyword in line: 
            print(line)


#----------------------------------------
# Q.no.6 Add New Students
with open("students.txt", "a") as file:
    name = input("enter your name: ")
    roll_no = input("enter your roll_no: ")
    course = input("enter course(physics, biology, management)")
    file.write(f"{name}, {roll_no}, {course}")


#-----------------------------------------
# Q.no. 7: Attendence Tracker
with open("attendence.txt", "w") as file:
    file.write("Date: 25th January | Present: Ram, Hari, Shyam")

with open("attendence.txt", "a") as file: 
    date = input("Enter the date: ")
    present_student = input("Names of present student: ")
    
    file.write(f"\n Date: {date} | Present: {present_student}")




#_______________________C S V____________________________
import csv
with open("students.csv", "w", newline = "") as file: 
    writer = csv.writer(file)
    writer.writerow(["Roll" , "Name", "Course", "Marks"])
    writer.writerow([101, "Ram"])
    writer.writerow([102, "Hari"])

with open("students.csv", "a", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow([103, "Sita"])

search_id = input("Enter ID: ")
with open("students.csv", "r") as file: 
    reader = csv.reader(file)
    for row in reader: 
        if row[0] == search_id:
            print(row)

#------------------------------
# Q.no. 1: Student Record Management

import csv
MENU = """
1. Add Student record
2. View all student records
3. Search by Roll Number
4. exit
"""
while True: 
    print(MENU)
    user_choice = input("Enter your choice(1,2,3): ")
    if user_choice == "1":
        with open("students.csv", "a", newline = "") as file:
            roll_no = input("Enter Roll No: ") 
            name = input("Enter name: ")
            course = input("Enter course: ")
            marks = input("Enter Marks: ")
            writer = csv.writer(file)
            writer.writerow([roll_no, name, course, marks])
    elif user_choice == "2":
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader: 
                print(row)
    elif user_choice == "3": 
        keyword = input("Enter the Roll No of student whose data you need: ")
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == keyword: 
                    print(row)
    elif user_choice == "4":
        break
