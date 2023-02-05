a = int(input())
if a == 0:
    print(0)
else:
    f1,f2=0,1
    b=1
    while f2<=a:
        if f2==a:
            print(b)
            break
        f1,f2=f2,f1+f2
        b+=1
    else:
        print(-1)