def myfunc(str):
  res = "" 
  for i in range(len(str)):
    if i%2 == 0:
      res = res + str[i]
  return res
print(myfunc(input()))
