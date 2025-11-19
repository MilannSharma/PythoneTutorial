with open ("table.txt","w")as f:
     (f.write("table doc \n"))

n = int(input("enter a num to priint table : "))
table = [n*i for i in range(1,11)]
with open ("table.txt","a")as f:
 f.write(str(f" Table of {n} is : {table} \n"))


print("done")
