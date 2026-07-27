class Number:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")

# Calling the static method using class name
Number.check_even_odd(12)

# Creating an object
obj = Number()

# Calling the static method using object
obj.check_even_odd(17)