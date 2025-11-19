name = " Milan  Sharma "

# Detect first double space
print("First double space at index:", name.find("  "))

# Detect first single space
print("First single space at index:", name.find(" "))

# Count spaces
singlespace_count = name.count(" ")
doublespace_count = name.count("  ")

print(f"The number of single spaces is {singlespace_count},\nand double spaces is {doublespace_count}")

# Remove extra spaces (cleans multiple spaces to single spaces)
cleaned = ' '.join(name.split())
print("Cleaned string:", cleaned)

# ❌ Typo in method name: 'replce' → ✅ Correct is 'replace'
print(name.replace("  ", " "))  # Creates a new string with double spaces replaced by single space

# Original string remains unchanged (because strings are immutable in Python)
print("Original string remains unchanged:", name)

# Format letter using escape characters
letter = "Dear Milan,\n\tThis Python course is nice.\nThanks"
print("\nFormatted letter:\n")
print(letter)
