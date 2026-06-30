# Objest Oriented Programming in Python 

class Student: 
    def __init__(self, name, address, marks): ##Consturctor , ## Method
        self.name = name
        self.address = address
        self.marks = marks  ##public
        self._marks = marks ## protected
        self.__marks = marks ## private
    
    # Concept of --GETTER-- : which is a method to get the value of a private data from a class which cannot be accessed inside the class
    @property               ## here this decorator property makes marks as a attribute rather than a method so while callingit would be easy
    def marks(self):
        return self.__marks
    
    # concept of --SETTER-- : which is a method to set/change the value of a private data from a class which cannot be accessed inside the class
    def set_marks(self, marks):
        self.__marks.append(marks)

    def average(self): ## Method 
        average = sum(self.marks)/len(self.marks)
        return average
    
    def show_student(self):
        average = self.average()
        return f"Name : {self.name}\nAddress : {self.address}\nAverage : {average}"

s1 = Student("Hari", "Kathmandu", [98, 82, 84, 90, 75])
s2 = Student("Shyam", "Pokhara", [82, 82, 95, 75, 50])

print(f"The average of {s1.name} is {s1.average()}")
print(s1.show_student())
print(s2.show_student())


print(s1.marks)
s1.set_marks(90)
print(s1.marks)