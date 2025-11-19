# ✅ What is the Walrus Operator (:=) in Python?
# The Walrus Operator (:=) is used to assign values to variables as part of an expression.
# It was introduced in Python 3.8 and is also known as the Assignment Expression operator.

# 🧠 Syntax:
# variable := expression
# This assigns the result of 'expression' to 'variable' and also returns the value.

# 🔧 Why Use It?
# - Makes code more concise
# - Improves readability
# - Avoids redundant calculations or repeated function calls

# 🔍 Use Cases of Walrus Operator

# ✅ 1. While Loops — Read Input Until a Condition
# Traditional way
line = input("Enter something: ")
while line != "exit":
    print(f"You typed: {line}")
    line = input("Enter something: ")

# Walrus way
while (line := input("Enter something: ")) != "exit":
    print(f"You typed: {line}")
# ✅ Benefit: Removes duplicate input() call


# ✅ 2. Working with Length, Regex, or Function Calls
# Traditional way
data = [1, 2, 3, 4]
length = len(data)
if length > 2:
    print(f"List has {length} items")

# Walrus way
if (length := len(data)) > 2:
    print(f"List has {length} items")
# ✅ Benefit: No need to call len(data) twice or store beforehand


# ✅ 3. Inside List Comprehensions or Loops
words = ["apple", "hi", "banana", "ok"]
filtered = [word for word in words if (n := len(word)) > 3]
print(filtered)  # Output: ['apple', 'banana']
# ✅ Benefit: You can reuse 'n' later without re-computing len(word)


# 🚫 When Not to Use It:
# - If it makes the code hard to read
# - When assigning inside very complex expressions
# - If you're using Python version < 3.8


# 🧪 Final Example:
# Read numbers from user until 0 is entered and calculate the total
total = 0
while (num := int(input("Enter number (0 to stop): "))) != 0:
    total += num
print(f"Total is: {total}")




#my  code
#normal code 

line = input("Enter something: ")
while line != "exit":
    print(f"You typed: {line}")
    line = input("Enter something: ")




#walrus code

while (line := input("Enter Something :" )) != "exit" and line !="0" :
    print(f"you typed {line}")




    