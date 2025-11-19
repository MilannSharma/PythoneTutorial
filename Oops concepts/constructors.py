# ✅ What is a Constructor in Python?
# A constructor is a special method that automatically runs when you create (instantiate) an object of a class.

# In Python, the constructor method is named: __init__(self)

# 🧪 Example 1: Constructor without parameters
class Person1:
    def __init__(self):
        print("A new person is created!")

# Creating an object
p = Person1()  # Output: A new person is created!


# 🧠 Purpose of __init__():
# - Initialize values for each object
# - Create instance attributes like self.name, self.age, etc.


# 🔨 Example 2: Constructor with Parameters
class Person2:
    def __init__(self, name, age): #dunder method automatically calls
        self.name = name      # instance attribute
        self.age = age        # instance attribute

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object with data
p1 = Person2("Milan", 22) # Constructor runs here and sets name = "Milan" and age = 22
p1.show()  # Output: Name: Milan, Age: 22
