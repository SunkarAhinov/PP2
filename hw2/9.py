m = input("Input the month: ")
day = int(input("Input the day: "))

if m in ('January','February','March'):
	s = 'winter'
elif m in ('April','May','June'):
	s = 'spring'
elif m in ('July','August','September'):
	s = 'summer'
else:
	s = 'autumn'
print("Season is",s)
