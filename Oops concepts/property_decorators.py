class Employee:
    a = 1  # Class variable

    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname, self.lname = value.split(" ")  # 👈 No if check

# ----------------------
# ✅ Using the class now
# ----------------------

e = Employee()

# Instance variable 'a'
e.a = 45
print("Instance variable e.a:", e.a)  # 45 (object-level)

# Setting name properly (first + last name)
e.name = "milan sharma"
print("Full name using @property:", e.name)  # milan khan
print("First name:", e.fname)
print("Last name:", e.lname)

# Class method uses class variable 'a'
e.show()  # Output: The class value of a is 1
