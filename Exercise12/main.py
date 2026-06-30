## Objest Oriented Programming in Python 

class Student: 
    def __init__(self, name, address, marks): ##Consturctor , ## Method
        self.name = name
        self.address = address
        self.marks = marks 
    
    def average(self): ## Method 
        average = sum(self.marks)/len(self.marks)
        return average
    
    def show_student(self):
        average = self.average()
        return f"Name : {self.name}\nAddress : {self.address}\nAverage : {average}"

s1 = Student("Hari", "Kathmandu", [98, 82, 84, 90, 75])
s2 = Student("Shyam", "Pokhara", [82, 82, 95, 75, 50])

# print(f"The average of {s1.name} is {s1.average()}")
print(s1.show_student())
print(s2.show_student())