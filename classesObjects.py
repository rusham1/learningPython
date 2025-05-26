class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Your Name is: ", self.name)

s1 = Student("Archie")
s1.display()