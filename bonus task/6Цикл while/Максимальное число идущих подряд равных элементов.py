a=-1
l1=0
l2=0
b=int(input())
while b!=0:
    if a==b:
        l1+=1
    else:
        a=b
        l2=max(l2,l1)
        l1=1
    b=int(input())
l2=max(l2,l1)
print(l2)