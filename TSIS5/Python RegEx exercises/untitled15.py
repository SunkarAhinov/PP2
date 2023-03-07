import re
with open("AAA.txt") as file:
    result = re.findall("^[a-z]+_[a-z]+$", file.read())
    print(result)