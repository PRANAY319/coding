a = int(input())
b = int(input())
c=0
sum=0
alt=0
for i in range(a,b+1):
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc=fc+1
    if fc==2:
        alt=alt+1
        if alt%2==1:
            c = c + 1
            sum = sum + i
        avg = sum/c
print(sum)