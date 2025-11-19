# this is simple method to print lst 
ls = [3,44,5,54,3,2,33,44,444]
index = 0 
for i in ls:
    print(f"The item no {index} is {i}")
    index +=1

# this is Enumrate func or method method

for index , item in enumerate(ls):
    print(f"this item number at index {index} is {item}")


