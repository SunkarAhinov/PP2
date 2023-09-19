d = int(input("Input birthday: "))
m = input("Input month of birth (e.g. march, july etc): ")
if m == 'december':
	a = 'Sagittarius' if (d < 22) else 'capricorn'
elif m == 'january':
	a = 'Capricorn' if (d < 20) else 'aquarius'
elif m == 'february':
	a = 'Aquarius' if (d < 19) else 'pisces'
elif m == 'march':
	a = 'Pisces' if (d < 21) else 'aries'
elif m == 'april':
	a = 'Aries' if (d < 20) else 'taurus'
elif m == 'may':
	a = 'Taurus' if (d < 21) else 'gemini'
elif m == 'june':
	a = 'Gemini' if (d < 21) else 'cancer'
elif m == 'july':
	a = 'Cancer' if (d < 23) else 'leo'
elif m == 'august':
	a = 'Leo' if (d < 23) else 'virgo'
elif m == 'september':
	a = 'Virgo' if (d < 23) else 'libra'
elif m == 'october':
	a = 'Libra' if (d < 23) else 'scorpio'
elif m == 'november':
	a = 'scorpio' if (d < 22) else 'sagittarius'
print("Your Astrological sign is :",a)