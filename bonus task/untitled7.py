

a = int(input())
b = int(input())

e = a*a+b*b
sqrt = e ** (0.5)

print(e)

a = int(input())
sqrt = a ** (0.5)
print(str(sqrt))

print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # две звёздочки означают возведение в степень
print(37 / 3)  # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша считают частное от деления нацело
                # это как операция div в других языках
print(37 % 3)  # процент считает остаток от деления нацело
               # это как операция mod в других языках


x = int(input())
if x > 0:
    print(x)
else:
    print(-x)
    
    
    x = int(input())
if x < 0:
    x = -x
print(x)



x = int(input())
y = int(input())
if x > 0:
    if y > 0:               # x > 0, y > 0
        print("Первая четверть")
    else:                   # x > 0, y < 0
        print("Четвертая четверть")
else:
    if y > 0:               # x < 0, y > 0
        print("Вторая четверть")
    else:                   # x < 0, y < 0
        print("Третья четверть")
        
        
        
        
        a = int(input())
b = int(input())
if a % 10 == 0 or b % 10 == 0:
    print('YES')
else:
    print('NO')
