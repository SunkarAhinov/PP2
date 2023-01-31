h=int(input())
m=int(input())
s=int(input())

q=h*3600
w=m*60
s=q+w+s
r=s*(360/(12*60*60))
print(r)