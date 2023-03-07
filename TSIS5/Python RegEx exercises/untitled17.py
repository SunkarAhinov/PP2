import re
file = open("AAA.txt"):
    result = re.findall("[A-Z]+[a-z]+$", file.read())
    print(result)