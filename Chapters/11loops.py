# # 🔁 Loops in Python

# # -----------------------------------
# # 📌 For Loop Example
# for i in range(0, 101):
#     print(i)

# # -----------------------------------
# # 📌 While Loop Example
# i = 0
# while i <= 50:
#     print(i)
#     i += 1

# # -----------------------------------
# # 📌 Print a name using while loop
# i = 0
# while i <= 5:
#     print("Milan")
#     i += 1

# # -----------------------------------
# # 📌 Print list elements using while loop
# l = [1, "Harry", False, "Milan", "this", "hello", "mf"]

# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# # -----------------------------------
# # 📌 Simple password check using while loop
# password = ""
# while password != "milan123":
#     password = input("Enter pass key: ")
    
# print("✅ Access granted")

# # -----------------------------------
# # 📌 Advanced password check (Max 5 attempts)
# correct_password = "milan123"
# attempts = 0

# while attempts < 5:
#     password = input("Enter pass key: ")
    
#     if password == correct_password:
#         print("✅ Access granted")
#         break
#     else:
#         print("❌ Incorrect password, try again.")
#         attempts += 1

# if attempts == 5:
#     print("🚫 Too many wrong attempts. Access denied.")

# # -----------------------------------
# # 📌 Sum of first N numbers using while
# n = int(input("Enter a number: "))
# i = 1
# total = 0

# while i <= n:
#     total += i
#     if total > 10:
#         print("Stopping early as total > 10")
#         break
#     i += 1

# print("Total:", total)



# # -----------------------------------
# # 🔁 For Loop Examples in Python

# # ✅ Basic For Loop: 0 se 3 tak print karega
# for i in range(4):
#     print(i)

# # -----------------------------------
# # ✅ Advanced For Loop with step size
# # range(start, stop, step)

# # Yahaan:
# # start = 1
# # stop = 101 (exclusive, i.e., 100 tak chalega)
# # step = 5 (har baar 5 se badhega)
# for i in range(1, 101, 5):
#     print(i)

# # -----------------------------------
# # 📘 Explanation (Hinglish):
# # i = 1 se shuru hoga
# # i < 101 tak chalega
# # i har baar 5 se badhega → 1, 6, 11, 16, ..., 96


# -------------------------------------
# ✅ For Loop in Different Data Types
# -------------------------------------

# 🔁 1. For loop in a List
lst = [1, 3, 5, 79, 545, 3]
for i in lst:
    print(i)

# 🔁 2. For loop in a Tuple
tpl = (6, 231, 75, 122)
for i in tpl:
    print(i)  # 👈 You forgot to write print()

# 🔁 3. For loop in a Dictionary (keys only)
dict = {
    "milan": 54,
    "sharma": 43
}
for i in dict:
    print(i)

# 🔁 4. For loop for both key and value
for key, value in dict.items():
    print(key, value)


# in character vise 

text = "milan"
for char in text:
    print(char)

#output
# m
# i
# l
# a
# n

#  Loop With range() + Index


fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Index {i} → {fruits[i]}")

#Loop With enumerate()

names = ["milan", "sharma", "raj"]

for index, name in enumerate(names):
    print(f"{index} → {name}")



# ✅ Example: for loop with else

l = [1, 7, 8, 9, 6]

for item in l:
    print(item)
else:
    print("✅ Done! Loop finished without break.")


#❌ With break → else will NOT run

l = [1, 7, 8, 9, 6]

for item in l:
    print(item)
    if item == 8:
        break
else:
    print("✅ Done!")  # This won't run because break was used


#📌 When To Use?
#Searching in a list: agar item mil gaya → break; agar nahi mila → else block.


# PASS , is null statement in python , its use to do nothing just skip the step 

# like 

for i in range(222):
    pass   # this pass will skip the for loop (just skip this step)

    i+=1

    while(i>=9):
        print(i)
        break