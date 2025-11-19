# What is __name__?
# __name__ is a built-in special variable in Python.

# It holds a string value:

# If the script is being run directly, __name__ == "__main__"

# If the script is being imported, __name__ == "module_name"

# ✅ Why use if __name__ == "__main__"?
# It prevents code from running when the module is imported somewhere else.

# 🧠 Think of it like:
# "Only run this block of code if you’re running this file directly. Don’t run it if it’s being imported."


# Common Uses:
# Testing code inside a file

# Avoid running unnecessary code when importing

# Structuring large applications



def myFunc():
    print("hello world")


myFunc()

print(__name__)


if __name__ == "__main__":

    #if this code directly exicuted by running the file its present in

    print("we are run code directly")
    myFunc()
    print(__name__)



