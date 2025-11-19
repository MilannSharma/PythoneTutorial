# -------------------------------------
# Functions Basics: Definition & Usage
# -------------------------------------

# 1. Function to calculate the average of two numbers
def average_of_num(a, b):
    return (a + b) / 2  # Corrected: average of 2 numbers

# Taking user input
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# Calling the function and storing the result
average = average_of_num(num1, num2)

# Displaying the result
print(f"This is your average of the numbers: {average}")


# -------------------------------------
# Quick Quiz: Greeting Program
# -------------------------------------

# 2. Function to greet the user
def greet_user(name):
    print(f"Hey {name}, hope you're having a great day!")

# Taking user's name as input
user_name = input("Enter your name: ")

# Calling the greeting function
greet_user(user_name)


# -------------------------------------
# Function Types:
# 1. User-defined functions (like above)
# 2. Built-in functions (e.g., print(), input(), int())
# -------------------------------------


# -------------------------------------
# Default Parameters in Functions
# -------------------------------------

# Example 1: Providing a value to the default parameter
def greet_user(name, ending="thanks"):
    print(f"Hey {name}, hope you're having a great day!")
    print(ending)

# Taking user's name as input
user_name = input("Enter your name: ")

# Calling the function with a custom ending
greet_user(user_name, "thank you")


# Example 2: Not providing a value to the default parameter
def greet_user(name, ending="thanks"):
    print(f"Hey {name}, hope you're having a great day!")
    print(ending)

# Taking user's name as input
user_name = input("Enter your name: ")

# Calling the function without passing 'ending', so default is used
greet_user(user_name)
