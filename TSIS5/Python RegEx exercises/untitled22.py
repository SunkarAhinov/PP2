import re
capital = open("AAA.txt")
def capital_words_spaces(capital):
    
  return re.sub(r"(\w)([A-Z])", r"\1 \2",capital)

print(capital_words_spaces(capital))
