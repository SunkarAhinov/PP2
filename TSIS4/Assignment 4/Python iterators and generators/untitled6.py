x=int(input())
def myfunc(x):
    i=x
    while i>=0:
        yield i 
        i-=1
my=myfunc(x)
for s in my:
    print(s)