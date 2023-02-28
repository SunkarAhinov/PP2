n=int(input())
def myfunc(n):
    i=0
    while i<=n:
        yield i
        i+=2
my=myfunc(n)
for s in my:
    print(s,sep=",",end=", ")