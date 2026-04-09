'''a = 30
s=0
for i in range(1,a+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c +=1
    if c==2:
        print(i,end=" ")
        s +=1'''
'''a=int(input())
def prime(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc +=1
    if fc==2:
        return True
    return False
for i in range(1,a+1):
    h=2
    for i in range(1,i+1):
        print(h,end=" ")
        h +=1
        while not prime(h):
            h +=1
    print()'''
'''n = int(input( ))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

rows = 3
num = 2

for i in range(1, rows + 1):
    count = 0
    while count < i:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()'''
'''a = 5
n=1
for i in range(a,0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        if n<=9:
            print(n,end=" ")
        else:
            print(" "+str(n),end="")
        n +=1
    print()'''
#prime by using functions
'''def k(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc +=1
    if fc==2:
        print("prime")
    else:
        print("not prime")
n = int(input())
k(5)'''
# palindrome number
'''def reverse(a):

    for i in range(1,a+1):
        t=i
        rev=0
        while t>0:
            r = t%10
            rev=rev*10+r
            t= t//10
    if rev==i:
        print(rev,"number is Palindrome")
    else:
        print("not palindrome")
n = int(input())
reverse(n)'''
# armstrong number
'''def armstrong(a):
    for i in range(1,a+1):
        h=i
        rev=0
        c=0
        while h>0:
            h =h//10
            c +=1
        h=i
        while h>0:
            r =h%10
            rev = rev+r**c
            h =h//10
        if rev==i:
            print(rev)

n =int(input())
armstrong(n)'''
'''def m(n):
    if n>=1:
        print(n)
        m(n-1)
        print(n)
n = int(input())
m(n)'''
'''def m(n):
    if n>=1:
        if n%2==0:
            print(n)
        m(n-1)
n = int(input())
m(n)'''
#recursion
'''def m(n,k):
    if k<=n:
        if n%k==0:
            print(k)
    m(n,k+1)
n = int(input())
m(n,1)'''
a = 6
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

