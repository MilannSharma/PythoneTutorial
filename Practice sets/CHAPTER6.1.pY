#find a greterst of a phone number 

g1 = int (input("Enter a number : "))
g2 = int (input("Enter a number : "))
g3 = int (input("Enter a number : "))
g4 = int (input("Enter a number : "))

if g1 > g2 and g1 > g3 and g1 > g4:
    print("Student 1 has the highest marks:", g1)
elif g2 > g1 and g2 > g3 and g2 > g4:
    print("Student 2 has the highest marks:", g2)
elif g3 > g1 and g3 > g2 and g3 > g4:
    print("Student 3 has the highest marks:", g3)
else:
    print("Student 4 has the highest marks:", g4)

    #or

if g1 > g2 and g1 > g3 and g1 > g4:
    print("Student 1 has highest:", g1)
elif g2 > g3 and g2 > g4:
    print("Student 2 has highest:", g2)
elif g3 > g4:
    print("Student 3 has highest:", g3)
else:
    print("Student 4 has highest:", g4)