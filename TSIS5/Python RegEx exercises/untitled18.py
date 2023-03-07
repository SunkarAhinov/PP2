import re
file = open("AAA.txt"):
    result = re.findall("a.*?b$", file.read())
    print(result)