print("Input lengths of the triangle sides: ")
x = int(input())
y = int(input())
z = int(input())
if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")