a=int(input())
if a==0:
    print(0)
else:
    b,c=0,1
    for i in range(2,a+1):
        b,c=c,b+c
    print(c)