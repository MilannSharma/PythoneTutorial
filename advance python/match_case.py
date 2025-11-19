# ✅ What is match in Python?
# The match statement is Python's version of switch-case logic, introduced in Python 3.10.
# It uses pattern matching to compare values and run specific code blocks based on the pattern.

# 🧠 Syntax:
# match variable:
#     case pattern1:
#         # do something
#     case pattern2:
#         # do something else
#     case _:
#         # default case


# 🔥 Basic Example
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Paused.")
    case _:
        print("Unknown command")


# 📦 Example with Numbers
x = 3

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else")


# 🧰 Use Cases

# ✅ 1. Matching Multiple Values
animal = "dog"

match animal:
    case "dog" | "puppy":
        print("It's a dog!")
    case "cat":
        print("It's a cat!")
    case _:
        print("Unknown animal")


# ✅ 2. Matching with Conditions (if)
age = 25

match age:
    case x if x < 18:
        print("Minor")
    case x if x >= 18 and x < 60:
        print("Adult")
    case _:
        print("Senior")


# ✅ 3. Matching Data Structures (Tuples, Lists)
point = (0, 2)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at y={y}")
    case (x, 0):
        print(f"X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")


# ✅ 4. Matching Dictionaries with Classes
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Milan", 22)

match user:
    case User(name="Milan", age=22):
        print("Hello Milan!")
    case User(name=name, age=age):
        print(f"Hello {name}, age {age}")
    case _:
        print("Unknown user")


# ✅ 5. Destructuring Lists
values = [1, 2, 3]

match values:
    case [1, 2, 3]:
        print("Matched exact list")
    case [1, *rest]:
        print(f"Starts with 1, rest: {rest}")
    case _:
        print("No match")


# 🚫 When Not to Use It
# ❌ In versions before Python 3.10
# ❌ For simple if-else when pattern matching is overkill




#my code



