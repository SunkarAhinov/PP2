a=int(input())
start = 540
lesson = 45
bruh = 5
bruh2 = 15
b=a - a//2
p=a*lesson+start+(a//2*bruh2)+b*bruh
j = 60
p = p%1440
if a%2!=0:
    print((p-5) // j,":",(p-5) % j)
elif a%2==0:
    print((p-15) // j,":",(p-15) % j)
else:
    print("No")