a = int(input())
b = int(input())
sum= 0
c=0
for i in range(a,b+1):
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f= f+1
    if f==2:
        if c%2==1:
            sum = sum + i
            c = c + 1
print(sum/c)



