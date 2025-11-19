# Function to find the greatest of three numbers
def greatest(a, b, c):
    if a > b and a > c:
        return "A is greater than B & C"
    elif b > a and b > c:
        return "B is greater than A & C"
    elif c > a and c > b:
        return "C is greater than A & B"
    else:
        return "There is a tie among the numbers"

# Taking user input
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

# Function call
greatest_result = greatest(a, b, c)  

# Displaying the result
print(f"The GOAT is: {greatest_result}")


