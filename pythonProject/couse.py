class Course:
    total_student=0
    def __init__(self,student_name):
        self.student_name=student_name

    def enroll(self):
        Course.total_student += 1
        print(f"{self.student_name} enrolled successfully")
    @classmethod
    def _total(cls):
        print("Total students enrolled:", cls.total_student)
    @staticmethod
    def is_eligible(age):
        return  age>=18

s1 = Course("Ravi")
s2 = Course("Meena")
s3 = Course("Arjun")


print("Is Ravi eligible?", Course.is_eligible(20))
print("Is Meena eligible?", Course.is_eligible(17))

# Enroll students
s1.enroll()
s2.enroll()
s3.enroll()

#
Course._total()





