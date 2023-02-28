n=int(input())
def myfunc(n):
    i=0
    while i<=n:
        if i%3==0 and i%4==0:            
            yield i
        i+=1
my=myfunc(n)
for s in my:
    print(s,sep=",",end=", ")