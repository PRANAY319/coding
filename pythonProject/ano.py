class Student:
    total_student=0
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_student +=1
    def result(self):
        if self.marks>=Student.passing_marks:
            print("Pass")
        else:
            print("fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def _category(marks):
        if marks>90:
            print("A")
        elif marks>85:
            print("B")
        else:
            print("c")

p1=Student("pranay",85)
Student.update_passing_marks(45)
print(Student.passing_marks)






