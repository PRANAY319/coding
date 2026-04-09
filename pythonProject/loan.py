'''. Build a Loan class that:
•	Has a common interest rate for all loans.
•	Each object stores borrower name and principal.
•	Calculates total payable amount.
•	Provides a function to update the interest rate.
•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
1.	Creating multiple loan accounts.
2.	Updating interest rates.
3.	Checking eligibility and total repayment for borrowers'''

class Loan:
    interest_rate=0.02
    def __init__(self,name,principal):
        self.name=name
        self.principal =principal
    def total_payable(self,interest):
        interest =(self.principal*Loan.interest_rate)
        return self.principal+interest
    @classmethod
    def update(cls,new_rate):
        cls.interest_rate=new_rate
    @staticmethod
    def is_check(salary):
        return salary>30000

p1=Loan("xyz",50000)
p2=Loan("pqr",100000)
print("p1 Total Payable:", p1.total_payable('interest'))
print("p2 Total Payable:", p2.total_payable('interest'
                                            ''))
Loan.update(new_rate=0.05)
print(Loan.update(p1.total_payable()))

print(Loan.is_check(40000))









