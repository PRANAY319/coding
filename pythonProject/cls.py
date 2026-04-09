'''Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    def _passed(self):
        if self.marks>=40:
            return True
        return False
p1 = Student('pranay',45)
print(f"{p1.name} is passed",p1._passed())'''
from functools import reduce

from encodings.punycode import selective_find

'''import queue
from multiprocessing.managers import Value

from pyexpat.errors import messages
'''
'''Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances.

class Employee:
    def __init__(self,name):
        self.name=name
        Employee.company_name='TechCorp'
    @classmethod
    def changed_company(cls,new_name):
        cls.company_name=new_name
        return cls.company_name
e1=Employee('PRANAY')
print(e1.changed_company('xyz'))'''

'''Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance.
class MathOps:
    def __init__(self,num):
        self.num=num
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
a1= MathOps(2)
print(a1.is_even(a1.num))'''
''''. Create a class Car with:
•	instance attribute mileage
•	class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.

class Car:
    def __init__(self,mileage):
        self.mileage=mileage
        Car.wheels=4
    def display_spacs(self):
        return self.mileage,Car.wheels
    @classmethod
    def change(cls,new_wheels):
        cls.wheels=new_wheels
        return cls.wheels
a1 = Car(40)
print(a1.display_spacs())
print(a1.change(6))'''
'''Use map() with a lambda to add 5 to every element of the following nested
list [[1, 2], [3, 4], [5, 6]]'''

'''p = int(input())
h = int(input())
a,b=0,1
c=0
s=0
for i in range(p,h+1):
    while a<=h:
        if a>=p:
            c +=1
            s +=a
        a,b=b,a+b
if c ==0:
    print("No Fabonoci series")
else:
    avg=s/c
    print("%.2f"%avg)'''
'''l = list(map(int,input().split()))
i = int(input())
if i in l:
    print(l.index(1,0,2))

else:
    print("no")'''
#ABSTRACTION
'''from abc import ABC, abstractmethod
class VECHILE(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class CAR(VECHILE):
    def go(self):
        print("DRIVE THE CAR")
    def stop(self):
        print("STOP THE CAR")
car = CAR()
car.go()
car.stop()'''
#prime or not
'''a = int(input())
b = int(input())
s=0
c=0
if a>0 and b>0:
    for i in range(a,b+1):
        fc = 0
        for j in range(1,i+1):
            if i%j==0:
                fc +=1
        if fc==2:
            c +=1
            if c%2==1:
                s += i
    if c !=0:
        print(s)
    else:
        print("not a prime")

avg = s/c
print("%.2f"%avg)
'''

#sum of even digits
'''a = int(input())
s=0
while a>0:
    r =a%10
    if r%2==0:
        s +=r
    a = a//10
print(s)
'''
'''l = list(map(int,input().split()))
k = int(input())
if k<len(l):
    l.pop(k)
else:
    print("no")
print(l)
'''
'''l = list(map(int,input().split()))
i = int(input())
if i in l:
    print(l.index(i))
else:
    print("no")
k=l[0]+l[-1]
print(k)
'''
'''l = list(map(int,input().split()))
k = int(input())
s=0
for i in range(len(l)):
    if i<=k:
        s +=l[i]
print(s)'''

#LCM WITH LIST
'''l = list(map(int,input().split()))
m = max(l)
k = m
while (True):
    c = 0
    for i in range(len(l)):
        if k%l[i]==0:
            c=c+1
    if c ==len(l):
        print(k)
        break
    k = k+m'''
# STACK IN DATA STRUCTURE
'''stack = []
def push():
    el = input("Enter You the Value")
    stack.append(el)
    print(f"Value is add to stack",el)
def pop():
    if not stack:
        print("stack is empty")
    else:
        el=stack.pop()
        print("Value is removed",el)
        print(stack)
def peek():
    print(f"top value",stack[-1])
def display():
    print(stack)

while True:
    print("Select the operation 1.push 2.pop 3.peek 4.show")
    choice = int(input())
    if choice ==1:
        push()
    elif choice == 2:
        pop()
    elif choice ==3:
        peek()
    elif choice == 4:
        display()
    else:
        print("Enter the Correct Operation")
'''
# PRIORITY QUEUE
'''import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(30)
q.put(40)
q.put(50)
print(q.get())
print(q.get())
print(q.get())
'''
# deque left to right 60,50,40,30,20,10
'''import collections
q=collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.appendleft(50)
q.appendleft(60)
q.pop()
q.pop()
print(q)'''
# deque right to left 10,20,30,40,50
'''import collections
q=collections.deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
q.append(50)
q.append(60)
q.popleft()
q.popleft()
print(q)'''
# First largest number
'''l = list(map(int,input().split()))
h1 = int(input())
h2=h1
for i in range(len(l)):
    if l[i]>h1:
        h2=h1
        h1 = l[i]
    else:
        l[i]>h2
        h2=l[i]
print(l)'''

'''l = list(map(int,input().split()))
a=int(input())
for i in range(len(l)):
    if i==a:
        l.insert(a,50)
        break

print(*l)'''


'''l = list(map(int,input().split()))
n = int(input())
print(l.count(n))'''

'''l = list(map(int,input().split()))
for i in range(len(l)):
    a=l[0]+l[-1]
print(a)'''

'''l = list(map(int,input().split()))
b = True
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        b = False
if b==True:
    print("List is Sorting")
else:
    print("no")'''

'''class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print("BOW")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print("MOW")
animal = Animal("abc")
dog = Dog("tom")
print(dog.name)
dog.make_sound()
'''

'''l = [1,2,3,4]
for i in l:
    l.remove(i)
print(l)'''

'''l = [10,20,30,40,50]
for i in range(0,len(l)):
    l1 = l[i:-1:-1]
    if l.count(l[i]>=0):
        print(l[i],l.count(l[i]))
'''
'''l = [1,2,8,5,7,11]
for i in l:
    fc = 0
    for j in range(1,i+1):
        if i%j==0:
            fc +=1
    if fc==2:
        print(i)'''

'''l = [1,2,10,12,15]
c = 0
s=0
for i in range(len(l)):
    if l[i]%2==1:
        c +=1
        s +=l[i]
print(s/c)'''

'''l = [1,2,10,7,11,12,15]
c = 0
s=0
for i in l:
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc +=1
    if fc==2:
        c +=1
        s +=i
avg = s/c
print("%.2f"%avg)'''

'''l = [1,2,10,7,11,12,15]
c = 0
s=0
for i in l:
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc +=1
    if fc==2:
        c +=1
        s +=i
        if j%2==1:
            print(i)
avg = s/c
print("%.2f"%avg)


l = [1,2,10,7,11,12,15]
l.reverse()
print(l)'''

# KEY VALUE
'''l = [1,2,10,7,11,12,15]
k = 17
found = False
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == k:
            print("Pair found:", l[i], l[j])
            found = True

    if not found:
        print("No pair found")
'''
# First Largest
'''l = [1,2,10,7,11,22,15]
h = float("-inf")
for i in range(len(l)):
    if l[i]>h:
        h=l[i]
print(h)'''

'''l = [1,2,10,7,11,22,15,1,2]
h = float("-inf")
for i in range(len(l)):
    c=0
    for j in range(0,i,1): #i-1,-1,-1
        if l[i]==l[j]:
            c = c+1
    if c == 0:
        k = l.count(l[i])
        if k>1:
            print(l[i])
# second largest number
l = [1,2,10,7,11,22,15,1,2]
h1 = float("-inf")
h2=h1
for i in range(len(l)):
    if l[i]>h1:
        h2 = h1
        h1 = l[i]
    elif l[i]>h2:
        h2 = l[i]
print({"second largest number : ",h2})
'''
# sort list without using sort
'''l = [1,2,10,7,11,22,15,1,2]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j] =l[j] ,l[i]
print(l)'''
# 20. Write a program to print the first four smallest missing elements from a list
'''l = [1,2,10,7,11,22,15,1,2]
m = min(l)+1
c=0
while True:
    if m not in l:
        print(m)
        c +=1
        if c ==4:
            break
    m +=1'''
# Linear Search'''
'''l = [1,2,10,7,11,22,15,1,2]
n = int(input())
b = False
for i in range(len(l)):
    if n ==l[i]:
        b = True
        break
if b == True:
    print("Found")
else:
    print('not found')
'''

'''l = [1,2,10,7,11,22,15,1,2]
for i in range(len(l)):
    c =0
    for j in range(len(l)):
        if l[i]==l[j]:
            c +=1
    if c==1:
        print(f"{l[i]} ~ {c}")'''

'''from abc import ABC , abstractmethod
class Notification(ABC):
    def __init__(self,message):
        self.message = message
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def __init__(self,message):
        super().__init__(self.message)
    @abstractmethod
    def send(self):
        print("send Notification")
class SMSNotification(Notification):
    def __init__(self,message):
        super().__init__(self.message)
    @abstractmethod
    def send(self):
        print("sms send message")
class PushNotification(Notification):
    def __init__(self,message):
        super().__init__(self.message)
    @abstractmethod
    def send(self):
        print("push the message")
hi = Notification("Hii")
print(EmailNotification.h1)

EmailNotification.send("hii")'''
'''
from abc import ABC, abstractmethod
# Abstract Base Class
class Notification(ABC):
    def __init__(self, message):
        self.message = message
    @abstractmethod
    def send(self):
        pass
# Child Class 1
class EmailNotification(Notification):
    def __init__(self, message):
        super().__init__(message)
    def send(self):
        print("Sending Email:", self.message)
# Child Class 2
class SMSNotification(Notification):
    def __init__(self, message):
        super().__init__(message)
    def send(self):
        print("Sending SMS:", self.message)
# Child Class 3
class PushNotification(Notification):
    def __init__(self, message):
        super().__init__(message)

    def send(self):
        print("Sending Push Notification:", self.message)
# Demonstrating Polymorphism
notifications = [
    EmailNotification("Welcome via Email"),
    SMSNotification("OTP via SMS"),
    PushNotification("New Alert via Push")
]
for n in notifications:
    n.send()'''


'''a = 1
b = 200
c=0
s=0
alt=0
for i in range(a,b+1):
    res=0
    dc=0
    t=i
    while t>0:
        t = t//10
        dc +=1
    t=i
    while t>0:
        r = t%10
        res = res+r**dc
        t = t//10
    if res == i:
        c +=1
        s +=i
        print(s)
        alt +=1
        if alt%2==1:
            print(i)

avg = s/c
print(avg)


n = 5
for i in range(1,n+1):
    num = i
    step = n-1
    for j in range(i):
        print(num,end=" ")
        num +=step
        step -=1
    print()

l = ['p','r','a','n','a','y']
l.reverse()
print(l)'''

#Write a program to print next Prime number for each element   in a list.
'''l =[10,14,5,12,30,34]
for i in range(0,len(l)):
    m = l[i]+1
    while True:
        fc = 0
        for j in range(1,m+1):
            if m%j==0:
                fc +=1
        if fc==2:
            print(m)
            break
        m +=1'''

f'''rom abc import ABC,abstractmethod

class Item(ABC):
    def __init__(self,title,metadata_dict,protected_available_flag):
        self.title=title
        self.__metadata_dict=metadata_dict
        self.protected_available_flag=protected_available_flag
'''
'''
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance
    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount
            print("Amount deposited:", amount)
        else:
            print("Insufficient balance :",amount)
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid withdraw amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -+ amount

    def get_balance(self):
        return self.__balance
acc = BankAccount(12321,2000)
acc.deposit(1000)
acc.withdraw(2000)
print(" Balance :",acc.get_balance())

acc.__balance = 100000
print("After direct modification attempt:", acc.__balance)
print("Actual Balance:", acc.get_balance())'''
# even number
'''n = int(input())
num = 2

for i in range(1, n+1):
    temp = num
    for j in range(i):
        print(temp, end=" ")
        temp += 6
    num += 2
    print()
'''
'''a =5
for i in range(1,a+1):
    print(""*(i-1),end="")
    for j in range(i,1,-1):
        print("*",end=" ")
    print()'''

'''Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
each implementing a different logic method.
Demonstrate how polymorphism can be achieved without inheritance by using
interchangeable strategy objects.'''
'''class Payment:
    def process(self, amount):
        print("Processing payment of", amount)


class CreditCardPayment(Payment):
    def process(self, amount, card_type):
        print("Processing", amount, "using", card_type, "credit card")


# Creating objects
p = Payment()
p.process(1000)

cc = CreditCardPayment()
cc.process(2000, "Visa")'''

'''class Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    @property
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        pass
class SavingAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)
    def withdraw(self,amount):
        return self.get_balance - amount
p1 = Account("xyz",1000)
print(p1.withdraw(100))
p2=SavingAccount("pqr",2000)
print(p2.withdraw(100))'''
# with slicing
'''l = [10,20,30,40]
for i in range(len(l)):
    print(*l)
    l=l[1:len(l)]+[l[i]]'''

# without slicing
'''l = [10,20,30,40]
for i in range(len(l)):
    print(*l)
    ele = l[0]
    for j in range(len(l)):
        l[j-1]=l[j]
    l[len(l)-1]=ele'''
#Automorphic
'''a = int(input("Enter number: "))
sq = a * a
digits = len(str(a))

if sq % (10 ** digits) == a:
    print("Automorphic")
else:
    print("Not Automorphic")'''

'''Automorphic
n = int(input())

if n == 0:
    print("Invalid Input.")
else:
    if n < 0:
        n = abs(n)

    sq = n * n
    digits = len(str(n))
    last = sq % (10 ** digits)

    if last == n:
        print("Automorphic")
    else:
        print(n - last)'''
'''
a = 5
m =1
for i in range(1,a+1):
    s = 0
    for j in range(1,i+1):
        print(m,end=" ")
        s += m
        m +=1
    print("-",s,end="")
    print()'''

'''
a = 5
m =2
for i in range(1,a+1):
    for j in range(1,i+1):
        print(m,end=" ")
        m +=2
    m = m-1
    print()'''
'''a = 5
b =10
for i in range(a,0,-1):
    for j in range(i):
        print(b,end=" ")
        b -=1
    print()'''

'''class Student:
    def __init__(self):
        self.marks = None

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks = marks

try:
    s1 = Student()
    s1.set_marks(85)
    print("Marks:", s1.marks)

    s1.set_marks(120)   # Invalid marks
except ValueError as e:
    print("Error:", e)'''

'''class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance=balance
    @property
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>=0:
            self.__balance += amount
            return self.__balance
        return f"Insufficient amount"
    def withdrawal(self,amount):
        if amount >0 and amount <=self.__balance:
            self.__balance -=amount
            return self.__balance
        return f"Insufficient Balance"
p1 = BankAccount(4110,5000)
print(p1.deposit(1000))
print(p1.withdrawal(1000))

p1.__balance = 100000
print("After direct modification attempt:", p1.get_balance)'''

'''class Student:
    def __init__(self,marks):
        self.marks=marks
        self.set_marks(marks)

    def set_marks(self, marks):
        if marks >0 and marks<100:'''
# string operation
'''n = "pranay123"
print(len(n))
print(n.find("a",1,6)) #first occurance
print(n.rfind("a",1,6)) # last occurance value
print(n.capitalize())
print(n.upper())
print(n.lower())
print(n.isdigit())
print(n.isalpha())
print(n.isalnum())'''

'''a = 5
for i in range(a,0,-1):
    s =0
    n = 1
    for j in range(i,0,-1):
        print(j,end=" ")
        s +=n
        n += 1
    print("-",s,end=" ")
    print()'''
'''
a = 5
n=2
for i in range(1,a+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n +=2
    n -=1
    print()'''

'''a = 4
b =5
for i in range(1,a+1):
    s = 0
    for j in range(1,i+1):
        print(b,end=" ")
        s += b
        b += 2
    if s%2==0:
        print("@",s,"-","even",end=" ")
    else:
        print("@",s,"-","odd",end=" ")

    print()'''
'''a = 5
n = 1
for i in range(1,a+1):
    s =0
    for j in range(i):
        print(n,end=" ")
        s +=n
        n += 2
    print("-",s,end=" ")
    print()'''

'''class SecureFile:
    def __init__(self,content,password):
        self.__content = content
        self.__password=password
        self.__log=[]
    def read(self,password):
        if password==self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return "Access Denied "

file1 = SecureFile("Secret Data", "1234")

print(file1.read("1234"))   
print(file1.read("1111"))
print(file1.read("0000"))'''
# next prime number
'''l = list(map(int,input().split()))
for i in range(0,len(l)):
    m=l[i]+1
    while True:
        c =0
        for i in range(1,m+1):
            if m%i==0:
                c +=1
        if c==2:
            print(i,end=" ")
            break
        m +=1'''
# key value
'''l = list(map(int,input().split()))
k = 10
for i in range(len(l)):
    for j in range(i+1,len(l)):
     if l[i]+l[j] ==k:
         print(l[i],l[j])'''

#Third largest number
'''l = list(map(int,input().split()))
m = float("-inf")
h1 = m
h2 =h1
for i in range(len(l)):
    if l[i]>m:
        h2 = h1
        h1=m
        m = l[i]
    elif l[i]>h1:
        h2 = h1
        h1 = l[i]
    elif l[i]>h2:
        h2=l[i]
print(m)
print(h1)
print(h2)'''

'''l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)'''
# missing number in list
'''l = list(map(int,input().split()))
m = min(l)+1
c=0
while True:
    if m not in l:
        print(m)
        c +=1
        if c==4:
            break
    m +=1'''

'''l = list(map(int,input().split()))
k = 4
for i in range(len(l)):
    if l[i]==k:
        print("Found")
        break
else:
    print("Not Found")'''

'''''k = list(map(int, input().split()))
o = int(input())

l = 0
u = len(k) - 1
b = False

while l <= u:
    m = (l + u) // 2

    if k[m] == o:
        b = True
        break
    elif o > k[m]:
        l = m + 1
    else:
        u = m - 1

if b:
    print("Found")
else:
    print("Not Found"'')'''

'''l = list(map(int, input().split()))
m = max(l)
while True:
        c=0
        for j in range(len(l)):
            if m%l[j]==0:
                c +=1
        if c==len(l):
            print(j)
            break
        m +=1'''

'''l = list(map(int, input().split()))

for i in range(len(l)):
    c = 0
    f = 0

    for k in range(i):
        if l[i] == l[k]:
            f = 1
            break

    if f == 1:
        continue

    for j in range(len(l)):
        if l[i] == l[j]:
            c += 1

    print(l[i], c)'''

'''l = list(map(int, input().split()))
for i in range(len(l)):
    c = 0
    f = 0
    for k in range(i):
        if l[i]==l[k]:
            f =1
            break
    if f==1:
        continue
    for j in range(len(l)):
        if l[i]==l[j]:
            c +=1
    print(l[i], c)'''
'''
l = list(map(int, input().split()))
h =0
ele=0
for i in range(len(l)):
    c=0
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            c+=1
            h= c
            ele =l[i]
    print(l[i], h)'''

'''l = list(map(int, input().split()))
for i in range(len(l)):
    m = l[i]+1
    while True:
        c = 0
        for j in range(1,m+1):
            if m %j==0:
                c +=1
        if c==2:
            print(j)
            break
        m +=1'''

'''l = list(map(int, input().split()))
m = float("-inf")
h1 = m
h2 = h1
for i in range(len(l)):
    if l[i]>m:
        h1 = m
        m =l[i]
    elif l[i]>h1:
        h2 =h1
        h1 =l[i]
    elif l[i]>h2:
        h2=l[i]

print(m)
print(h1)
print(h2)'''

'''l = list(map(int, input().split()))
for i in range(len(l)):
    m =l[i]+1
    c=0
    if m not in l:
        print(m)
        c +=1
    if c==4:
        break'''

'''l = list(map(int, input().split()))
m = min(l)
for i in range(m,-1,-1):
    c=0
    for j in range(len(l)):
        if l[j]%i==0:
            c +=1
    if c==len(l):
        print(i)
        break'''
'''l = list(map(int, input().split()))
m = max(l)
while True:
    c=0
    for i in range(len(l)):
        if m%l[i]==0:
            c +=1
    if c==len(l):
        print(m)
        break
    m +=1
'''

'''l = list(map(int, input().split()))
max_no=max(l)
step=max_no
while True:
    for i in l:
        if max_no%i!=0:
            break
    else:
        print(max_no)
        break
    max_no+=step'''
# clockwise rotation
'''l = [10,20,30,40]
for i in range(len(l)):
    print(*l)
    h = l[len(l)-1]
    for j in range(len(l)-2,-1,-1):
        l[j+1]=l[j]
    l[0]=h'''
'''l = [10,20,30,40]
for i in range(len(l)):
    print(*l)
    h = l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
    l[len(l)-1]=h
'''

'''l = list(map(int,input().split()))
k = int(input())

n = len(l)
k = k % n          # important if k > n

for i in range(k):
    print(l)
    first = l[0]
    for j in range(n-1):
        l[j] = l[j+1]
    l[n-1] = l[0]'''

'''l = list(map(int,input().split()))
for i in range(len(l)):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(*l)'''

'''l = [1,2,3,5]
for i in range(len(l)):
    m = l[i]+1
    while True:
        c =0
        for j in range(1,m+1):
            if m%j==0:
                c+=1
        if c==2:
            print(m)
            break
        m +=1'''
'''a = int(input())
if a<0:
    print("Invalid Input")
elif a==0:
    print(0)
elif a==1:
    print(2000)
elif an or a==3:
    print(5000)
elif a>=4 and a<=6:
    print(9000)
elif a==9:
    print(12000)
elif a==12:
    print(15000)
else:
    print("Error")'''

'''n = 16
a=2
c=0
while True:
    if c ==n:
        break
    c1=0
    for i in range(1,a+1):
        if a%i==0:
            c1+=1
    if c1==2:
        print(a)
        c +=1
    a +=1'''

'''l = [-1,-2,-3,4]
m=1
for i in l:
    m=m*i
    m = abs(m)
print(m)'''

'''def is_valid(s):
    if len(s)<10:
        return "Invalid"
    a = ord(s[0])
    if a<65 or a>90:
        return "Invalid"
    cc = dc = sc = sp=0
    for i in s:
        a = ord(i)
        if a>=65 and a<=90:
            cc +=1
        elif a>=97 and a<=122:
            sc +=1
        elif a>=48 and a<=57:
            dc +=1
        elif i == " ":
            return "Invalid"
        else:
            sp +=1
    if cc >=1 and sc >=1 and dc >=1 and sp>=1:
        return "valid"
    return "Invalid"
s = input()
print(is_valid(s))'''

'''class ShoppingCart:
    def __init__(self):
        self.__items=[]
    def add_item(self,item):
        self.__items.append(item)
    def remove(self,item):
        if item in self.__items:
            self.__items.remove(item)
    def get_item(self):
        return self.__items
    def set_item(self):
        if self.__items<0:
            return "no item is buy"
        return self.__items

cart = ShoppingCart()

cart.add_item("Apple")
cart.add_item("Banana")

print(cart.get_item())  # ['Apple', 'Banana']

# Attempt to modify externally
items = cart.get_item()
items.append("Hacked Item")

print(cart.get_item())
'''

'''l = [[1,2],[2,3],[3,4],[5,6]]
p = list(map(lambda s: list(map(lambda x:x+5,s)),l))
print(p)'''

'''d = {"apple":100,"banana":40,"cherry":150}
p = list(filter(lambda x : x>50,d.values()))
print(p)
'''
'''l = [5,10,15,20,25,30]
p = list(map(lambda x:x**2,l))
p1=list(filter(lambda x:True if x%5==0 else False ,l))
p2=list(reduce(lambda x,y:x+y,l))
print(p)'''

'''l =[1,2,3,4,5]
s=0
c = 0
for i in range(len(l)):
    c +=1
    s +=i
print(s/c)
'''
'''l =[10,20,30,40,50]
for i in range(len(l)):
    m = l[i]+1
    while True:
        fc = 0
        for j in range(1,m+1):
            if m%j==0:
                fc +=1
        if fc==2:
            print(m,end=" ")
            break
        m +=1'''

'''l =[10,20,30,40,50]
k = 90
found = False
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==k:
            print("True",l[i],l[j])
            found = True
if not found:
    print("False")'''

'''l =[10,20,30,40,50]
m = float("-inf")
h1 = m
for i in range(len(l)):
        if l[i]>m:
            h1 = m
            m = l[i]
        elif l[i]>m:
            h1 = l[i]
print(h1)'''

'''l = [1,3,6,2,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
    print(l[i],end=" ")'''


'''Write a Program to Check the Given Email Id is Valid or Not?

Note : Given Email Id is in the Form of ID@Domain.Extension
Constraints:
Input            : First Line of The Input Consists of Email Id

Output         : Print Valid or Invalid
Constraints  : 

ID@Domain.Extension

Email id Must starts with Alphabet.
Id Consists of Capital Letters, Small Letters, Digits, dot( . ) and Underscore( _ ) Only
Id Doesn't Starts with dot( . ) or Underscore( _ ) and Doesn't Ends with  dot( . ) or Underscore( _ ).
After Id @ Symbol Must 
Domain May consists of Alphabets and Digits Only
After Domain Dot( . ) Symbol Must
Extension May Consists of only Alphabets
Email Id Must Consists of 15 to 25 Characters Only ( 15 <= Length'''

'''def is_valid(id):
    asi = ord(id[0])
    if (asi>=65 and asi<=90) or (asi>=97 and asi<=122):
        if id[-1]=="." or id[-1]=="-":
            return "False"
        for i in range(1,len(l)):
            asi = ord(id[i])
            if (asi>=65 and asi<=90) or (asi>=97 and asi<=122) or (asi>=48 and asi<=57):
                continue
            if i<len(i)-1 and (id[i]=="." or id[i]=="-"):
                continue
            return False
        return True
    else:
        return False'''

'''def is_valid(email):

    # 1. Length check
    if len(email) < 15 or len(email) > 25:
        return "Invalid"

    # 2. First character must be alphabet
    a = ord(email[0])
    if not ((a >= 65 and a <= 90) or (a >= 97 and a <= 122)):
        return "Invalid"

    # 3. Check '@' count and position
    count = 0
    pos = -1
    for i in range(len(email)):
        if email[i] == '@':
            count += 1
            pos = i

    if count != 1:
        return "Invalid"

    # 4. ID part check
    if email[0] == '.' or email[0] == '_' or email[pos-1] == '.' or email[pos-1] == '_':
        return "Invalid"

    for i in range(1, pos):
        a = ord(email[i])
        if (a >= 65 and a <= 90) or (a >= 97 and a <= 122) or (a >= 48 and a <= 57):
            continue
        elif email[i] == '.' or email[i] == '_':
            continue
        else:
            return "Invalid"

    # 5. Find dot after '@'
    dot = -1
    for i in range(pos+1, len(email)):
        if email[i] == '.':
            dot = i
            break

    if dot == -1:
        return "Invalid"

    # 6. Domain check (letters + digits)
    for i in range(pos+1, dot):
        a = ord(email[i])
        if not ((a >= 65 and a <= 90) or (a >= 97 and a <= 122) or (a >= 48 and a <= 57)):
            return "Invalid"

    # 7. Extension check (only letters)
    for i in range(dot+1, len(email)):
        a = ord(email[i])
        if not ((a >= 65 and a <= 90) or (a >= 97 and a <= 122)):
            return "Invalid"

    return "Valid"

id = input()
print(is_valid(id))'''

'''def is_valid(email):

    # 1. Length check
    if len(email) < 15 or len(email) > 25:
        return "Invalid"

    # 2. First character must be alphabet
    a = ord(email[0])
    if not ((a >= 65 and a <= 90) or (a >= 97 and a <= 122)):
        return "Invalid"

    # 3. ID start should not be . or _
    if email[0] == '.' or email[0] == '_':
        return "Invalid"

    # 4. Traverse string
    i = 0

    # ---- ID PART ----
    while i < len(email) and email[i] != '@':
        a = ord(email[i])

        if (a >= 65 and a <= 90) or (a >= 97 and a <= 122) or (a >= 48 and a <= 57):
            pass
        elif email[i] == '.' or email[i] == '_':
            pass
        else:
            return "Invalid"
        i += 1

    # must have '@'
    if i == len(email):
        return "Invalid"

    # ID should not end with . or _
    if email[i-1] == '.' or email[i-1] == '_':
        return "Invalid"

    i += 1  # move after '@'

    # ---- DOMAIN PART ----
    start = i
    while i < len(email) and email[i] != '.':
        a = ord(email[i])
        if not ((a >= 65 and a <= 90) or (a >= 97 and a <= 122) or (a >= 48 and a <= 57)):
            return "Invalid"
        i += 1

    # must have '.'
    if i == len(email) or i == start:
        return "Invalid"

    i += 1  # move after '.'

    # ---- EXTENSION PART ----
    if i == len(email):
        return "Invalid"

    while i < len(email):
        a = ord(email[i])
        if not ((a >= 65 and a <= 90) or (a >= 97 and a <= 122)):
            return "Invalid"
        i += 1

    return "Valid"'''

'''l = [10,30,50,70]
m = min(l)+1
c =0
while True:
    if m not in l:
        c +=1
        print(m,end=" ")
        if c ==4:
            break
    m +=1'''

'''l = [1,2,3,4,5]
n = 5
b = False
for i in range(len(l)):
    if n ==l[i]:
        b= True
        break
if b==True:
    print("found")
else:
    print("Not found")'''

'''l = [1,2,3,4,5]
n = 5
l1 = 0
up=len(l)-1
b = False
while l1<=up:
    m = (l1+up)//2
    if l[m]==n:
        print("found")
        b = True
        break
    elif n>l[m]:
        l1 = m+1
    elif n<l[m]:
        up = m-1
if b == False:
    print("not Found")
'''
'''l = [1,2,3,4,5]
m = min(l)
for i in range(m,0,-1):
    c = 0
    for j in range(len(l)):
        if l[j]%i==0:
            c +=1
    if c==len(l):
        print(i)
        break'''
'''l = [1,2,3,4,5]
m = max(l)
while True:
    c = 0
    for i in range(len(l)):
        if m%l[i]==0:
            c+=1
    if c==len(l):
        print(m)
        break
    m +=1'''

'''l = [10,15,30,10,30,40,50]
hf=0
ele=0
for i in range(len(l)):
    c = 0
    for j in range(i-1,-1,-1):
        if l[i]==l[j]:
            c+=1
    if c==0:
        print(l[i],l.count(l[i]))'''

'''l = [10,15,30,10,30,40,50,10]
lv = float("inf")
for i in range(len(l)):
    c = l.count(l[i])
    if c==1:
        if l[i] < lv:
            lv =l[i]

if lv != float("inf"):
    print(lv)
else:
    print("No unique element")'''

'''l=[10,20,30,40,50]
for i in range(len(l)):
    print(*l)
    ele=l[0]
    for j in range(1,len(l)):
        l[j-1]=l[j]
    l[len(l)-1]=ele'''

'''l=[10,20,30,40,50]
for i in range(len(l)):
    print(*l)
    ele=l[len(l)-1]
    for j in range(len(l)-2,-1,-1):
        l[j+1]=l[j]
    l[0]=ele'''

'''l = [10, 20, 30, 40, 50]
k = 2

for _ in range(k):
    ele = l[0]
    for j in range(1, len(l)):
        l[j-1] = l[j]
    l[-1] = ele

print(*l)'''

'''n = int(input())
if n<=0:
    print("Invalid Input")
else:
    for i in range(1, n+1):
        num = i
        step = n - 1
        for j in range(i):
            print(num, end=" ")
            num += step
            step -= 1
        print()'''

'''l = list(map(int,input().split()))
pos=[]
neg=[]
for i in l:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
i = 0
j = 0
res=[]
while i<len(pos) and j<len(neg):
    res.append(pos[i])
    res.append(neg[j])
    i +=1
    j +=1
while i<len(pos):
    res.append(pos[i])
    i +=1
while j<len(neg):
    res.append(neg)
    j +=1
print(*res)'''

'''l = [1,2,3,1,2,3]
for i in range(len(l)):
    c = 0
    for j in range(i-1,-1,-1):
        if l[i]==l[j]:
            c+=1

    print(f"{l[i]}~{c}")'''

'''l = [1,2,3,1,2,3]
p=0
h=0
for i in range(len(l)):
    c =0
    for j in range(len(l)):
        if l[i]==l[j]:
            c +=1
        if c>p:
            p = c
            h =l[i]
            print(f"{h}~{p}")'''
# file handling
"""file = "text"
with open(file,"r") as f:
    c = f.read()
    print(c)"""
'''f= open("text","r")
a = f.read()
print(a)
'''

'''file = "text"
with open(file,"w") as f:
    f.write("hello")
    f.writelines([" what are you doing\n"
                 " i am fine \n"])'''

'''l = [1,2,3,1,2,3,1,2]
b = False
for i in range(len(l)):
    for k in range(i):
        if l[i]==l[k]:
            b = True
            break
    if b:
        continue
    c  =0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    print(f"{l[i]}~{c}")'''

'''l = [1,2,3,1,2,3,4,2]
for i in range(len(l)-1,-1,-1):
    b=False
    for k in range(i+1,len(l)):
        if l[i]==l[k]:
            b = True
            break
    if b:
        continue
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c +=1
    print(f"{l[i]}~{c}")
'''
'''n , a = map(int, input().split())
for i in range(n):
    for j in range(a):
        if i==0 or i==n-1 or j==0 or j==a-1:
            print("*",end=" ")
        else:
            print("$",end=" ")
    print("")'''

'''n = 6
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print("1",end=" ")
        else:
            print(i,end=" ")
    print()'''

n = 5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")
