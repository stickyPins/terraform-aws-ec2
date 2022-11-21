print("Hello Python")

if 5 > 2:
 print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")


 if 5 > 2:
  print("Five is greater than two!")
  print("Five is greater than three!")

  #This is a comment
  print("I love snakes ")


# Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.

x=5
y="will"
print(y)
print(x)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Number of variables must match number of values

# Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)