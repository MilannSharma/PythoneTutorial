username = input("Enter a name : ")

if(len(username)< 10):
    print("Username Not Valid ,Try again !")

else:
    print("username created succesfully ")



l = ["Harry", "milan", "shubam", "divya"]
name = input("Enter a name: ")

if name in l:
    print("Try another name")
else:
    print("Username created successfully")
    l.append(name)  # Correct way to add to list

print("Updated list:", l)



marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    grade = "EX"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 60 and marks < 70:
    grade = "C"
elif marks >= 50 and marks < 60:
    grade = "D"
elif marks >= 0 and marks < 50:
    grade = "f"
    print("you are faild")
else:
    grade = "Invalid marks"
    
print("Your grade is:", grade)

