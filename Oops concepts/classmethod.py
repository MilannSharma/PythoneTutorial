# 🧠 @classmethod kya hota hai?
# 🔹 Normal method kya karta hai?
# Ek normal method object (yaani instance) ke liye hota hai.


# class Student:
#     def show(self):
#         print("I am a student")
# 
# s1 = Student()
# s1.show()  # ✅ object bana ke call kiya


# 🔹 Lekin @classmethod class ke liye hota hai — bina object banaye bhi chalta hai.
# 🔧 Syntax:


# class ClassName:
#     @classmethod
#     def method_name(cls):
#         # code here
# 🔸 Yahan cls matlab "class" (jaise self object hota hai)

# ✅ Example 1: Simple class method

class School:
     school_name = "ABC School"

     @classmethod
     def get_school_name(cls):
         print("School ka naam:", cls.school_name)

School.get_school_name()  # ✅ bina object ke call ho gaya
#cls.school_name ka matlab: class ka variable use karna.

# 🤔 Difference between self vs cls?
# Term	Meaning	Used For
# self	object (instance)	normal methods
# cls	class (not object)	class methods

# ✅ Example 2: Class method se object banana (Alternative constructor)
# python
# Copy
# Edit
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string_data):
        name, age = string_data.split("-")
        return cls(name, int(age))

s1 = Student.from_string("Amit-22")
print(s1.name, s1.age)  
# 📌 Class method ne ek string ko tod kar object bana diya.

# 🔑 Summary:
# Feature	Explanation
# @classmethod	Method jo class par kaam karta hai
# Uses cls	cls ka matlab class ka reference
# Call without object	Yes! Direct class se call kar sakte ho
# Common use	Class variables access, object banane ke shortcut




#my code 

class Employee:

    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    

e = Employee()
e.a = 45 
e.show()
print(e.a)



