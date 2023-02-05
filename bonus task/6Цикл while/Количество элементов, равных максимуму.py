m=0
s=0
a=-1
while  a!=0:
    a=int(input())
    if a>m:
        m,s=a,1
    elif a==m:
        s+=1        
print(s)
