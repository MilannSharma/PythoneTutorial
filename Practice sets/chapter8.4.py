
def rem(ls,word):
    
    for item in ls:
        ls.remove(word)
        return ls
    

ls = ["harry", "rohan" , "milan" , "rn"]

print(rem(ls,"rn"))



def rem(ls, word):
    result = []
    for item in ls:
        if item != word:  # Keep only items that are not equal to the word
            result.append(item)
    return result

# Example list
ls = ["harry", "rohan", "milan", "rn"]

# Call the function and print the result
print(rem(ls, "rn"))

