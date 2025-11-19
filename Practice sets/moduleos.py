import os

path = "E:/Python Cource/Practice sets"

# Method 1: Using os.listdir()
content = os.listdir(path)
for item in content:
    print(item)

# Method 2: Using os.scandir()
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print("File:", entry.name)
        elif entry.is_dir():
            print("Directory:", entry.name)
