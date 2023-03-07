def Palindrome(string):
	lp = 0
	rp = len(string) - 1
	
	while rp >= lp:
		if not string[lp] == string[rp]:
			return False
		lp += 1
		rp -= 1
	return True
print(Palindrome(input()))