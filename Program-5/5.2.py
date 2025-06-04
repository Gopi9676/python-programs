class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
def print_Student_info(Student):
    print(f"name:{Student.name},marks:{Student.marks}")
s1=Student("tillu",92)
print_Student_info(s1)
