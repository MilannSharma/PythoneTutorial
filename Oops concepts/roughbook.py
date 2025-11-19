class Subject:
    sub_name = "Hindi"
    subject_marks = 100

    @classmethod
    def show(cls):
        print(f"This is subject name : {cls.sub_name}")
        print(f"Marks Contain Subject : {cls.subject_marks}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname, self.lname = value.split(" ")  # 👈 No if check


# ✅ Object banate hain
s = Subject()

# ✅ Set full name using property setter
s.name = "Hindi Subject"

# ✅ Create instance variables
s.subject_marks = 45


# ✅ Print name
print("Full Name:", s.fname, s.lname)

# ✅ Class method still shows class variables, not instance
s.show()












