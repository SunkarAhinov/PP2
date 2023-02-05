a=int(input())
m1=0
m2=0
while a!=0:
    if a>m1:
        m2=m1
        m1=a
    elif a>m2:
        m2=a
    a=int(input())
print(m2)