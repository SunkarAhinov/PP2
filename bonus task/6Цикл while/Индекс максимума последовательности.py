i=-1
b=-1
max=0
len=0
while b!=0:
    b=int(input())
    if b>max:
        max=b
        i=len
    len+=1
print(i)