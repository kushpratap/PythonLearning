X = 5
Y = "Kush"
print(X, end=" Times ")
print(Y)
X = 6
print(X)
var1 = 4
var2 = 36.4
print(type(var1))
print(var1 + var2)
# print(var1+Y)  # ---- this will throw error as both variable are of different types

var3 = "20"
var4 = "30"
print(var3 + var4)  # the type will become string if it is in double quotes.That is why it is not adding the digits.

# typecasting . If a variable has to be changed from string to integer,it can be done via typecasting.

print(int(var3) + int(var4))  # Now the value is getting added and the type is changed to int.

"""  Similarly we have multiple functions for typecasting e.g
str()
int()
float()
etc.
"""
# if a string need to be written multiple times then we can multiply the string by the needed no like shown below.
print(10 * "Hello world")  # if new line is needed we can use backslash n
print(10 * "Hello world\n")

a = str(3)
b = int(3)
c = float(3)
print(a)
print(b)
print(c)

d = 4
D = "Sally"
print(d)
print(D)  # D will not overwrite d

"""  
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

""" 
Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

"""

"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"
Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"
Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"


Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
Note: Make sure the number of variables matches the number of values, or else you will get an error.

One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
# Unpack a Collection
# If you have a collection of values in a list,
# tuple etc. Python allows you extract the values into variables. This is called unpacking.


fruits = ["apple", "banana", "cherry"]
e, f, g = fruits

print(e)
print(f)
print(g)

"""
Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

Example
x = "awesome"
print("Python is " + x)
output= Python is awesome

"""

"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Example
Create a variable outside of a function, and use it inside the function

l = "awesome"

def myfunc():
  print("Python is " + l)
myfunc()

===Output= Python is awesome.

"""


"""

If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
for example :- 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x, end=" and ")

myfunc()

print("Python is " + x)

Output= Python is fantastic and Python is awesome
"""




"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
Example
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

Also, use the global keyword if you want to change a global variable inside a function.

Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""


print("Enter Your number")
num = input()

print('The number entered is ', num)


# print("Enter Your number 1")
# inpnum1 = input()
# print("Enter Your number 2")
# inpnum2 = input()
#
# print("The addition is", int(inpnum1)+int(inpnum2))

