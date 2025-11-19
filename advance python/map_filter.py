from functools import reduce




#map 
# 
ls = [1,2,3,4,5,6,7,8]

squaredList= lambda x: x*x

sqList = map(squaredList , ls)
print(list(sqList))



# filter 

def even(n):
    if (n%2==0):
        return True
    
    return False


onlyEven = filter(even ,ls)
print(list(onlyEven))


#reduce func 


def Sum(a, b):
    return a + b

x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
nums = [x, y]

result = reduce(Sum, nums)
print("Sum using named function:", result)


# ex 2

x = int(input("Enter a num1: "))
y = int(input("Enter a num2: "))

# Create a list of the two numbers
nums = [x, y]

# Use reduce to sum them
result = reduce(lambda a, b: a + b, nums)

print("The sum is:", result)
