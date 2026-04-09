class Student:
    total_students=0
    passing_marks = 40

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.total_students +=1
    def result(self):
        if self.marks>= Student. passing_marks:
            print("pass")
        else:
            print("fail")
    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @classmethod
    def curve_marks(cls, students_list, percent):
        for stu in students_list:
            stu.marks = stu.marks + (stu.marks * percent / 100)

    @staticmethod
    def get_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "E"

s1 = Student("Pranay", 78)
s2 = Student("Ravi", 92)
s3 = Student("Kiran", 55)

# Total students
print("Total students:", Student.total_students)

# Pass/Fail
print(s1.name, "=>", s1.result())
print(s2.name, "=>", s2.result())

# Curve marks by +10%
Student.curve_marks([s1, s2, s3], 10)

print("Marks after curving:")
print(s1.name, s1.marks)
print(s2.name, s2.marks)
print(s3.name, s3.marks)

# Grades
print("Grade of", s2.name, ":", Student.get_grade(s2.marks))


