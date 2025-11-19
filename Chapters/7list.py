# ----------------------------------------
# 📦 LISTS IN PYTHON
# ----------------------------------------

# ✅ A list is a **collection of values** stored in a single variable.
# ✅ Lists can hold **different data types** (strings, numbers, booleans, etc.)
# ✅ Lists are **mutable**, meaning we can change, add, or remove elements.
# ✅ List indexing starts from 0.
# ✅ Lists are flexible — we can insert or delete elements from anywhere.

# Example List:
friends = ["apple", "orange", 5, 345.06, False, "akash", "milan"]

# ----------------------------------------
# 🔢 INDEXING
# ----------------------------------------

print(friends[0])     # Output: 'apple'

# Changing the value at index 0
friends[0] = "grapes"
print(friends[0])     # Output: 'grapes'

# ----------------------------------------
# ✂️ SLICING
# ----------------------------------------

# Syntax: list[start_index : end_index]
# Includes start_index, excludes end_index
print(friends[0:4])   # Output: ['grapes', 'orange', 5, 345.06]

# ----------------------------------------
# ⚠️ STRING vs LIST BEHAVIOR
# ----------------------------------------

# ❗ Strings are immutable:
#    Any method creates a **new** string
# ✅ Lists are mutable:
#    Most methods modify the **original** list directly

# ----------------------------------------
# 🛠️ COMMON LIST METHODS
# ----------------------------------------

numbers = [1, 2, 3, 4, 5]

# ✅ .append(value) → Adds element to the end
numbers.append(6)
print(numbers)        # Output: [1, 2, 3, 4, 5, 6]

# ✅ .insert(index, value) → Adds element at specific index
numbers.insert(2, 99) # list.insert(index, value)
# 2-> where to insert , 99 -> what  to insert 
print(numbers)        # Output: [1, 2, 99, 3, 4, 5, 6]

# ✅ .extend(iterable) → Adds elements from another list (or iterable)
numbers.extend([10, 11])
print(numbers)        # Output: [1, 2, 99, 3, 4, 5, 6, 10, 11]

# ✅ .remove(value) → Removes first occurrence of value
numbers.remove(99)
print(numbers)        # Output: [1, 2, 3, 4, 5, 6, 10, 11]

# ✅ .pop(index) → Removes and returns value at index (default: last)
last = numbers.pop()
#list.pop()              # Removes the last item
#list.pop(index)         # Removes the item at the given index

print(last)           # Output: 11
print(numbers)        # Output: [1, 2, 3, 4, 5, 6, 10]

# ✅ .clear() → Removes all elements
# numbers.clear()
# print(numbers)      # Output: []

# ✅ .sort() → Sorts list in ascending order (modifies original)
nums = [5, 2, 9, 1]
nums.sort()
print(nums)           # Output: [1, 2, 5, 9]

# ✅ .reverse() → Reverses the list
nums.reverse()
print(nums)           # Output: [9, 5, 2, 1]

# ✅ .copy() → Returns a new copy of the list
copy_nums = nums.copy()
print(copy_nums)      # Output: [9, 5, 2, 1]

# ✅ .count(value) → Counts how many times value appears
print(nums.count(5))  # Output: 1

# ✅ .index(value) → Returns index of first occurrence
print(nums.index(2))  # Output: 2

# ----------------------------------------
# 🧠 NOTE:
# - List methods like `append()`, `insert()`, `extend()`, `sort()` modify the **original list**
# - String methods return a **new string**
