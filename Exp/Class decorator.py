def add_message(cls):
    class NewClass(cls):
        def display(self):
            print("Welcome!")
            super().display()
    return NewClass

class Student:
    def display(self):
        print("This is Student class.")

# Create object
s = Student()
s.display()
