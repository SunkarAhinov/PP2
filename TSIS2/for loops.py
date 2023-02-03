                          #for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
for x in "banana":
  print(x)
  
  
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break                   #if it equal to banana it stops
    
    
    fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)                  #if it equal to banana it will be missing
  
  
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)                #it misses the banana and print apple and cherry 
  
x = int(input())
for x in range(6):
  print(x)
  
  
for x in range(2, 6):
  print(x)
  
  
for x in range(2, 30, 3):
  print(x)                    #it will miss numbers witch can be divided by 3
  
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")   #when it equal to 6 it prints finally
  
  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")   #it will stop after 2
  
  
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)        #the result is red fruits big fruits tasty fruits
    
    
for x in [0, 1, 2]:    
  pass         #for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

