def myfunc(str, n):
      fpart = str[:n] 
      lpart = str[n+1:]
      return fpart + lpart
print(myfunc(input(), int(input())))
