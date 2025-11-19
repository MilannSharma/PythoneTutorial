# --------------------------------------------
# 🚦 Conditional Expressions in Python
# Types:
# 1. if
# 2. if-else
# 3. if-elif-else
# --------------------------------------------

# -----------------------
# Example 1: Simple if
# -----------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are allowed to access")

# -----------------------
# Example 2: if-else
# -----------------------
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are allowed to access")
else:
    print("You are not allowed")

# -----------------------
# Example 3: if-elif-else
# -----------------------
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are allowed to access")
elif age <= 0:
    print("You are not born yet, buddy!")
else:
    print("You are not allowed")




print("End of program")



# --------------------------------------------
# End of Examples
# --------------------------------------------
