# =========================================================
# Basic Code Snippet Examples for If/Elif/Else Statements
# =========================================================

# Simple if-statement
a = 33
b = 200
if b > a: # b in this case is greater than a hence the subsequent indented block will execute
    print("b is greater than a")

# Checking if a number is positive
number = 15
if number > 0: # Since 15 is greater than 0, the indented block will execute
    print("The number is positive")

# Improper indentation (for demonstration)
a = 33
b = 200
# if b > a:
# print("b is greater than a")  # error because the print is not indented properly.

# Multiple statements in an if block
age = 20
if age >= 18: # 20 is greater than 18, so the block will execute, since all subsequent lines are indented all will run
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

# Using a boolean variable in a condition
# Directly uses a boolean variable (no comparison operator) in the if statement.
is_logged_in = True
if is_logged_in:
    print("Welcome back!")

# else keyword example
# If the first condition fails, goes into the elif or else as appropriate.
a = 200
b = 33
if b > a: # first condition checked
    print("b is greater than a")
elif a == b: # elif checks another condition if the first if fails
    print("a and b are equal")
else: # else is the fallback if all prior conditions fail
    print("a is greater than b")

# else without elif
# Simple two-way choice: if/else only. Either first or second block runs.
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Elif keyword — multiple elif example
# Checks score and prints grade based on value.
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# Nested if statements
# Inner if only executes if outer condition is true.
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Nested if + else example
# Age & license check using nested conditions.
age = 25
has_license = True
if age >= 18:
    # this if-else is nested inside the first if. It follows the same indentation level.
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
# outer else for age check. Indentation level matches the first if.
else:
    print("You are too young to drive")

# More levels of nesting
# Rule of thumb: avoid deep nesting for readability. If you find code with nested levels >2, consider refactoring.
score = 85
attendance = 90
submitted = True
if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    # this else follows the attendance check indentation level        
    else:
        print("Pass but low attendance")
# outer else for score check
else:
    print("Fail")

# One-line if statement (shorthand)
# When there’s only one statement to execute in the if.
a = 5
b = 2
if a > b: print("a is greater than b")

# One-line if/else (ternary sequece style with prints)
a = 2
b = 330
print("A") if a > b else print("B") # Output: B

# Ternary assignment (if/else used to choose value)
a = 10
b = 20
bigger = a if a > b else b 
print("Bigger is", bigger) 

# One-line if/else chain with 3 outcomes
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# ===========================================
# Basic code snippets for match statements
# ===========================================

# Basic match on a weekday number
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
# Output: Thursday

# default case using underscore (_)
day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")
# If none of the earlier cases match, the `case _:` acts like a default.
# Output: Looking forward to the Weekend

# combining values (OR) with the pipe (|) operator
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5: # matches any of 1, 2, 3, 4, or 5
        print("Today is a weekday")
    case 6 | 7: # matches either 6 or 7
        print("I love weekends!")
# The first case matches any of 1–5, the second 6 or 7.
# Output: Today is a weekday

# using guards (if-conditions) in case patterns
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
# Here each pattern has an additional `if` guard: only if month matches.
# Since month == 5 and day is 4 (so day is in 1–5), the second case executes.
# Output: A weekday in May

# ============================================
# Advanced match statements examples.
# ============================================

# Matching on tuple structure
point = (2, 3)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point is at ({x}, {y})")
# matches a 2-tuple and binds variables x and y.
# Output: Point is at (2, 3)


# Matching on lists with variable-length unpacking
numbers = [1, 2, 3, 4, 5]

match numbers:
    case [1, 2, *rest]:
        print(f"Starts with 1, 2; the rest is {rest}")
    case [1, 2]:
        print("List is exactly [1, 2]")
# `*rest` captures the remaining elements.
# Output: Starts with 1, 2; the rest is [3, 4, 5]


# Matching dictionaries
person = {"name": "Alice", "age": 30}

match person:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")
    case {"name": name}:
        print(f"Person named {name}")
    case _:
        print("Unknown structure")
# Output: Alice is 30 years old

person = {"name": "Alice"}

match person:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")
    case {"name": name}:
        print(f"Person named {name}")
    case _:
        print("Unknown structure")
# Output: Person named Alice

# Using guards (if conditions) in match cases
value = 50

match value:
    case x if x < 0: # guard to check for negative
        print("Negative number")
    case x if 0 <= x <= 10: # guard for small range
        print("Small number")
    case x if 10 < x <= 100: # guard for medium range
        print("Medium number")
    case _: # default case
        print("Large number")
# Output: Medium number

# Nested pattern matching
shapes = [
    {"type": "circle", "radius": 10},
    {"type": "rectangle", "width": 5, "height": 8},
]

for shape in shapes:
    match shape:
        case {"type": "circle", "radius": r}:
            print(f"Circle with radius {r}")
        case {"type": "rectangle", "width": w, "height": h}:
            print(f"Rectangle of {w}x{h}")
        case _:
            print("Unknown shape")
# Output:
# Circle with radius 10
# Rectangle of 5x8


# Binding variables with wildcard and ignoring values
data = ("User", "John", 42, "Admin")

match data:
    case ("User", name, *_):
        print(f"Found user: {name}")
# `*_` ignores remaining values, keeping only what we need.
# Output: Found user: John

# ============================================================
# WRONG / INVALID usage examples of match statements
# ============================================================

# `match` without `case` statements
# match 5:
#     print("This will cause a SyntaxError")

# Duplicate case labels
# INVALID (Python does not allow identical literal patterns)
# match 1:
#     case 1:
#         print("One")
#     case 1:
#         print("Also one")  # Unreachable, but not an error; just useless.

# Using expressions in patterns (not allowed)
# INVALID: Cannot use computed expressions directly in case patterns
# value = 10
# match value:
#     case 5 + 5:  # You cannot use arithmetic in the pattern
#         print("Ten")
# This will cause SyntaxError: expressions are not allowed in patterns.

# Incorrect unpacking structure
# INVALID: mismatch between tuple structure and data
# point = (1, 2, 3)
# match point:
#     case (x, y):
#         print("Will not match because tuple has 3 elements")
# Expected output:
# (no output, since pattern doesn't match)

# Guard variable not defined
# match 5:
#     case x if y > 0:  # 'y' is not defined
#         print("Error")
# Raises NameError: name 'y' is not defined

# =========================================================
# Basic code snippets for While loops
# =========================================================

# Print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1
# We start with i=1, and as long as i<6 the loop runs, printing i each time then incrementing.
# Output:
# 1
# 2
# 3
# 4
# 5

# Using break to exit the loop early when i == 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# Loop as long as i<6, but if i becomes 3 we break out immediately.
# Output:
# 1
# 2
# 3

# Using continue to skip printing when i == 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# i runs from 1 up to 6; when i becomes 3 we ‘continue’ which skips the print for that iteration.
# Output:
# 1
# 2
# 4
# 5
# 6

# Using else with a while loop — else triggers when loop condition becomes false (and no break)
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# The loop goes while i<6; once that becomes false, the else-block executes.
# Output:
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6

# -*- coding: utf-8 -*-
"""
Advanced and incorrect examples of Python while loops
"""

# Countdown using while loop
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
# Simple countdown loop; decrements until count == 0.
# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


# While loop with else block
n = 1
while n <= 3:
    print("Processing", n)
    n += 1
else:
    print("All items processed.")
# The `else` runs when the while loop exits normally (not via break).
# Output:
# Processing 1
# Processing 2
# Processing 3
# All items processed.


# Using break to stop early (so else won't run)
n = 1
while n <= 5:
    print("n =", n)
    if n == 3:
        print("Breaking early")
        break
    n += 1
else:
    print("Loop completed without break")
# When break is hit, the else part is skipped.
# Output:
# n = 1
# n = 2
# n = 3
# Breaking early


# Nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# Outer loop runs 3 times; inner loop runs 2 times each.
# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2


# Infinite loop with break
x = 0
while True:
    x += 1
    print("Looping:", x)
    if x >= 3:
        break
print("Loop ended.")
# `while True` creates an infinite loop; `break` stops it.
# Output:
# Looping: 1
# Looping: 2
# Looping: 3
# Loop ended.


# Using while with a flag variable
flag = True
counter = 0
while flag:
    print("Running iteration", counter)
    counter += 1
    if counter >= 3:
        flag = False  # turn off loop
print("Loop ended after flag became False")
# Uses boolean flag to control loop.
# Output:
# Running iteration 0
# Running iteration 1
# Running iteration 2
# Loop ended after flag became False


# ============================================================
# INVALID / WRONG USAGE examples of While loops
# ============================================================

# Missing increment leads to infinite loop
# WARNING: This would run forever
# i = 0
# while i < 5:
#     print(i)
## i is never incremented; loop never stops.

# Syntax error – missing colon
# while True
#     print("Missing colon")
# # Raises SyntaxError

# Using a non-boolean condition (logical mistake)
# This is allowed syntactically, but logic may fail:
num = 5
while num:  # condition is truthy while num != 0
    print("num =", num)
    num -= 2
# Works but may confuse readers; explicit comparison (num > 0) is clearer.
# Output:
# num = 5
# num = 3
# num = 1


# Unreachable else due to break
count = 0
while count < 5:
    if count == 2:
        break
    count += 1
else:
    print("Will never print")  # unreachable
# The else never runs if a break is encountered.
# Output: (No output from else)


# TypeError in condition
# INVALID at runtime
# while "Hello":
#     print("Infinite loop!")  # non-empty string always truthy → infinite loop
# # Explanation: Legal but bad logic — runs forever.

# Modifying iterable while looping over it (logic error)
items = [1, 2, 3]
i = 0
while i < len(items):
    print(items[i])
    items.append(i)  # grows list during iteration, this is risky and can result in unexpected behaviour !
    if i > 5:
        break
    i += 1
# Explanation: Avoid changing list length while looping — can cause unintended behavior.
# Output (truncated safely):
# 1
# 2
# 3
# 0
# 1
# 2
# (and so on if not broken)

# =========================================================
# Basic code snippet using for loops
# =========================================================

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# Iterate over each element in the list and print it.
# Output:
# apple
# banana
# cherry

# Loop through a string
for char in "banana":
    print(char)
# Strings are iterable, so this prints each character.
# Output:
# b
# a
# n
# a
# n
# a

# Using break in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# Loop until the element equals "banana", then break.
# Output:
# apple
# banana

# Using continue in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# Skip printing "banana"; continue to next iteration.
# Output:
# apple
# cherry

# Using range() to loop a fixed number of times
for x in range(6):
    print(x)
# range(6) yields 0,1,2,3,4,5 and we print each.
# Output:
# 0
# 1
# 2
# 3
# 4
# 5

# Using start and step in range()
for x in range(2, 6):
    print(x)
# range(2,6) yields 2,3,4,5.
# Output:
# 2
# 3
# 4
# 5

for x in range(2, 30, 3):
    print(x, end=" ")
print()
# range(2,30,3) yields numbers starting at 2, step 3, up to but not including 30.
# Output (in one line):
# 2 5 8 11 14 17 20 23 26 29 

# For loop with else
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# The else block executes after the loop finishes normally (no break).
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
# Here we break at x==3, so the else block does NOT execute.
# Output:
# 0
# 1
# 2

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for a in adj:
    for f in fruits:
        print(a, f)
# For every adjective `a`, we iterate through every fruit `f` and print combination.
# Output:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

# Empty loop body using pass
for x in []:
    pass
# If a loop would be empty (here no iteration), using pass avoids an error. Practical when you intend to do nothing.
# Output: (nothing printed)

# ============================================================
# Advanced and incorrect examples of For loops
# ============================================================

# Looping with enumerate to get index + value
animals = ["cat", "dog", "rabbit"]
for idx, animal in enumerate(animals, start=1):
    print(f"{idx}: {animal}")
# enumerate provides index and element. start=1 so index begins at 1.
# Expected output:
# 1: cat
# 2: dog
# 3: rabbit

# Iterating through dictionary keys & values
person = {"name": "Alice", "age": 30, "city": "Shimla"}
for key, value in person.items():
    print(f"{key} -> {value}")
# items() returns key‐value pairs for looping.
# Output (order may vary because dicts are unordered in older Python):
# name -> Alice
# age -> 30
# city -> Shimla

# Using list comprehension inside a for loop (mixed style)
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n * n)
print("Squares:", squares)
# Instead of list comprehension, this uses a for loop to build a list.
# Output: Squares: [1, 4, 9, 16, 25]

# Looping with break and complex condition
for n in range(10):
    if n % 2 == 0 and n > 4:
        print("Even number > 4 found:", n)
        break
    print("Checking:", n)
else:
    print("No even number > 4 found")
# Loop from 0 to 9; print checks until we hit first even number >4 then break; else would run if no break.
# Output:
# Checking: 0
# Checking: 1
# Checking: 2
# Checking: 3
# Checking: 4
# Even number > 4 found: 6


# Wrong: Modifying list while iterating (can lead to weird/missed items)
items = [1, 2, 3, 4]
for i in items:
    print("Item:", i)
    if i == 2:
        items.remove(3)
# Removing elements from the list being iterated can cause skipped elements or unpredictable behavior.
# Output (one possible outcome, actual may vary):
# Item: 1
# Item: 2
# Item: 4
# (3 may be skipped)

# Wrong: Using range incorrectly (off-by-one)
for x in range(5):
    print(x)
# Someone expecting 0-5 inclusive might be surprised it goes 0-4. Should be range(6) for 0-5.
# Output:
# 0
# 1
# 2
# 3
# 4

# Wrong: Using loop variable outside scope (logical mistake)
for i in range(3):
    print(i)
print("After loop, i is:", i)
# While valid in Python (i remains last value), relying on it outside the loop may be poor style.
# Output:
# 0
# 1
# 2
# After loop, i is: 2
