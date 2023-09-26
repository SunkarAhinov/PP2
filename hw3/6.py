def myfunc(str):
  length = len(str)
  if length > 1:
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'
  return str
print(myfunc(input()))

