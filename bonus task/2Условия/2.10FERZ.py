a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("Yes")
elif b + a == c + d:
    print("Yes")
elif a == b and c == d:
    print("Yes")
elif (a+b-c+d)%2 == 0 and a-b != c-d and b-a != d-c and b-a != c-d and a-b != d-c:
    print("Yes")
else:
    print("No")