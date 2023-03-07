import re
with open("AAA.txt") as file:
    result = re.findall("^a(b*)$", file.read())
    print(result)