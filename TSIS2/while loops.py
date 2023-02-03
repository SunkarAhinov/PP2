                    #while loops
i = 1
while i < 6:
  print(i)
  i += 1
  
  
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1    #equal to 3
  
  
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)   #3 will be missing
  
  
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  #i is no longer less than 6 will be after 12345
  
  
  