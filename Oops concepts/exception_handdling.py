#exception handdling 



try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")
except Exception as e:
    print(f"Error: {e}")

print("Done!")




#option 2


try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")

except ValueError:
    print("Please enter a valid number!")

print("Thank you")



#for more error 

try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")

except ValueError:
    print("Please enter a valid number!")

except Exception as e :
    print(e)

except TypeError as t :
    print(t)

# much more excption handdle here !!



print("Thank you")


