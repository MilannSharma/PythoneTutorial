# file: calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This should only run when you execute calculator.py directly
if __name__ == "__main__":
    print("Running calculator tests...")
    a = int(input("Enter number A : "))
    b = int(input("Enter number B : "))
    print(add(a, b))
    print(subtract(a, b))