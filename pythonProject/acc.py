'''Create a BankAccount class that stores:
• account number
• balance (should not be directly modifiable)
You must:
1. Make the balance attribute inaccessible from outside.
2. Provide functions to deposit/withdraw that validate the amount.
3. Prevent withdrawal if balance becomes negative.
4. Show what happens if someone tries to modify balance directly and why
encapsulation prevents it.'''

'''class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.__balance=balance
    def set_balance(self):'''

'''Write a Program to print the first 50 prime Numbers without using Factors count?


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( N ) .

Output        :- Print First N no of Prime Numbers.

Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".'''
'''n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    count = 0
    num = 2

    while count < n:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
            count += 1

        num += 1'''
'''a = int(input())
b =a*a
b=b%10
if b == a:
    print('True')
else:
    print('False')'''


'''a = int(input())
b = a
c = a
count = 0

# count digits
while b > 0:
    count += 1
    b //= 10

p = 10 ** (count - 1)

while count > 0:
    r = c % 10
    c = c // 10
    c = r * p + c
    print(c)

    count -= 1'''
'''n = 7
a,b=0,1
for i in range(n):
    if a%2==0:
        print(a,end=" ")
    else:
        print(end=" ")
    a,b=b,a+b'''
'''n = int(input())

a, b = 0, 1
for i in range(n):
    for j in range(1,i+1):
        print(a, end=" ")
        a, b = b, a + b
    print()'''
'''a = int(input())
for i in range(1,a+1):
    n=2
    c=0
    while c<i:
        isprime=True
        for j in range(2,n):
            if n % j == 0:
                isprime=False
                break
        if isprime:
            print(n,end=" ")
            c +=1
        n +=1
    print()'''
'''n = int(input())

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

a, b = 0, 1

for i in range(n):
    if is_prime(a):
        print(i,end=" ")
    else:
        print(a,end=" ")
    a, b = b, a + b'''
a =200
b =1
if a==0 and b==0:
    print("Invalid Inputs")
else:
    if a>b:
        a,b=b,a
    if a<0:
        a=abs(a)
    c=0
    if b<0:
        b=abs(b)
    for i in range(a,b+1):
        dc=0
        h=0
        t=i
        while t>0:
            t=t//10
            dc +=1
        t=i
        while t>0:
            r=t%10
            h=h+r**dc
            t=t//10
        if h==i:
            if h%2==1:
                print(h)
