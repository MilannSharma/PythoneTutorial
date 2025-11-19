from random import randint
import random

class Programmer:
    company = "Microsoft"
    def __init__(self , name , pincode, salary):
        self.name = name
        self.pincode = pincode
        self.salary = salary




employee = Programmer("milan" , 1234 , 200000)

print(employee.name , employee.salary , employee.pincode)




# claculator 


class Calculator:
    def __init__(self , n):
        self.n = n

    def square(self):
         print(f"the square of {self.n} is {self.n*self.n}")

    def square_root(self):
        print(f"the Square root of {self.n} is {self.n**1/2}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
#Q.4 using static in q 3 
    @staticmethod
    def hello():
        print("hello there!")


a = Calculator(4)

a.square()
a.square_root()
a.cube()

a.hello()


# does the classs atribute change ?

class demo:
    a= 4


o = demo()
print(o.a)#print class attribute


o.a = 0 # set instance atrribute 


print(o.a)#print instance  attribute
print(demo.a) #class atrribute will print 


#ans NOOO just value will be chnage atrribute will not its remain smae 


class Train:

    def __init__(self , train_no):
        self.train_no = train_no

    def book(self, where , to , username ):
        print(f"{username} Ticket is booked in train no : {self.train_no} from {where} to {to}")
        

    def getStatus(self ):
        print(f"{self.train_no} running on time ")


    def getFare(self , where , to):
        print(f"Ticket is booked in train no : {self.train_no} from {where} to {to} is {random.randint(299,99999)}")




t = Train(68322)
t.book("rampur" , "pune" , "milan")
t.getStatus()
t.getFare("rampur" , "pune")










