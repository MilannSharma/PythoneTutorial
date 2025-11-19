from functools import reduce 
# using format func 


name = input("Enter a name : ")
number = input("Enter a number : ")
marks = input("Enter a marks : ")


info = "The name is {} , his marks are  {} and phone number is {} ".format(name , marks , number)


print(info)


# join func

n = int(input("Enter a num : "))

table = [str(n*i) for i in range (1 , 11)]

s ="\n".join(table)
print(s)



#filter func 


def devisible5(n):
    if(n%5==0):
        return True
    return False


ls = [5,35,65,344,46,34345,34,45,34,355,45,34,35,46,54,7,5757,4]


fltr = list(filter(devisible5 , ls))
print(fltr)

#max of num 

from functools import reduce 

ls = [5,35,65,344,46,34345,34,45,34,355,45,34,35,46,54,7,5757,4]


def greter(a,b):
    if(a>b):
        return a
    return b


print(reduce(greter,ls))


