import re
with open("C:\Users\user\.spyder-py3\labs\TSIS5\Python RegEx exercises\AAA.txt") as file:
    result = re.findall("ab{2,3}", file.read())
    print(result)