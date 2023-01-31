x="sprite"                                #global variables
def func():
  print("Python is " + x)
func()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def func():
  global x
  x="fanta"
func()
print("Python is " + x)


x="pepsi"
def func():
  global x
  x="pepsi"
func()
print("Python is " + x)