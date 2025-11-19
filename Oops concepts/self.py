class Company:
    # Class attributes
    employe_name = "milan"
    employe_id = 1123
    employe_salary = 120000
    language = "Python"
    # Method to print employee info
    def getInfo(self):
        print(f" The ID is {self.employe_id}.\n The salary is {self.employe_salary}.\n The Language  is {self.language}.")

    # Method to greet the employee
    def greet(self):
        print(f"Good morning, {self.employe_name}!")

    @staticmethod
    def greet():
     print("Hello milan")

    

# Creating object 'milan'
milan = Company()

# Calling methods
milan.greet()
milan.getInfo()

milan.language = "javascript"
print( milan.employe_id , milan.language , milan.employe_salary , milan.employe_name)
Company.greet()
 