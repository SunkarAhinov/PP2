x=int(input())
def myfunc(x):
    i=0
    while i<x:
        i+=1
        yield i*i        
my=myfunc(x)
for s in my:
    print(s)