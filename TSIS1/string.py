print("Hello")      #string
print('Hello')                       #they are same


a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)                             #also u can use three quotes



a = "Hello, World!"                  #result is e second letter
print(a[1])                          #string are arrays


#Loop through the letters in the word "banana":
for x in "banana":
  print(x)
  
  
  # the result is lenght of a its 13
  a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
  txt = "The best things in life are free!"
print("expensive" not in txt)



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
