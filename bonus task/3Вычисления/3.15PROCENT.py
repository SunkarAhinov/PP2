a=int(input())
b=int(input())
c=int(input())

q=b*100
w=q+c
e=w*(a/100+1)
print(round(e//100),round(e%100))