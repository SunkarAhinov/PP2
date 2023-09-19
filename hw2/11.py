a = int(input("Input your birth year: "))
if (a - 2000) % 12 == 0:
    b = 'Dragon'
elif (a - 2000) % 12 == 1:
    b = 'Snake'
elif (a - 2000) % 12 == 2:
    b = 'Horse'
elif (a - 2000) % 12 == 3:
    b = 'sheep'
elif (a - 2000) % 12 == 4:
    b = 'Monkey'
elif (a - 2000) % 12 == 5:
    b = 'Rooster'
elif (a - 2000) % 12 == 6:
    b = 'Dog'
elif (a - 2000) % 12 == 7:
    b = 'Pig'
elif (a - 2000) % 12 == 8:
    b = 'Rat'
elif (a - 2000) % 12 == 9:
    b = 'Ox'
elif (a - 2000) % 12 == 10:
    b = 'Tiger'
else:
    b = 'Hare'
print("Your Zodiac sign :",b)