n=int(input())
s1=1
s2=0
for i in range(1,n+1):
    s1*=i
    s2+=s1
    print(s2)