'''. Create an Employee class that:
•	Keeps a minimum experience required for promotion (shared across all employees).
•	Stores employee name, experience, and department.
•	Has a method to check eligibility for promotion.
•	Provides a function to update promotion criteria globally.
•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
1.	Creating employees from different departments.
2.	Changing promotion criteria.
3.	Displaying eligibility results and department validation.'''

class Employee:
    min_experience= 3
    valid_departments = ["HR", "Tech", "Admin"]

    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def check(self):
        return self.experience >=self.experience >= Employee.min_experience
    @classmethod
    def update(cls,new_min_experience):
        cls.min_experience=new_min_experience
    @staticmethod
    def is_valid(dep):
        return dep  in Employee. valid_departments

e1 = Employee("Alice", 2, "HR")
e2 = Employee("Bob", 4, "Tech")
e3 = Employee("Charlie", 1, "Admin")

employees = [e1, e2, e3]



# Check department validity
print(Employee.is_valid("Finance"))   # False
print(Employee.is_valid("Tech"))




