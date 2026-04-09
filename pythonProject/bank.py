class BankAccount:
    bank_name="xyz"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid amount")
    @classmethod
    def  change_bank_name(cls, new_name):
        cls.new_name = new_name
    @staticmethod
    def validate_amount(amount):
        return amount>0

a1 = BankAccount("Pranay", 5000)
a1.deposit(1000)

print("Bank holder:", BankAccount.bank_name)

BankAccount.change_bank_name("PQR Bank")

print("Bank name after change:", BankAccount)
