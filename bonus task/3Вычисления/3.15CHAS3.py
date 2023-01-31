a = float(input())
c = 12*3600/360
b=int(a*c//3600)
d=int(a*c%3600//60)
e=int(a*c%3600%60)
print(b,d,e)