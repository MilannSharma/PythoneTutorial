myList = [1,2,3,4,5,6,7,8,9]

squaredList = []

for item in myList:
    squaredList.append(item)


print(squaredList)



#comprehensions method 

squaredList = [i for i in myList]
print(squaredList)
