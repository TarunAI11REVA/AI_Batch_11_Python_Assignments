# ===============================================
# Python Functions
# ===============================================

# Creating and calling a basic function
# Define a function using the 'def' keyword followed by function name and parentheses
def my_function():
# The function body is indented and contains the code to execute
# This function takes no parameters and prints a simple message
    print("Hello from a function")

# Call the function by using its name followed by parentheses
my_function()

# Output:
# Hello from a function

# Function with one argument
# Define function that accepts one parameter 'fname'
# The parameter acts as a variable inside the function
# We concatenate the parameter with a string and print it
def my_function_with_arg(fname):
    print(fname + " Refsnes")

# Call function three times with different arguments
# Each call passes a different string value to the parameter
my_function_with_arg("Emil")
my_function_with_arg("Tobias")
my_function_with_arg("Linus")

# Output:
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

# Function with two arguments
# Define function with two parameters separated by comma
def my_function_two_args(fname, lname):
# Inside function, concatenate both parameters with a space
    print(fname + " " + lname)

# Both parameters are required when calling the function
# Call function with exactly two arguments in order
my_function_two_args("Emil", "Refsnes")

# Output:
# Emil Refsnes

# Arbitrary arguments with *args
# Use asterisk (*) before parameter to accept any number of arguments
def my_function_arbitrary(*kids):
# Inside function, the parameter becomes a tuple of all passed values
# Access tuple elements using index notation
# kids[2] accesses the third element (index 2) of the tuple
    print("The youngest child is " + kids[2])

# Call function with three arguments
my_function_arbitrary("Emil", "Tobias", "Linus")

# Output:
# The youngest child is Linus

# Keyword arguments
# Define function with three parameters in specific order
# When calling, we can use parameter_name=value syntax
# This allows us to pass arguments in any order
def my_function_kwargs(child3, child2, child1):
    print("The youngest child is " + child3)

# Call with keyword arguments - order doesn't matter here
my_function_kwargs(child1="Emil", child2="Tobias", child3="Linus")

# Output:
# The youngest child is Linus

# Arbitrary keyword arguments with **kwargs
# Use double asterisk (**) before parameter for unlimited keyword arguments
# Inside function, the parameter becomes a dictionary
# Access dictionary values using keys
def my_function_arbitrary_kwargs(**kid):
    print("His last name is " + kid["lname"])

# Call function with keyword arguments as key=value pairs
# These become dictionary items inside the function
my_function_arbitrary_kwargs(fname="Tobias", lname="Refsnes")

# Output:
# His last name is Refsnes

# Default parameter values
# Assign default value to parameter using equals sign
# If no argument provided, default value is used
# If argument is provided, it overrides the default
def my_function_default(country="Norway"):
    print("I am from " + country)

# Call function with and without arguments
my_function_default("Sweden")  # Uses provided argument
my_function_default("India")   # Uses provided argument
my_function_default()          # Uses default "Norway"
my_function_default("Brazil")  # Uses provided argument

# Output:
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

# Passing a list as argument
# Define function that accepts any data type as parameter
# Use a for loop to iterate through the list
# Print each element on a separate line
def my_function_list(food):
    for x in food:
        print(x)

# Create a list of strings
# Pass the entire list to the function
fruits = ["apple", "banana", "cherry"]
my_function_list(fruits)

# Output:
# apple
# banana
# cherry

# Return values
# Define function that performs a calculation
# Use 'return' keyword to send result back to caller
# The returned value can be used in expressions or printed
def my_function_return(x):
    return 5 * x

# Call function and print returned value immediately
# Each call multiplies the argument by 5 and returns the result
print(my_function_return(3))
print(my_function_return(5))
print(my_function_return(9))

# Output:
# 15
# 25
# 45

#  The pass statement
# Sometimes you need an empty function definition
# Python doesn't allow empty code blocks, so use 'pass'
# 'pass' is a null operation - nothing happens when executed
def myfunction_pass():
    pass

# Function can be called but does nothing
myfunction_pass()

# Output:
# (no output - function does nothing)

#  Positional-only arguments
# Add ', /' after parameters to enforce positional-only
# This means arguments must be passed by position, not by keyword
# Function accepts the value and prints it
def my_function_pos_only(x, /):
    print(x)

# Call with positional argument (this works)
my_function_pos_only(3)

# Output:
# 3

#  Keyword-only arguments
# Add '*, ' before parameters to enforce keyword-only
# This means arguments must be passed by keyword, not by position
# Function accepts the value and prints it
def my_function_kwd_only(*, x):
    print(x)

# Call with keyword argument (this works)
my_function_kwd_only(x=3)

# Output:
# 3

#  Combining positional-only and keyword-only
# Parameters before '/' are positional-only
# Parameters after '*' are keyword-only
# This gives precise control over how function is called
def my_function_combined(a, b, /, *, c, d):
    print(a + b + c + d)

# First two arguments must be positional, last two must be keyword
my_function_combined(5, 6, c=7, d=8)

# Output:
# 26

#  Function with one argument - detailed
# Define function with single parameter 'fname'
# Concatenate parameter with string " Refsnes"
# Print the result
def my_function_detailed(fname):
    print(fname + " Refsnes")

# Call function multiple times with different first names
my_function_detailed("Emil")
my_function_detailed("Tobias")
my_function_detailed("Linus")

# Output:
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

#  Default parameter values - detailed
# Set default value "friend" for parameter 'name'
# If argument is provided, it overrides the default
# If no argument, default value is used
def my_function_default_detailed(name="friend"):
    print("Hello", name)

# Call with various arguments and without argument
my_function_default_detailed("Emil")    # Uses "Emil"
my_function_default_detailed("Tobias")  # Uses "Tobias"
my_function_default_detailed()          # Uses default "friend"
my_function_default_detailed("Linus")   # Uses "Linus"

# Output:
# Hello Emil
# Hello Tobias
# Hello friend
# Hello Linus

#  Default country parameter
# Set default value "Norway" for parameter 'country'
# Print a message using the country value
def my_function_country(country="Norway"):
    print("I am from", country)

# Call function with different countries and without argument
my_function_country("Sweden")  # Override with "Sweden"
my_function_country("India")   # Override with "India"
my_function_country()          # Use default "Norway"
my_function_country("Brazil")  # Override with "Brazil"

# Output:
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

#  Keyword arguments with two parameters
# Define function with two parameters: animal and name
# Print information using both parameters
def my_function_animal(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

# Call using keyword arguments - order doesn't matter
my_function_animal(animal="dog", name="Buddy")

# Output:
# I have a dog
# My dog's name is Buddy

#  Keyword arguments in different order
# Same function definition as above
# Call with keywords in reverse order to demonstrate order independence
def my_function_animal2(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

# Pass name before animal - still works correctly
my_function_animal2(name="Buddy", animal="dog")

# Output:
# I have a dog
# My dog's name is Buddy

#  Positional arguments
# Define function with two parameters
# When called without keywords, position matters
def my_function_positional(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

# Pass arguments by position - first is animal, second is name
my_function_positional("dog", "Buddy")

# Output:
# I have a dog
# My dog's name is Buddy

#  Wrong positional argument order
# Same function as above
# Swap the order of arguments to show importance of position
def my_function_wrong_order(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

# Pass arguments in wrong order - produces incorrect output
my_function_wrong_order("Buddy", "dog")

# Output:
# I have a Buddy
# My Buddy's name is dog

#  Mixing positional and keyword arguments
# Define function with three parameters
# First argument is positional, remaining are keyword
def my_function_mixed(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

# Pass first argument positionally, others as keywords
my_function_mixed("dog", name="Buddy", age=5)

# Output:
# I have a 5 year old dog named Buddy
#  Passing a list to a function
# Define function that expects a list
# Iterate through the list and print each element
def my_function_fruits(fruits):
    for fruit in fruits:
        print(fruit)

# Create a list of fruits
# Pass the list to the function
my_fruits = ["apple", "banana", "cherry"]
my_function_fruits(my_fruits)

# Output:
# apple
# banana
# cherry

#  Passing a dictionary to a function
# Define function that expects a dictionary
# Access dictionary values using keys and print them
def my_function_dict(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

# Create a dictionary with person information
# Pass the dictionary to the function
my_person = {"name": "Emil", "age": 25}
my_function_dict(my_person)

# Output:
# Name: Emil
# Age: 25

#  Returning values from function
# Define function that takes two parameters
# Add them together and return the sum
def my_function_add(x, y):
    return x + y

# Call function and store result in variable
# Print the returned result
result = my_function_add(5, 3)
print(result)

# Output:
# 8

#  Returning a list
# Define function that returns a list
# Create and return a list inside the function
def my_function_return_list():
    return ["apple", "banana", "cherry"]

# Call function and store returned list
# Access and print individual elements
fruits = my_function_return_list()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Output:
# apple
# banana
# cherry

#  Returning a tuple
# Define function that returns a tuple with two values
# Return multiple values separated by comma (creates tuple)
def my_function_return_tuple():
    return (10, 20)

# Call function and unpack tuple into two variables
# Print both unpacked values
x, y = my_function_return_tuple()
print("x:", x)
print("y:", y)

# Output:
# x: 10
# y: 20

#  Using *args
# Use *kids to accept any number of positional arguments
# Inside function, kids becomes a tuple
# Access tuple element at index 2 (third element)
def my_function_args(*kids):
    print("The youngest child is " + kids[2])

# Call with three arguments - they form a tuple
my_function_args("Emil", "Tobias", "Linus")

# Output:
# The youngest child is Linus

#  Understanding *args type
# Use *args to accept variable number of arguments
# Print the type of args (will be tuple)
# Access and print individual arguments by index
# Print all arguments together
def my_function_args_type(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

# Call with three string arguments
my_function_args_type("Emil", "Tobias", "Linus")

# Output:
# Type: <class 'tuple'>
# First argument: Emil
# Second argument: Tobias
# All arguments: ('Emil', 'Tobias', 'Linus')

#  *args with regular arguments
# Combine regular parameter 'greeting' with *args
# First argument goes to 'greeting', rest go to 'names' tuple
# Loop through names and print greeting for each
def my_function_args_regular(greeting, *names):
    for name in names:
        print(greeting, name)

# First argument "Hello" goes to greeting parameter
# Remaining arguments form the names tuple
my_function_args_regular("Hello", "Emil", "Tobias", "Linus")

# Output:
# Hello Emil
# Hello Tobias
# Hello Linus

#  Sum function with *args
# Accept any number of numeric arguments with *numbers
# Initialize total to 0
# Loop through all numbers and add each to total
# Return the final sum
def sum_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Call function with different numbers of arguments
print(sum_function(1, 2, 3))           # Sum of 3 numbers
print(sum_function(10, 20, 30, 40))    # Sum of 4 numbers
print(sum_function(5))                 # Sum of 1 number

# Output:
# 6
# 100
# 5

#  Finding maximum with *args
# Accept any number of arguments with *numbers
# Check if no arguments provided, return None
# Initialize max_num with first element
# Loop through all numbers comparing each with max_num
# Update max_num if current number is larger
# Return the maximum number found
def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Call function with multiple numbers
print(find_max(3, 7, 2, 9, 1))

# Output:
# 9

#  Using **kwargs
# Use **kid to accept any number of keyword arguments
# Inside function, kid becomes a dictionary
# Access dictionary value using key "lname"
def my_function_kwargs_basic(**kid):
    print("His last name is " + kid["lname"])

# Call with keyword arguments as key=value pairs
my_function_kwargs_basic(fname="Tobias", lname="Refsnes")

# Output:
# His last name is Refsnes

#  Understanding **kwargs type
# Use **myvar to accept any number of keyword arguments
# Print the type of myvar (will be dict)
# Access and print specific dictionary values
# Print entire dictionary
def my_function_kwargs_type(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

# Call with multiple keyword arguments
my_function_kwargs_type(name="Tobias", age=30, city="Bergen")

# Output:
# Type: <class 'dict'>
# Name: Tobias
# Age: 30
# All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

#  **kwargs with regular arguments
# Combine regular parameter 'username' with **kwargs
# First argument goes to username, rest become dictionary
# Print username and then iterate through details dictionary
def my_function_kwargs_regular(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print("  ", key + ":", value)

# First argument goes to username parameter
# Keyword arguments form the details dictionary
my_function_kwargs_regular("emil123", age=25, city="Oslo", hobby="coding")

# Output:
# Username: emil123
# Additional details:
#    age: 25
#    city: Oslo
#    hobby: coding

#  Combining *args and **kwargs
# Use regular parameter, *args, and **kwargs together
# Regular parameter must come first
# *args captures positional arguments
# **kwargs captures keyword arguments
def my_function_both(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# First arg goes to title, next two to args, rest to kwargs
my_function_both("User Info", "Emil", "Tobias", age=25, city="Oslo")

# Output:
# Title: User Info
# Positional arguments: ('Emil', 'Tobias')
# Keyword arguments: {'age': 25, 'city': 'Oslo'}

#  Unpacking list with *
# Define function expecting three parameters
# Function adds all three parameters
def my_function_unpack(a, b, c):
    return a + b + c

# Create a list with three numbers
# Use * to unpack list into separate arguments
numbers = [1, 2, 3]
result = my_function_unpack(*numbers)  # Same as: my_function_unpack(1, 2, 3)
print(result)

# Output:
# 6

#  Unpacking dictionary with **
# Define function with two parameters
# Function prints full name using both parameters
def my_function_unpack_dict(fname, lname):
    print("Hello", fname, lname)

# Create dictionary with keys matching parameter names
# Use ** to unpack dictionary into keyword arguments
person = {"fname": "Emil", "lname": "Refsnes"}
my_function_unpack_dict(**person)  # Same as: my_function_unpack_dict(fname="Emil", lname="Refsnes")

# Output:
# Hello Emil Refsnes

#  Basic lambda function
# Create lambda function that takes one argument 'a'
# Lambda returns a + 10 (adds 10 to the argument)
# Store the lambda function in variable 'x'
x = lambda a: a + 10

# Call the lambda by using variable name with parentheses
# Pass 5 as argument, result is 5 + 10 = 15
print(x(5))

# Output:
# 15

#  Lambda with two arguments
# Create lambda that takes two arguments 'a' and 'b'
# Lambda multiplies a and b and returns result
# Store lambda in variable 'x'
x = lambda a, b: a * b

# Call lambda with two arguments: 5 and 6
# Result is 5 * 6 = 30
print(x(5, 6))

# Output:
# 30

#  Lambda with three arguments
# Create lambda that takes three arguments
# Lambda adds all three arguments together
# Store lambda in variable 'x'
x = lambda a, b, c: a + b + c

# Call lambda with three arguments: 5, 6, and 2
# Result is 5 + 6 + 2 = 13
print(x(5, 6, 2))

# Output:
# 13

#  Lambda inside a function - doubler
# Define function that takes parameter 'n'
# Function returns a lambda that multiplies its argument by n
# This creates a closure where lambda remembers value of n
def myfunc(n):
    return lambda a: a * n

# Call myfunc(2) to create a doubler function
# Returned lambda will multiply its argument by 2
mydoubler = myfunc(2)

# Call the doubler with 11
# Result is 11 * 2 = 22
print(mydoubler(11))

# Output:
# 22

#  Lambda inside a function - tripler
# Use same function definition as above
# Call myfunc(3) to create a tripler function
# Returned lambda will multiply its argument by 3
def myfunc2(n):
    return lambda a: a * n

mytripler = myfunc2(3)

# Call the tripler with 11
# Result is 11 * 3 = 33
print(mytripler(11))

# Output:
# 33

#  Creating both doubler and tripler
# Use same function to create multiple functions
# Create doubler by passing 2
# Create tripler by passing 3
def myfunc3(n):
    return lambda a: a * n

mydoubler = myfunc3(2)
mytripler = myfunc3(3)

# Call both functions with same argument (11)
# Doubler returns 11 * 2 = 22
# Tripler returns 11 * 3 = 33
print(mydoubler(11))
print(mytripler(11))

# Output:
# 22
# 33

#  Local scope
# Define function with local variable 'x'
# Variable x is created inside function (local scope)
# Variable is only accessible inside the function
def myfunc_local():
    x = 300
    print(x)

# Call function to print local variable
myfunc_local()

# Output:
# 300

#  Function inside function
# Outer function creates local variable x = 300
# Inner function can access outer function's variable
# This demonstrates nested scope
def myfunc_nested():
    x = 300
    # Define inner function inside outer function
    def myinnerfunc():
        # Inner function can access x from outer function
        print(x)
    # Call inner function
    myinnerfunc()

# Call outer function which calls inner function
myfunc_nested()

# Output:
# 300

#  Global scope
# Create variable x in global scope (outside any function)
x = 300

# Define function that accesses global variable
def myfunc_global():
    # Function can read global variable x
    print(x)

# Call function to print global variable
myfunc_global()

# Print global variable directly
print(x)

# Output:
# 300
# 300

#  Local vs global variable with same name
# Create global variable x = 300
x = 300

# Define function with local variable also named x
def myfunc_different():
    # This x is local to function (x = 200)
    x = 200
    # Function prints its local x
    print(x)

# Call function - prints local x (200)
myfunc_different()

# Print global x - still 300 (unchanged)
print(x)

# Output:
# 200
# 300

#  Using global keyword to create global variable
# Define function that creates global variable
def myfunc_global_keyword():
    # Use 'global' keyword to declare x as global
    # This makes x accessible outside the function
    global x
    x = 300

# Call function to create global variable x
myfunc_global_keyword()

# Print x outside function - works because x is global
print(x)

# Output:
# 300

#  Modifying global variable with global keyword
# Create global variable x = 300
x = 300

# Define function that modifies global variable
def myfunc_modify_global():
    # Use 'global' keyword to reference global x
    global x
    # Modify the global variable
    x = 200

# Call function to modify global x
myfunc_modify_global()

# Print x - shows modified value (200)
print(x)

# Output:
# 200

# Basic Decorator
# Think of a decorator as a wrapper that modifies how a function works
# It's like gift wrapping - you're adding something extra around the original

# First, we create our decorator function called 'changecase'
# This decorator will take any function and make its output UPPERCASE
def changecase(func):
    # Inside the decorator, we create a new function called 'myinner'
    # This is the wrapper that will replace the original function
    def myinner():
        # Call the original function and convert result to uppercase
        return func().upper()
    # Return this new wrapped function
    return myinner

# Now we use the decorator with @ symbol
# Think of @ as saying "wrap this function with changecase"
@changecase
def myfunction():
    return "Hello Sally"

# When we call myfunction(), it actually calls the wrapped version
# So "Hello Sally" becomes "HELLO SALLY"
print(myfunction())

# Output:
# HELLO SALLY


# Using Same Decorator Multiple Times
# You can reuse the same decorator on different functions
# It's like using the same gift wrap for multiple presents

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

# Decorate first function
@changecase
def myfunction():
    return "Hello Sally"

# Decorate second function with the same decorator
@changecase
def otherfunction():
    return "I am speed!"

# Both functions now return uppercase text
print(myfunction())
print(otherfunction())

# Output:
# HELLO SALLY
# I AM SPEED!


# Decorator with Function Arguments
# What if the function we want to decorate needs arguments?
# We need to pass those arguments through the wrapper

def changecase(func):
    # The wrapper function now accepts an argument 'x'
    def myinner(x):
        # Pass the argument to the original function, then uppercase the result
        return func(x).upper()
    return myinner

# This function takes a name as argument
@changecase
def myfunction(nam):
    return "Hello " + nam

# When we call it with "John", it returns "HELLO JOHN"
print(myfunction("John"))

# Output:
# HELLO JOHN

# Using *args and **kwargs for Flexibility
# What if we don't know how many arguments the function will take?
# Use *args and **kwargs to handle any combination of arguments

def changecase(func):
    # This wrapper can now accept ANY number of arguments
    # *args catches positional arguments, **kwargs catches keyword arguments
    def myinner(*args, **kwargs):
        # Pass all arguments to the original function
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

# Still works the same way
print(myfunction("John"))

# Output:
# HELLO JOHN

# Decorator with Arguments
# Sometimes you want the decorator itself to take arguments
# This requires an extra layer - it's like a decorator factory

# Outer function takes the decorator's argument 'n'
def changecase(n):
    # Middle function is the actual decorator
    def changecase(func):
        # Inner function is the wrapper
        def myinner():
            # If n is 1, convert to lowercase
            if n == 1:
                a = func().lower()
            # Otherwise, convert to uppercase
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

# We call the decorator with an argument (1)
# This means use lowercase
@changecase(1)
def myfunction():
    return "Hello Linus"

# Result is lowercase because we passed 1 to the decorator
print(myfunction())

# Output:
# hello linus

# Multiple Decorators on One Function
# You can stack decorators - they apply from bottom to top
# Think of it like putting on multiple layers of clothing

# First decorator: converts to uppercase
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

# Second decorator: adds greeting text around the result
def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

# Apply decorators - order matters!
# First addgreeting wraps the function, then changecase wraps that
@changecase
@addgreeting
def myfunction():
    return "Tobias"

# Step by step:
# 1. myfunction() returns "Tobias"
# 2. addgreeting adds text: "Hello Tobias Have a good day!"
# 3. changecase makes it uppercase: "HELLO TOBIAS HAVE A GOOD DAY!"
print(myfunction())

# Output:
# HELLO TOBIAS HAVE A GOOD DAY!

# Function Metadata - The Problem
# Functions in Python have metadata like their name
# Without decoration, you can access the function name

def myfunction():
    return "Have a great day!"

# This prints the function's name
print(myfunction.__name__)

# Output:
# myfunction

# Decorated Function Loses Metadata
# When you decorate a function, it loses its original metadata
# The name becomes the wrapper's name instead

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Have a great day!"

# This prints 'myinner' instead of 'myfunction'
# Because myfunction is now replaced by the myinner wrapper
print(myfunction.__name__)

# Output:
# myinner

# Preserving Metadata with functools.wraps
# To fix the metadata problem, use functools.wraps
# This copies the original function's metadata to the wrapper

import functools

def changecase(func):
    # Add @functools.wraps(func) to preserve metadata
    # This copies __name__, __doc__, etc. from func to myinner
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Have a great day!"

# Now this correctly prints 'myfunction'
# The wrapper keeps the original function's name
print(myfunction.__name__)

# Output:
# myfunction

"""
Python Lambda Functions, Recursion, and Generators
Complete Examples from W3Schools with Simple Explanations
"""

# Basic Lambda Function
# Lambda is like a mini function that you write in one line
# Think of it as a shortcut when you need a simple function quickly
# Syntax: lambda arguments : expression

# Create a lambda that adds 10 to whatever number you give it
x = lambda a: a + 10

# Call the lambda by using the variable name like a function
# Give it 5, it returns 5 + 10 = 15
print(x(5))

# Output:
# 15

# Lambda with Two Arguments
# Lambda can take multiple arguments, just separate them with commas

# This lambda multiplies two numbers together
x = lambda a, b: a * b

# Pass two numbers: 5 and 6
# It calculates 5 * 6 = 30
print(x(5, 6))

# Output:
# 30

# Lambda with Three Arguments
# You can have as many arguments as you need

# This lambda adds three numbers together
x = lambda a, b, c: a + b + c

# Pass three numbers: 5, 6, and 2
# It calculates 5 + 6 + 2 = 13
print(x(5, 6, 2))

# Output:
# 13

# Lambda Inside a Function - Creating a Doubler
# This is where lambda really shines!
# We can create functions that make other functions

# This function creates custom multipliers
# Whatever number you pass in 'n', it makes a multiplier for that
def myfunc(n):
    # Return a lambda that multiplies by n
    return lambda a: a * n

# Create a doubler (multiplies by 2)
mydoubler = myfunc(2)

# Now use the doubler to double 11
# 11 * 2 = 22
print(mydoubler(11))

# Output:
# 22

# Lambda Inside a Function - Creating a Tripler
# Same function, but now we create a tripler

def myfunc(n):
    return lambda a: a * n

# Create a tripler (multiplies by 3)
mytripler = myfunc(3)

# Use the tripler to triple 11
# 11 * 3 = 33
print(mytripler(11))

# Output:
# 33

# Creating Multiple Lambda Functions
# You can create different functions from the same template

def myfunc(n):
    return lambda a: a * n

# Create both a doubler and a tripler
mydoubler = myfunc(2)
mytripler = myfunc(3)

# Use both of them
print(mydoubler(11))  # 11 * 2 = 22
print(mytripler(11))  # 11 * 3 = 33

# Output:
# 22
# 33

# Simple Countdown using Recursion
# Recursion is when a function calls itself
# It's like looking in a mirror that reflects another mirror

# This function counts down from a number to zero
def countdown(n):
    # Base case: stop when we reach 0 or below
    if n <= 0:
        print("Done!")
    else:
        # Print current number
        print(n)
        # Call itself with n-1 (recursive case)
        countdown(n - 1)

# Start counting down from 5
countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1
# Done!

# Factorial using Recursion
# Factorial means: 5! = 5 * 4 * 3 * 2 * 1 = 120
# Recursion is perfect for this!

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    # This is where recursion stops
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    # Function calls itself with a smaller number
    else:
        return n * factorial(n - 1)

# Calculate 5! = 5 * 4 * 3 * 2 * 1 = 120
print(factorial(5))

# Output:
# 120

# Fibonacci Sequence using Recursion
# Fibonacci: each number is the sum of the previous two
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(n):
    # Base case: first two numbers are 0 and 1
    if n <= 1:
        return n
    else:
        # Each number is sum of previous two
        # This calls the function twice for each step
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get the 7th Fibonacci number
# 0, 1, 1, 2, 3, 5, 8, 13
# The 7th number (index 7) is 13
print(fibonacci(7))

# Output:
# 13

# Summing a List with Recursion
# Instead of using a loop, we can sum a list recursively

def sum_list(numbers):
    # Base case: empty list sums to 0
    if len(numbers) == 0:
        return 0
    else:
        # Add first number to sum of the rest
        # numbers[0] is first element
        # numbers[1:] is everything except first element
        return numbers[0] + sum_list(numbers[1:])

# Sum the list [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# Output:
# 15

# Finding Maximum in a List with Recursion
# Find the biggest number in a list recursively

def find_max(numbers):
    # Base case: if only one number, that's the max
    if len(numbers) == 1:
        return numbers[0]
    else:
        # Find max of remaining numbers
        max_of_rest = find_max(numbers[1:])
        # Compare first number with max of rest
        # Return whichever is bigger
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest

# Find max in [3, 7, 2, 9, 1]
my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

# Output:
# 9

# Checking Recursion Limit
# Python has a safety limit to prevent infinite recursion
# Default is usually around 1000 calls

import sys

# Check what the current recursion limit is
print(sys.getrecursionlimit())

# Output:
# 1000 (or similar, depends on your system)

# Setting Recursion Limit
# You can increase the limit, but be careful!
# Too deep recursion can crash your program

import sys

# Increase limit to 2000
sys.setrecursionlimit(2000)

# Check the new limit
print(sys.getrecursionlimit())

# Output:
# 2000

# Simple Generator
# Generators are special functions that can pause and resume
# They use 'yield' instead of 'return'
# Think of it like a conveyor belt that delivers one item at a time

def my_generator():
    yield 1  # First time called, returns 1 and pauses here
    yield 2  # Next time called, returns 2 and pauses here
    yield 3  # Next time called, returns 3 and stops

# Use a for loop to get all values from the generator
for value in my_generator():
    print(value)

# Output:
# 1
# 2
# 3

# Generator that Counts Up
# This generator counts from 1 to n

def count_up_to(n):
    count = 1
    # Keep looping until we reach n
    while count <= n:
        # Yield the current count and pause
        yield count
        # Increment for next time
        count += 1

# Count from 1 to 5
for num in count_up_to(5):
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# Memory-Efficient Generator
# Generators don't store all values in memory
# They generate values one at a time as needed

def large_sequence(n):
    # This could be a million numbers
    # But it doesn't create them all at once
    for i in range(n):
        yield i

# Create a generator for 1 million numbers
# This doesn't use much memory!
gen = large_sequence(1000000)

# Get values one at a time using next()
print(next(gen))  # Gets first value: 0
print(next(gen))  # Gets second value: 1
print(next(gen))  # Gets third value: 2

# Output:
# 0
# 1
# 2

# Using next() with Generators
# You can manually get the next value from a generator

def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"

# Create the generator
gen = simple_gen()

# Get each name one by one
print(next(gen))  # First yield: "Emil"
print(next(gen))  # Second yield: "Tobias"
print(next(gen))  # Third yield: "Linus"

# Output:
# Emil
# Tobias
# Linus

# StopIteration Exception
# When a generator runs out of values, it raises StopIteration
# This happens automatically in loops, but manually with next() you'll see it

def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(next(gen))  # Returns 1
print(next(gen))  # Returns 2
# print(next(gen))  # This would raise StopIteration error!

# Output:
# 1
# 2

# Generator Expression vs List Comprehension
# Generator expressions look like list comprehensions but use parentheses

# List comprehension: creates entire list in memory immediately
list_comp = [x * x for x in range(5)]
print(list_comp)  # Shows the actual list

# Generator expression: creates generator object, values on demand
gen_exp = (x * x for x in range(5))
print(gen_exp)  # Shows generator object, not values
print(list(gen_exp))  # Convert to list to see values

# Output:
# [0, 1, 4, 9, 16]
# <generator object <genexpr> at 0x...>
# [0, 1, 4, 9, 16]

# Generator Expression with sum()
# Generator expressions are great with functions like sum()
# No need to create a full list, just generate and sum on the fly

# Calculate sum of squares from 0 to 9
# 0^2 + 1^2 + 2^2 + ... + 9^2
total = sum(x * x for x in range(10))
print(total)

# Output:
# 285

# Infinite Fibonacci Generator
# Generators can run forever!
# This creates Fibonacci numbers endlessly

def fibonacci():
    a, b = 0, 1
    # Infinite loop - but it's okay because it's a generator
    while True:
        yield a  # Give current Fibonacci number
        # Calculate next Fibonacci number
        a, b = b, a + b

# Create the generator
gen = fibonacci()

# Get just the first 10 Fibonacci numbers
# We could get as many as we want without running out of memory
for _ in range(10):
    print(next(gen))

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# Generator send() Method
# You can send values back into a generator while it's running
# This is advanced but very powerful

def echo_generator():
    while True:
        # Wait to receive a value
        received = yield
        # Print what was received
        print("Received:", received)

# Create generator
gen = echo_generator()

# Prime the generator (start it up)
next(gen)

# Now send values to it
gen.send("Hello")  # Sends "Hello" to the generator
gen.send("World")  # Sends "World" to the generator

# Output:
# Received: Hello
# Received: World

# Generator close() Method
# You can manually stop a generator

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        # This runs when generator is closed
        print("Generator closed")

# Create generator
gen = my_gen()

# Get first value
print(next(gen))

# Close the generator early (before getting all values)
gen.close()

# Output:
# 1
# Generator closed

# Creating a range with one argument
# When you give range() just one number, it counts from 0 up to (but not including) that number
# Think of it like a number generator that stops right before your number

x = range(10)

# To see what's in the range, we convert it to a list
# This creates numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(x))

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creating a range with two arguments
# First number is where to start, second is where to stop (not included)
# It's like saying "start here, stop before there"

x = range(3, 10)

# This creates numbers starting from 3 and stopping before 10
# So we get: 3, 4, 5, 6, 7, 8, 9
print(list(x))

# Output:
# [3, 4, 5, 6, 7, 8, 9]

# Creating a range with three arguments (step)
# Third argument is the "step" - how much to jump each time
# Like counting by 2s or 3s instead of 1s

x = range(3, 10, 2)

# Start at 3, stop before 10, jump by 2 each time
# So we get: 3, 5, 7, 9
print(list(x))

# Output:
# [3, 5, 7, 9]

# Using range in a for loop
# This is where range really shines - perfect for loops!
# We don't need to create a list, we just loop through the numbers

for i in range(10):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Different ways to display ranges
# You can create different patterns by changing the arguments

# Range from 0 to 4
print(list(range(5)))

# Range from 1 to 5
print(list(range(1, 6)))

# Range from 5 to 19, jumping by 3
print(list(range(5, 20, 3)))

# Output:
# [0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [5, 8, 11, 14, 17]

# Slicing a range
# You can access parts of a range using index notation

r = range(10)

# Get the element at index 2
print(r[2])

# Get elements from start up to (but not including) index 3
print(list(r[:3]))

# Output:
# 2
# [0, 1, 2]

# Testing membership in a range
# Check if a number exists in a range using 'in'

r = range(0, 10, 2)

# This range has: 0, 2, 4, 6, 8
# Check if 6 is in the range
print(6 in r)

# Check if 7 is in the range
print(7 in r)

# Output:
# True
# False

# Getting the length of a range
# Use len() to find out how many numbers are in a range

r = range(0, 10, 2)

# This range has: 0, 2, 4, 6, 8 (5 numbers total)
print(len(r))

# Output:
# 5

# Creating an array (list)
# In Python, we typically use lists instead of arrays
# A list can hold multiple values under one name

cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Output:
# ['Ford', 'Volvo', 'BMW']

# Accessing array elements
# Use index numbers to get specific elements
# Remember: index starts at 0!

cars = ["Ford", "Volvo", "BMW"]

# Get the first element (index 0)
x = cars[0]
print(x)

# Output:
# Ford

# Modifying array elements
# You can change values by assigning to an index

cars = ["Ford", "Volvo", "BMW"]

# Change the first element
cars[0] = "Toyota"
print(cars)

# Output:
# ['Toyota', 'Volvo', 'BMW']

# Getting array length
# len() tells you how many elements are in the array

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# Output:
# 3

# Looping through an array
# Use a for loop to go through each element one by one

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)

# Output:
# Ford
# Volvo
# BMW

# Adding elements to an array
# append() adds a new element to the end of the array

cars = ["Ford", "Volvo", "BMW"]

# Add "Honda" to the end
cars.append("Honda")
print(cars)

# Output:
# ['Ford', 'Volvo', 'BMW', 'Honda']

# Removing elements with pop()
# pop() removes an element at a specific index
# If you don't specify index, it removes the last element

cars = ["Ford", "Volvo", "BMW"]

# Remove element at index 1 (second element)
cars.pop(1)
print(cars)

# Output:
# ['Ford', 'BMW']

# Removing elements with remove()
# remove() deletes the first occurrence of a specific value

cars = ["Ford", "Volvo", "BMW"]

# Remove the element with value "Volvo"
cars.remove("Volvo")
print(cars)

# Output:
# ['Ford', 'BMW']

# Creating an iterator from a tuple
# An iterator lets you go through items one at a time
# Use iter() to create an iterator, next() to get each item

mytuple = ("apple", "banana", "cherry")

# Create an iterator from the tuple
myit = iter(mytuple)

# Get each item using next()
print(next(myit))  # Gets first item
print(next(myit))  # Gets second item
print(next(myit))  # Gets third item

# Output:
# apple
# banana
# cherry

# Iterator from a string
# Even strings can be turned into iterators!
# Each character becomes a separate item

mystr = "banana"

# Create iterator from string
myit = iter(mystr)

# Get each character one by one
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Output:
# b
# a
# n
# a
# n
# a

# Looping through an iterator with for loop
# You don't need to manually call next() in a for loop
# The for loop handles the iterator automatically

mytuple = ("apple", "banana", "cherry")

# Loop automatically creates an iterator and gets each item
for x in mytuple:
    print(x)

# Output:
# apple
# banana
# cherry

# Looping through string characters
# Strings are iterable, so you can loop through their characters

mystr = "banana"

# Loop through each character
for x in mystr:
    print(x)

# Output:
# b
# a
# n
# a
# n
# a

# Creating a custom iterator class
# You can make your own iterator by defining __iter__() and __next__()
# This is like building your own number generator

class MyNumbers:
    # __iter__() is called when iterator is created
    def __iter__(self):
        # Initialize starting number
        self.a = 1
        # Must return the iterator object (self)
        return self
    
    # __next__() is called to get the next value
    def __next__(self):
        # Get current number
        x = self.a
        # Increment for next time
        self.a += 1
        # Return the current number
        return x

# Create an instance of our iterator class
myclass = MyNumbers()

# Get the iterator
myiter = iter(myclass)

# Get values one by one
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Output:
# 1
# 2
# 3
# 4
# 5

# StopIteration - preventing infinite iteration
# Without a stop condition, an iterator would run forever
# Use StopIteration to tell Python when to stop

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        # Stop after 20 iterations
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            # Raise StopIteration to end the iteration
            raise StopIteration

# Create iterator
myclass = MyNumbers()
myiter = iter(myclass)

# Use in a for loop - it will automatically stop at 20
for x in myiter:
    print(x)

# Output:
# 1
# 2
# 3
# ... (continues up to)
# 20

# Importing a built-in module
# Modules are like toolboxes - they contain functions you can use
# Python has many built-in modules you can import

import platform

# Use a function from the platform module
# This tells us which operating system we're using
x = platform.system()
print(x)

# Output:
# Windows (or Linux, or Darwin for Mac)

# Using variables from a module
# Some modules contain predefined variables and data

import platform

# Access the version information
x = platform.python_version()
print(x)

# Output:
# 3.11.0 (or your Python version)

# Importing specific functions
# Instead of importing everything, import just what you need
# This uses "from module import function" syntax

from datetime import datetime

# Now we can use datetime directly without the module name
now = datetime.now()
print(now)

# Output:
# 2024-11-14 15:30:45.123456 (current date and time)

# Creating your own module
# You can create a module by saving Python code in a .py file
# Then import it just like built-in modules

# Let's say we have a file called mymodule.py with this code:
# def greeting(name):
#     print("Hello, " + name)

# Then in another file, we can import and use it:
# import mymodule
# mymodule.greeting("Jonathan")

# Output (when run):
# Hello, Jonathan

# Using module aliases
# Give modules shorter names to type less
# Use "import module as alias" syntax

import datetime as dt

# Now use 'dt' instead of typing 'datetime' every time
now = dt.datetime.now()
print(now.year)

# Output:
# 2024 (current year)

# Getting current date and time
# The datetime module lets you work with dates and times

import datetime

# Get the current date and time
x = datetime.datetime.now()
print(x)

# Output:
# 2024-11-14 15:30:45.123456 (current date and time)

# Accessing date parts
# You can get specific parts of a date like year, month, day

import datetime

x = datetime.datetime.now()

# Get individual parts of the date
print(x.year)        # The year
print(x.month)       # The month (1-12)
print(x.day)         # The day (1-31)
print(x.hour)        # The hour (0-23)
print(x.minute)      # The minute (0-59)

# Output:
# 2024
# 11
# 14
# 15
# 30

# Getting day of the week
# strftime() formats dates as strings using format codes

import datetime

x = datetime.datetime.now()

# %A gives the full weekday name
print(x.strftime("%A"))

# Output:
# Thursday (or whatever day it is)

# Creating a specific date
# You can create a date object for any date you want

import datetime

# Create a date for May 17, 2020
x = datetime.datetime(2020, 5, 17)
print(x)

# Output:
# 2020-05-17 00:00:00

# Formatting dates
# Use format codes to display dates in different ways

import datetime

x = datetime.datetime(2024, 6, 15)

# %B = full month name, %d = day, %Y = full year
print(x.strftime("%B %d, %Y"))

# %m = month as number, %d = day, %y = short year
print(x.strftime("%m/%d/%y"))

# Output:
# June 15, 2024
# 06/15/24

# Finding minimum and maximum
# min() and max() find the smallest and largest numbers

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# Output:
# 5
# 25

# Absolute value
# abs() gives you the absolute value (always positive)

x = abs(-7.25)
print(x)

# Output:
# 7.25

# Power function
# pow(x, y) calculates x to the power of y

x = pow(4, 3)  # Same as 4 * 4 * 4
print(x)

# Output:
# 64

# Using the math module
# The math module has many more mathematical functions

import math

# Square root
x = math.sqrt(64)
print(x)

# Output:
# 8.0

# Rounding numbers
# ceil() rounds up, floor() rounds down

import math

x = math.ceil(1.4)   # Round up to next integer
y = math.floor(1.4)  # Round down to previous integer

print(x)
print(y)

# Output:
# 2
# 1

# Pi constant
# Access mathematical constants like pi

import math

x = math.pi
print(x)

# Output:
# 3.141592653589793

# Converting JSON to Python (parsing)
# JSON is a text format for storing and exchanging data
# Use json.loads() to convert JSON string to Python dictionary

import json

# A JSON string (looks like JavaScript object notation)
x = '{ "name":"John", "age":30, "city":"New York"}'

# Parse the JSON string into a Python dictionary
y = json.loads(x)

# Now we can access it like a regular Python dictionary
print(y["age"])

# Output:
# 30

# Converting Python to JSON
# Use json.dumps() to convert Python objects to JSON strings

import json

# A Python dictionary
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
y = json.dumps(x)
print(y)

# Output:
# {"name": "John", "age": 30, "city": "New York"}

# Converting different Python objects to JSON
# You can convert lists, tuples, dictionaries, etc. to JSON

import json

# Dictionary
print(json.dumps({"name": "John", "age": 30}))

# List
print(json.dumps(["apple", "bananas"]))

# Tuple (converts to JSON array)
print(json.dumps(("apple", "bananas")))

# String
print(json.dumps("hello"))

# Integer
print(json.dumps(42))

# Float
print(json.dumps(31.76))

# Boolean
print(json.dumps(True))

# None becomes null in JSON
print(json.dumps(None))

# Output:
# {"name": "John", "age": 30}
# ["apple", "bananas"]
# ["apple", "bananas"]
# "hello"
# 42
# 31.76
# true
# null

# Formatting JSON output
# Make JSON more readable with indentation

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann","Billy")
}

# Use indent parameter to make it pretty
# separators remove extra spaces
print(json.dumps(x, indent=4, separators=(", ", " = ")))

# Output:
# {
#     "name" = "John",
#     "age" = 30,
#     "married" = true,
#     "children" = [
#         "Ann",
#         "Billy"
#     ]
# }

# Sorting JSON keys
# Use sort_keys=True to sort dictionary keys alphabetically

import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Sort the keys alphabetically
print(json.dumps(x, indent=4, sort_keys=True))

# Output:
# {
#     "age": 30,
#     "city": "New York",
#     "name": "John"
# }

# Basic try-except
# try lets you test code that might cause an error
# except catches the error so your program doesn't crash

try:
    # This will cause an error because x is not defined
    print(x)
except:
    # If an error happens, run this code instead
    print("An exception occurred")

# Output:
# An exception occurred

# What happens without try-except
# Without error handling, the program crashes with an error message

# This would crash the program:
# print(x)  # NameError: name 'x' is not defined

# Handling different types of errors
# You can have different except blocks for different error types

try:
    # This causes a NameError (variable doesn't exist)
    print(x)
except NameError:
    # Specific message for NameError
    print("Variable x is not defined")
except:
    # Catch any other type of error
    print("Something else went wrong")

# Output:
# Variable x is not defined

# Using else with try-except
# else block runs if NO error occurred

try:
    # This works fine - no error
    print("Hello")
except:
    # This won't run because there's no error
    print("Something went wrong")
else:
    # This runs because try succeeded
    print("Nothing went wrong")

# Output:
# Hello
# Nothing went wrong

# Using finally
# finally block ALWAYS runs, whether there's an error or not
# Great for cleanup tasks like closing files

try:
    # This causes an error
    print(x)
except:
    # Handle the error
    print("Something went wrong")
finally:
    # This runs no matter what
    print("The 'try except' is finished")

# Output:
# Something went wrong
# The 'try except' is finished

# Try-except with file handling
# A practical example: safely working with files

try:
    # Try to open a file
    f = open("demofile.txt")
    try:
        # Try to write to it
        f.write("Lorum Ipsum")
    except:
        # Handle writing error
        print("Something went wrong when writing to the file")
    finally:
        # Always close the file, even if there was an error
        f.close()
except:
    # Handle file opening error
    print("Something went wrong when opening the file")

# Output:
# Something went wrong when writing to the file
# (if file is read-only or doesn't exist)

# Raising your own exceptions
# You can intentionally cause an error using 'raise'
# This is useful for validating data

x = -1

# Check if x is negative
if x < 0:
    # Raise an exception with a custom message
    raise Exception("Sorry, no numbers below zero")

# Output:
# Exception: Sorry, no numbers below zero
# (Program stops here)

# Raising specific error types
# You can raise specific types of errors with custom messages

x = "hello"

# Check if x is an integer
if not type(x) is int:
    # Raise a TypeError with explanation
    raise TypeError("Only integers are allowed")

# Output:
# TypeError: Only integers are allowed

# Try-except with division
# A common use case: handling division by zero

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide numbers only!")

# Test different scenarios
divide_numbers(10, 2)     # Works fine
divide_numbers(10, 0)     # Division by zero
divide_numbers(10, "2")   # Wrong type

# Output:
# Result: 5.0
# Error: Cannot divide by zero!
# Error: Please provide numbers only!

# Multiple error handling with details
# You can access error details using 'as'

try:
    # Try to convert string to integer
    number = int("abc")
except ValueError as e:
    # 'e' contains details about the error
    print(f"Conversion error: {e}")

# Output:
# Conversion error: invalid literal for int() with base 10: 'abc'

