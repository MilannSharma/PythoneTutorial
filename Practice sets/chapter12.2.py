lt = [1,2,3,4,5,6,7,8,9]

index = 0 

for index , item in enumerate(lt):
    if index == 3 or  index == 5 or index == 7:
     print(f"Item number {index} and item is {item}")

    



# prob 3 

n = int(input("enter a num to priint table : "))

table = [n*i for i in range(1,11)]
print(table)

#prob 4 

try:
   a = int(input("enter a num to priint : "))
   b = int(input("enter a num to priint : "))
   print(a/b)
except ZeroDivisionError as v :
   print("infinite")

   



#store the multiplication tgable in file table 


with open ("table.txt","w")as f:
     (f.write("table doc \n"))

n = int(input("enter a num to priint table : "))
table = [n*i for i in range(1,11)]
with open ("table.txt","a")as f:
 f.write(str(f" Table of {n} is : {table} \n"))


print("done")
