a = 99 # global a
def fun():
    global a 
    a= 3 #local

    print(a)





print(a)#global

a = 89 #local
fun() 
print(a)
