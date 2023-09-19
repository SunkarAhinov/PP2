l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
	print(l, "is a vowel.")
elif l == 'y':
	print("vowel,consonant.")
else:
	print(l, "is a consonant.")