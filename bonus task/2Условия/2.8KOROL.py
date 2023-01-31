a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a-1 == c or a+1 == c:
    print("Yes")
elif b+1 == c or b-1 == a:
    print("Yes")
else:
    print("No")