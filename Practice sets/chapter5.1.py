# dic = {

# "madaat" :"help",
# "pani" : "water",
# "ghee" : "butter"

# }

 
# word = input("Enter the word: ").lower()

# if word in dic:
#     print(dic[word])
# else:
#     print("Sorry, word not found in dictionary.")


# #input 8 number from user and display unique number 

# numbers = []

# for i in range(1, 6):
#     num = int(input("Enter a number: "))
#     numbers.append(num)  # Add number to list

# print("Your list is:", numbers)


# s = set()

# for i in range (1, 6):
#     num = int(input("Enter a num"))
#     s.add(num)




# print("your set is " ,s)

# s.clear()

# print(s)


set = {"18" , 18}

set.add(19)
set.add("91")


print(set)

print(len(set))


dic = {}

# taking input 

for i in range (1, 4):

     name = input("enter frinds name : ")
     lang = input("enter lang name : ")
     dic.update({name : lang})




print(dic)




dic["milan"] = "u"
print(dic)



