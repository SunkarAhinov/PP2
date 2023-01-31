h=int(input())
a=int(input())
b=int(input())
if h<a:
    print(1) 
elif b == 0:
    print(h//a)
elif (h-a)//(a-b)!=0:
    print((h-a)//(a-b)+2)
elif b != 0:
    print((h-a)//(a-b)+1)
else:
    print("Error")
    
  #H = int(input())
  #A = int(input())
  #B = int(input())
  #print(1 + (H - A) // (A - B))