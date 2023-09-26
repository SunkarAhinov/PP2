def str(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]
print(str(input()))
