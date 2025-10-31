# ==========================================================================
# Assignment 1: Covers basic code snippets executed in the class from w3schools.com
# ==========================================================================

# ====================================================
# VALID code snippets illustrating "print" function !
# ====================================================

# 1. print function is used to print the text to the screen (output device)
print("Hello, World!") # this will print - Hello, World! - to the screen.

# 2. print functiom can have single or double quotes
print('Single quotes are okay !')
print("So, are double quotes :) ") 

# 3. Multiple print statements can also be stacked one by one and they will be executed in the same order as they are defined.
print("First statement !")
print("Second statement !")
print("Third statement !")

# 4. print by default displays the text in a new line, so the output of the above three print statements would be - 
"""
First statement !
Second statement !
Third statement !
"""

# 5. In case you wish to have them all in one line, you can use "ends" keyword as a parameter to the print function - 
print("First statement !", end = "")
print("Second statement !", end = "")
print("Third statement !")

"""
First statement ! Second statement ! Third statement !
"""

# 6. Semi colons are optional in python, but they are still valid. The following code snippet is valid but lacks readability, hence would be difficult to maintain.
print("Hello"); print("How are you?"); print("Have a great day!"); print("Bye, Bye !"); 

# 7. Using escape sequences inside print.
print("C:\\newfolder\\test")

# 8. print function with different data types

print("I am a string !")
print('I am a string too !')
print(1) # integer
print(1.1) # float

print(3 + 3) # math can also be done inside print function. This statement will print 6 as output.
print(2 * 5) # will print 10.

print("a" * 10) # this will print "a" 10 times.

print("I am", 35, "years old !") # mixing text and numbers. I am 35 years old ! will be printed in this case. 


# =================================================
# INVALID code snippets of "print" function !
# =================================================

# 1. If you put 2 print statements on the same line without a separator (newline or ;) then python will give an error.
"""

print("Darling, Darling - Stand by me !") print("I can not, since Python needs a separator between us ;) print("Sorry, The Beatles ! ) ") 

"""
# Correct version:
print("Darling, Darling - Stand by me !"); print("I can not, since Python needs a separator between us :(" ) ; print("Sorry, The Beatles ! ) ") 

# 2. print is a function, hence needs parentheses. Following gives an error since it is missing parentheses.

"""
print "Hello, World !"
"""
# Correct version:
print("Hello, World !")

# 3. Incorrect escape sequence

"""
print("C:\newfolder\test")
"""
# Correct version:
print("C:\\newfolder\\test")

# =================================================
# VALID code snippets illustrating "Indentation" !
# =================================================

# Indentation in Python is very important. The Python interpreter uses indentation to define code blocks and determine the structure of the program.

# 1. Basic if-else construct with indentation usage.
if 5 > 2:
    print("Five is greater than two!")
else : 
    print("Parallel Universe! where Five is not greater than two ;) ")

# 2. Basic for loop
for i in range(3):
    print("Iteration:", i)
    print("This line runs inside the for loop!")

print("Loop finished! This is outside the for loop, hence no indentation !")

# 3. Nested indentation ( mixing basic loop with basic if-else )

for i in range(3):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

print("Done !")

# 4. Indentation can be any number of spaces, but there should atleast be one space.

if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
            print("Five is greater than two! This indentation is also correct.")
if 5 > 2:
 print("Even this is fine, it has one space indentation !")


# =====================================================
# INVALID code snippets for "Indentation" !
# =====================================================

# 1. Missing indentation following the if clause. Interpreter will report an error here

"""
if 5 > 2:
print("This will result into error !")
"""
# Correct version:
if 5 > 2:
    print("Correct indentation !")

# 2. For the same conditional clause, spaces can not be mixed. They should all have the same indendation.
"""
if 5 > 2:
    print(" I have one tab indentation. ")
 print(" I have one space indentation. ")
        print(" I have two tabs indentation. ")
"""
# Correct version:
if 5 > 2:
    print(" I have one tab indentation. ")
    print(" I have one tab indentation. ")
    print(" I have one tab indentation. ")
print("Done!")

# =========================================================
# VALID code snippets illustrating "Comments" !
# ========================================================= 

# Comments. Comments are just information about the code in plain language. The interpreter ignores this while the python code is compiled to bytecode internally. ---

# 1. This is a basic, one-liner comment

"""
2. This is a multi-line comment.
Comments can explain code.
"""

'''
3. Multi-line comment can also be surrounded by single quotes.
This is also a multi-line comment.
'''

# 4. Inside quotes # is not treated as a comment delimiter by python interpreter.
print("Comments are ignored by Python. Inside quotes # is just a character, not a comment delimiter.")

# =========================================================
# INVALID code snippets for "Comments" !
# ========================================================= 

# 1. Indented comment outside a block

'''
if True:
    print("Hello")
  # This comment is wrongly indented
print("Done")
'''
# Correct version:
if True:
    print("Hello")
# Properly aligned comment
print("Done")


# =========================================================
# VALID code snippets illustrating "Variables" ! 
# =========================================================

'''
Varialbes in python are dynamically typed and flexible. Variables, as the name suggests, hold values that can vary.
In Python, a variable can store a value of any data type, and its data type can change during the program’s execution.
A single variable can hold integers, strings, lists, or any other data type at different points in the program.
'''

# 1. Variables.
x = 5
y = "John"
print(x) # will print 5
print(y) # will print John

# 2. Variables type can be changed.
x = "Sally" # x is now holding a string value.
print(x) # will print Sally 

# 3. Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z) # will print 3 3 3.0

# Get the type
x = 5
y = "John"
print(type(x)) # will print <class 'int'>
print(type(y)) # will print <class 'str'>

# Variable names are case-sensitive:
a = 4
A = "Sally"
print(a) # will print 4
print(A) # will print Sally

# --- Multiple Variables ---
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry

# One value to multiple variables:
x = y = z = "Orange"
print(x) # Orange
print(y) # Orange
print(z) # Orange

# Unpack a collection:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # apple
print(y) # banana
print(z) # cherry

# --- Output Variables ---
x = "Python is awesome"
print(x) # Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # Python is awesome

print(x + y + z)  # String concatenation # Pythonisawesome

# Mixing strings and numbers requires explicit conversion:
x = 5
y = 10
print(x + y)
print("The sum is:", x + y) # The sum is: 15

# --- Global Variables ---
x = "awesome" 

def myfunc():
    print("Python is " + x) # Python is awesome

myfunc()

# Change global variable inside function
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x) # Python is fantastic

# =========================================================
# VALID code snippets illustrating various data types !
# =========================================================

# Basic examples:
x = 5
print(type(x)) # <class 'int'>

x = "Hello World"
print(type(x)) # <class 'str'>

x = 20.5
print(type(x)) # <class 'float'>

x = ["apple", "banana", "cherry"]
print(type(x)) # <class 'list'>

x = ("apple", "banana", "cherry")
print(type(x)) # <class 'tuple'>

x = range(6)
print(type(x)) # <class 'range'>

x = {"name": "John", "age": 36}
print(type(x)) # <class 'dict'>

x = {"apple", "banana", "cherry"}
print(type(x)) # <class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # <class 'frozenset>

x = True
print(type(x)) # <class 'bool'>

x = b"Hello"
print(type(x)) # <class 'bytes>

x = bytearray(5)
print(type(x)) # <class 'bytearray>

x = memoryview(bytes(5))
print(type(x)) # <class 'memoryview>

x = None
print(type(x)) # <class 'NoneType'>

# =======================================================
# VALID code snippets illustrating Python Numeric types !
# =======================================================

'''
Python supports three main numeric types:

a. Integers (int): Whole numbers without decimals.
b. Floating Point Numbers (float): Numbers with decimals.
c. Complex Numbers (complex): Numbers with a real and imaginary part.

'''

# 1. Integer Examples

x = 1
y = 35656222554887711
z = -3255522
print("Integer examples:")  # Integer examples:
print(x, type(x))  # 1 <class 'int'>
print(y, type(y))  # 35656222554887711 <class 'int'>
print(z, type(z))  # -3255522 <class 'int'>

# 2. Float Examples

x = 1.10
y = 1.0
z = -35.59
print("\nFloat examples:")  # Float examples:
print(x, type(x))  # 1.1 <class 'float'>
print(y, type(y))  # 1.0 <class 'float'>
print(z, type(z))  # -35.59 <class 'float'>

# 3. Scientific Notation

x = 35e3
y = 12E4
z = -87.7e100
print("\nScientific notation examples:")  # Scientific notation examples:
print(x, type(x))  # 35000.0 <class 'float'>
print(y, type(y))  # 120000.0 <class 'float'>
print(z, type(z))  # -8.77e+101 <class 'float'>

# 4. Complex Numbers

x = 3 + 5j
y = 5j
z = -5j
print("\nComplex number examples:")  # Complex number examples:
print(x, type(x))  # (3+5j) <class 'complex'>
print(y, type(y))  # 5j <class 'complex'>
print(z, type(z))  # -5j <class 'complex'>

# 5. Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)   # Convert int to float
b = int(y)     # Convert float to int
c = complex(x) # Convert int to complex
print("\nType conversions:")  # Type conversions:
print(a, type(a))  # 1.0 <class 'float'>
print(b, type(b))  # 2 <class 'int'>
print(c, type(c))  # (1+0j) <class 'complex'>

# 6. Arithmetic Operations

x = 5
y = 2
print("\nArithmetic operations:")  # Arithmetic operations:
print("Addition:", x + y)         # Addition: 7
print("Subtraction:", x - y)      # Subtraction: 3
print("Multiplication:", x * y)   # Multiplication: 10
print("Division:", x / y)         # Division: 2.5
print("Modulus:", x % y)          # Modulus: 1
print("Exponentiation:", x ** y)  # Exponentiation: 25
print("Floor division:", x // y)  # Floor division: 2

# 7. Math Module
import math
print("Square root of 16:", math.sqrt(16))  # Square root of 16: 4.0
print("2 raised to power 3:", math.pow(2, 3))  # 2 raised to power 3: 8.0
print("Value of pi:", math.pi)  # Value of pi: 3.141592653589793

# 8. Random Numbers
import random
print("Random integer 1-100:", random.randint(1, 100))  # Random integer 1-100: <varies>
print("Random float 1.0-100.0:", random.uniform(1.0, 100.0))  # Random float 1.0-100.0: <varies>

# 9. More Complex Operations (Complex Numbers)

x = complex(2, 3)  # 2 + 3j
y = complex(1, -1) # 1 - 1j
z = x + y          # Add two complex numbers
print("x + y =", z)              # x + y = (3+2j)
print("Real part of z:", z.real) # Real part of z: 3.0
print("Imaginary part of z:", z.imag) # Imaginary part of z: 2.0
print("Magnitude of z:", abs(z))       # Magnitude of z: 3.605551275463989


# ==============================================================
# INVALID code snippets for python numeric types !
# ==============================================================

# 1. Invalid Type Conversions

'''
x = "5" + 10  # TypeError: cannot concatenate str and int
x = float("hello")  # ValueError: could not convert string to float
'''

# 2. Division by Zero (Commented)
'''
result = x / 0  # ZeroDivisionError: division by zero
'''

# 3. Invalid Complex Numbers (Commented)
'''
x = 3 + 5       # Not a complex number; just int addition (valid, but not complex)
y = 5k          # SyntaxError: invalid syntax
'''

# ========================================================
# VALID code snippets illustrating "casting" in python !
# ========================================================

'''
Casting (or type conversion) in python is the process of converting a value from one data type to another.
'''

# 1. Casting to Integer

x = int(1)       # x will be 1
y = int(2.8)     # y will be 2
z = int("3")     # z will be 3
print(x, type(x))  # 1 <class 'int'>
print(y, type(y))  # 2 <class 'int'>
print(z, type(z))  # 3 <class 'int'>

# 2. Casting to Float
x = float(1)      # x will be 1.0
y = float(2.8)    # y will be 2.8
z = float("3")    # z will be 3.0
w = float("4.2")  # w will be 4.2
print(x, type(x))  # 1.0 <class 'float'>
print(y, type(y))  # 2.8 <class 'float'>
print(z, type(z))  # 3.0 <class 'float'>
print(w, type(w))  # 4.2 <class 'float'>

# 3. Casting to String
x = str("s1")  # x will be 's1'
y = str(2)     # y will be '2'
z = str(3.0)   # z will be '3.0'
print(x, type(x))  # 's1' <class 'str'>
print(y, type(y))  # '2' <class 'str'>
print(z, type(z))  # '3.0' <class 'str'>

# 4. Type Conversion Between Types
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)   # Convert int to float
b = int(y)     # Convert float to int
c = complex(x) # Convert int to complex
print(a, type(a))  # 1.0 <class 'float'>
print(b, type(b))  # 2 <class 'int'>
print(c, type(c))  # (1+0j) <class 'complex'>

# 5. Implicit Type Conversion (Type Promotion)
x = 5      # int
y = 2.0    # float
z = x + y  # int automatically becomes float
print(z, type(z))  # 7.0 <class 'float'>

# 6. Explicit Type Conversion
x = "3"   # str
y = 2     # int
z = int(x) + y  # Convert x to int before addition
print(z, type(z))  # 5 <class 'int'>

# 7. Casting with User Input

# This uses a method from the library called input, that prompts for user action. 
age = input("Enter your age: ")  # User inputs a string
age = int(age)  # Convert the input string to an integer
print("Your age is:", age)

# ===========================================================
# INVALID code snippets for "casting" in python !
# ===========================================================

# 1. Invalid Casting Examples
'''
# x = int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
# y = float("xyz")  # ValueError: could not convert string to float: 'xyz'
# z = str([1, 2, 3])  # z will be '[1, 2, 3]' <class 'str'>, but not a simple string
'''

# 2. Invalid Complex Casting
'''
# x = complex("hello")  # ValueError: complex() arg is a string that cannot be converted to a complex number
'''

# 3. Invalid Type Conversion
'''
x = "3.14" + 2  # TypeError: can only concatenate str (not "int") to str
'''
