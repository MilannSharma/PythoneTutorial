marks = []

for i in range(7):
    mark = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

print(f"marks list:", marks)
marks.sort() # alphabitacally sort
print(marks)


#sum of element in tuple 

l = [23 ,0,4,5,0,6,45,0,54,5]

print(sum(l))
n = l.count(0)
print(n)

print(l.count(0))


