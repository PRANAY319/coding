class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40


p1 = student("x", 50)
p2 = student("y", 30)

if p1.is_passed():
    print(f"{p1.name} has passed")
else:
    print(f"{p1.name} has failed")

if p2.is_passed():
    print(f"{p2.name} has passed")
else:
    print(f"{p2.name} has failed")
