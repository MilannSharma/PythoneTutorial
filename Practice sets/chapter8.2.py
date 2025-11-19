# sum of first n natruall numvers ka

'''

sum(1) =1
sum(2) = 1+2
sum(3)= 1+2+3
.
.
.
.
.
sum(n)= 1+2+3+4+5+6+....+n

sum(n) = sum(n-1) + n
n * (n + 1) // 2 


'''


def sum(n):
    if (n==1 or n==0):
        return 1
    return n * (n + 1) // 2  



n = int(input("Enter a number n: "))


total = sum(n)
print(f"The sum of first {n} natural numbers is: {total}")



#patern printing 

def pattern(n):

    if(n==0):
        return 1
    print("*"*n)
    pattern(n-1)
    return "done"





n = int(input("Enter a number : "))

print(pattern(n))


def pattern(n, current=1):
    if current > n:
        return
    print("*" * current)
    pattern(n, current + 1)

n = int(input("Enter a number: "))
pattern(n)




