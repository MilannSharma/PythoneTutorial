class Company:
    def set_name(self, name):  # renamed method
        self.name = name

    def show(self):
        print(f"Company name is {self.name}")

class Employee(Company):
    salary = 1343524
    increment = 20 

# Create objects
a = Company()
e = Employee()

# Set company name
e.set_name("Microsoft")

# Show and print
e.show()                 # Company name is Microsoft
print(e.salary)          # 1343524
