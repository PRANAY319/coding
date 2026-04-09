class Employee:
    bonus_rate = 0
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
        Employee.bonus_rate +=0.1
    def final_salary(self):
        final_salary= self.base_salary + (self.base_salary *self. bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.new_rate=Employee.bonus_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            print(10000)
        else:
            print(20000)

p1=Employee("xyz",1000)
print(p1.name)
print(Employee.is_valid_salary(10000))
p1.update_bonus(30000)
print(p1)







