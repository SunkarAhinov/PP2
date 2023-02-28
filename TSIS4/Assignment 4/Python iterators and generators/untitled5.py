n=int(input())
x=int(input())
def myfunc(n,x):
    i=n
    while i<=x:
        yield i*i 
        i+=1
my=myfunc(n,x)
for s in my:
    print(s)