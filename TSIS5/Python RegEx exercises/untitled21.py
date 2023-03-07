import re
text = open("AAA.txt"):
print(re.findall('[A-Z][^A-Z]*', text))