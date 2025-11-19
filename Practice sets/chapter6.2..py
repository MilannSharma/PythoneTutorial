maths = int(input("Enter maths marks: "))
Geo = int(input("Enter geo marks: "))
java = int(input("Enter java marks: "))

# Check for total percentage
total_percentage = (maths + Geo + java) / 300 * 100

if maths < 33 or Geo < 33 or java < 33:
    print("You are failed due to marks less than 33 in a subject.")
elif total_percentage < 40:
    print("You are failed due to total percentage less than 40%.")
else:
    print("Congrats! You are passed 🎉")
