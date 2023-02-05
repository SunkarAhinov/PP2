s1=0
s2=0
i=0
a=int(input())
while a!=0:
    i+=1
    s1+=a
    s2+=a**2
    a=int(input())
print(((s2-s1**2/i)/(i-1))**(0.5))