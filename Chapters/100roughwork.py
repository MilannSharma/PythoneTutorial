# friends = ["apple", "orange", 5, 345.06, False, "akash", "milan"]
 
# print(friends)


# friends.append("harry")

# print(friends)
# l1 = [1,34,62,2,6,11]
# print(l1)

# #l1.pop(3)
# #print(l1)

# print(l1.pop(3))
# print(l1)
# print(l1.pop(3))

marks = {
    "milan": 100,
    "rohan": 10,
    "shubham": 23,
}


print(marks)

print(type(marks))
print(marks["milan"])#aqccess via key milan 


print(marks.get("milan"))


marks.update({"milan" : 99})

print(marks.get("milan"))

marks.popitem()

marks.pop("milan")
print(marks)


if "rohan" in marks:
    print("rohan is present ")
if "milan" in marks:
    print("milan is present ")

else : print("milan is absent")

# make a dic copy for backup 

new_marks = marks.copy()

print(new_marks)

# clear all item from dic 

marks.clear()

print(marks)


# use for default keys while inital stage like sub ject = eng;ish  = 0 (beacuse koimarks chadaye nahi hai abhi tak )


sub = ["marathi","english","maths"]

default_marks = dict.fromkeys(sub , 0 )
print(default_marks)

sub = {"marathi " : 99, 
       "english" : 100,
       "maths" : 39
       }



print(marks)



age = 120
if age>=0:
    print("yes")


ls = [1 ,  7, 2]
for item in ls:
    print(item)

else:
    print("done")


     


for i in range (100):
    if(i==34):
        continue
    print("i = " ,i)






