class Student:
    def getData(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

# Creating object
s1 = Student()

# Calling instance methods
s1.getData("Amit", 20)
s1.display()