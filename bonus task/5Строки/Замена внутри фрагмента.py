a=input()
b=a[:a.find('h')+1] 
c=a[a.find('h')+1:a.rfind('h')]
d=a[a.rfind('h'):]
f=c.replace('h','H')
e=b+f+c
print(e)
