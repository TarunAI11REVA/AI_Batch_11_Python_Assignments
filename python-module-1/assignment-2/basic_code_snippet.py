# =========================
# 1. Python Strings
# =========================

# Basic String Printing
print("Hello")                      # Output: Hello
print('Hello')                      # Output: Hello

print("It's alright")               # Output: It's alright
print("He is called 'Johnny'")      # Output: He is called 'Johnny'
print('He is called "Johnny"')      # Output: He is called "Johnny"

a = "Hello"
print(a)                            # Output: Hello

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Output:
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Output (same as above)

a = "Hello, World!"
print(a[1])                         # Output: e, since in python a string is considered just as 
# a collection of characters, with the first character starting at index 0.
 

for x in "banana":
    print(x)
# Output:
# b
# a
# n
# a
# n
# a

a = "Hello, World!"
print(len(a))                       # Output: 13

txt = "The best things in life are free!"
print("free" in txt)                # Output: True

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
# Output: Yes, 'free' is present.

txt = "The best things in life are free!"
print("expensive" not in txt)       # Output: True

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
# Output: No, 'expensive' is NOT present.

# Slicing Strings
b = "Hello, World!"
print(b[2:5])                       # Output: llo
print(b[:5])                        # Output: Hello
print(b[2:])                        # Output: llo, World!
print(b[-5:-2])                     # Output: orl

'''
Slicing string: the square bracket with a colon separating two optional numbers represents the starting index
of the slice on the left side of the colon and ending index(not included) on the right side.
Negative indexing starts from the end of the string and it starts with -1, -2 and so on...
i.e. 
For "Hello, World!" string the indices would look like this...
H -> 0, e -> 1, l -> 2, l -> 3, and so on... OR 
! -> -1, d -> -2, l -> -3, r -> -4 and so on...

'''

# Modify Strings
a = "Hello, World!"
print(a.upper())                    # Output: HELLO, WORLD! i.e. it converts all lowercase characters to upper
print(a.lower())                    # Output: hello, world! i.e. it converts all uppercase characters to lower

a = " Hello, World! "
print(a.strip())                    # Output: Hello, World! i.e. it removes extra spaces from the front and end of the string.

a = "Hello, World!"
print(a.replace("H", "J"))          # Output: Jello, World! i.e. it replaces a character present in the string by another one.

a = "Hello, World!"
print(a.split(","))                 # Output: ['Hello', ' World!'] i.e. it splits by the specified character if it exists.

# String Formatting
txt = f"The price is 49 dollars"
print(txt)                          # Output: The price is 49 dollars

price = 59
txt = f"The price is {price} dollars"
print(txt)                          # Output: The price is 59 dollars

'''
If this statement above is printed without specifying that its a "f" string, then the python interpretor would return an error,
since price is integer and txt is string. The other way to fix it could be by casting integer to string and then using it inside 
the string 'txt' 
'''

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)                          # Output: The price is 59.00 dollars
'''
.2f specifies that the price should be exactly upto two decimal places.
'''

txt = f"The price is {95:.2f} dollars"
print(txt)                          # Output: The price is 95.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt)                          # Output: The price is 1180 dollars

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)                          # Output: The price is 73.75 dollars

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)                          # Output: It is very Cheap

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)                          # Output: I LOVE APPLES

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)                          # Output: The plane is flying at a 9144.0 meter altitude

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)                          # Output: The price is 59,000 dollars

price = 49
txt = "The price is {} dollars"
print(txt.format(price))            # Output: The price is 49 dollars

txt = "The price is {:.2f} dollars" # (no print, just format string definition)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item number 567 for 49.00 dollars.
'''
format() function can be used to populate the placeholders in a given string on the fly or at runtime.
'''

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item number 567 for 49.00 dollars.

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# Output: His name is John. John is 36 years old.

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
# Output: I have a Ford, it is a Mustang.

# ===========================
# 2. Python Booleans
# ===========================

# Boolean Values – comparing numbers
print(10 > 9)    # True            # Checks if 10 is greater than 9
print(10 == 9)   # False           # Checks if 10 is equal to 9
print(10 < 9)    # False           # Checks if 10 is less than 9

# Using if/else with Boolean expression
a = 200
b = 33
if b > a:
    print("b is greater than a")   # This will not print in this case
else:
    print("b is not greater than a")   # Output: b is not greater than a
# Checks the condition b > a, then chooses if-else block accordingly.

# Evaluate Values and Variables with bool()
print(bool("Hello"))   # True            # Non-empty string is evaluated as True
print(bool(15))        # True            # Non-zero number is evaluated as True

x = "Hello"
y = 15
print(bool(x))         # True            # Variable x holds non-empty string i.e. True
print(bool(y))         # True            # Variable y holds non-zero number i.e. True

print(bool("abc"))                # True            # Non-empty string
print(bool(123))                  # True            # Non-zero integer
print(bool(["apple", "cherry", "banana"]))   # True   # Non-empty list

# Some values are False
print(bool(False))    # False   # Literal False
print(bool(None))     # False   # None is evaluated as False
print(bool(0))        # False   # Zero is evaluated as False
print(bool(""))       # False   # Empty string is evaluated as False
print(bool(()))       # False   # Empty tuple is False
print(bool([]))       # False   # Empty list is False
print(bool({}))       # False   # Empty dictionary is False

# Custom object __len__ returning zero => evaluates to False
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))    # False   # myobj has __len__ = 0, so bool(myobj) is False

# Functions can return a Boolean
def myFunction():
    return True

print(myFunction())   # True    # Calls function myFunction() that returns True

if myFunction():
    print("YES!")     # YES!    # Because myFunction() returned True
else:
    print("NO!")

# Built-in function returning Boolean: isinstance()
x = 200
print(isinstance(x, int))    # True    # Checks if x is instance of int

# =============================================================
# Python boolean learnings: edge cases and invalid use cases.
# =============================================================

# 1. Boolean with special numeric values

print(bool(0))           # False,  zero is always False
print(bool(-0))          # False,  -0 is the same as 0 in Python
print(bool(0.0))         # False,  zero float is also False
print(bool(float('inf')))  # True,  infinity counts as True
print(bool(float('-inf'))) # True,  negative infinity counts as True
print(bool(float('nan')))  # True,  NaN (not a number) is still True in bool context


# 2. Boolean with containers (lists, tuples, dicts, sets)

print(bool([]))           # False, empty list is False
print(bool([0]))          # True, non-empty list is True, even if it contains 0
print(bool({}))           # False, empty dict is False
print(bool({'a': None}))  # True, non-empty dict is True
print(bool(set()))        # False, empty set is False
print(bool({0}))          # True, non-empty set is True


# 3. Boolean with custom objects

class AlwaysFalse:
    def __bool__(self):
        return False

class AlwaysTrue:
    def __bool__(self):
        return True

print(bool(AlwaysFalse()))  # False, __bool__() explicitly returns False
print(bool(AlwaysTrue()))   # True, __bool__() explicitly returns True


# 4. Boolean with __len__ returning 0 or >0

class MyContainer:
    def __len__(self):
        return 0  # treated as False when length == 0

c = MyContainer()
print(bool(c))              # False, because len() == 0

class MyNonEmpty:
    def __len__(self):
        return 5

print(bool(MyNonEmpty()))   # True, len() > 0, True


# 5. Mixing Boolean and Arithmetic operations

print(True + True)          # 2, because True == 1 in arithmetic context
print(False + 5)            # 5, because False == 0
print(True * 10)            # 10, same reason
print(False * 100)          # 0, False acts like zero

# Logical expressions returning Boolean results
print(True and False)       # False
print(True or False)        # True
print(not 0)                # True, not converts Falsey to True


# 6. Edge cases with custom __bool__ returning non-bool values

class WeirdBool:
    def __bool__(self):
        return "not a bool"   # Invalid return type

# print(bool(WeirdBool()))
# INVALID: TypeError: __bool__ should return bool, not str


# 7. Edge case with __len__ returning invalid types

class InvalidLen:
    def __len__(self):
        return None   # must be an int >= 0

# print(bool(InvalidLen()))
# INVALID: TypeError: __len__() should return >= 0 integer


# 8. Boolean operations on non-comparable types

# print(10 < "5")
# INVALID: TypeError: '<' not supported between instances of 'int' and 'str'
# Python does not allow ordering comparisons between different types

# print(True > "False")
# INVALID: TypeError: '>' not supported between instances of 'bool' and 'str'
# You cannot directly compare bool and str


# 9. Boolean on deleted or undefined variables

# print(bool(undefined_var))
# INVALID: NameError: name 'undefined_var' is not defined
# Variable must be defined before using

# 10. Double negatives and nested booleans

print(not not True)          # True, double negation cancels out
print(not not [])            # False, [] is Falsey, so not not [] = False
print(not not "Hi")          # True, non-empty string hence True

# Boolean of Boolean
print(bool(True))            # True
print(bool(False))           # False


# 11. Boolean comparison quirks

print(True == 1)             # True, because bool is subclass of int
print(False == 0)            # True

# ==============================
# 3. Python operators
# ==============================

# Arithmetic Operators
# These operators perform mathematical operations between numeric values.
print(10 + 5)                # 15     # addition: adds 10 and 5
print(10 - 5)                # 5      # subtraction: subtracts 5 from 10
print(10 * 5)                # 50     # multiplication: multiplies 10 by 5
print(10 / 4)                # 2.5    # division: divides 10 by 4 (produces float)
print(10 % 3)                # 1      # modulus: remainder of dividing 10 by 3
print(2 ** 3)                # 8      # exponentiation: 2 raised to the power of 3
print(15 // 4)               # 3      # floor division: quotient of 15/4 disregarding remainder

# Assignment Operators
# These shorthand operators perform an operation and assign the result to a variable.
x = 5                        # assign 5 to x
x += 3                      # equivalent to x = x + 3
print(x)                     # 8      # x becomes 8
x *= 2                      # equivalent to x = x * 2
print(x)                     # 16     # x becomes 16

# Comparison Operators
# These operators compare two values and return a Boolean result.
print(5 == 5)               # True   # equality: checks if 5 equals 5
print(5 != 4)               # True   # not equal: checks if 5 is not equal to 4
print(5 > 4)                # True   # greater than: checks if 5 is greater than 4
print(5 < 4)                # False  # less than: checks if 5 is less than 4
print(5 >= 5)               # True   # greater than or equal: checks if 5 is at least 5
print(4 <= 3)               # False  # less than or equal: checks if 4 is at most 3

# Logical Operators
# These operators combine Boolean expressions or values.
a = True
b = False
print(a and b)              # False  # logical AND: True only if both operands are True
print(a or b)               # True   # logical OR: True if at least one operand is True
print(not a)                # False  # logical NOT: inverts the Boolean value of a

# Identity Operators
# These check whether two variables refer to the **same object**, not just equal value.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 is list3)       # True   # is: checks if both refer to same object.
print(list1 is list2)       # False  # although the lists are equal in content, they are distinct objects
print(list1 is not list2)   # True   # is not: checks if they are not the same object

# Membership Operators
# These test whether a value is present (or not) in a sequence (list, string, etc).
txt = "hello world"
print("world" in txt)       # True   # in: checks if substring "world" is present in txt
print("mars" not in txt)    # True   # not in: checks if substring "mars" is **not** present in txt

# --- Operator Precedence Example ---
# Demonstrates how parentheses and operator precedence affect evaluation order.
print((6 + 3) - (6 + 3))     # 0      # parentheses override default precedence
print(100 + 5 * 3)           # 115    # multiplication has higher precedence than addition (5 * 3 =15, then +100 =115)

'''
Golden rule here is to always use common brackets whereever possible - it keeps code more readable and comprehensible since 
operator precedence logic could get complex very easily.
'''

# =========================
# 4. Python lists.
# =========================

# Initialize a list
mylist = ["apple", "banana", "cherry"]

# 1. CREATE A LIST - Lists store multiple items in a single variable
mylist = ["apple", "banana", "cherry"]
print(mylist)
# Output: ['apple', 'banana', 'cherry']

# 2. ALLOW DUPLICATES - Lists can have items with the same value
mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)
# Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# 3. LIST LENGTH - Use len() to get number of items
print("\n3. Length of list:")
print(len(mylist))
# Output: 5

# 4. DATA TYPES - Lists can contain any data type
mylist = ["abc", 34, True, 40, "male"]
print(mylist)
# Output: ['abc', 34, True, 40, 'male']

# 5. TYPE CHECKING - Lists are objects with type 'list'
print("\n5. Type of list:")
print(type(mylist))
# Output: <class 'list'>

# 6. LIST CONSTRUCTOR - Create list using list() constructor
mylist = list(("apple", "banana", "cherry"))
print(mylist)
# Output: ['apple', 'banana', 'cherry']

# 7. ACCESS BY INDEX - Access items using index (0-based)
print(mylist[1])
# Output: banana, index 1 - so the second item in the list will be printed.

# 8. NEGATIVE INDEXING - Access from end using negative index
print(mylist[-1])
# Output: cherry

# 9. RANGE SLICING - Get subset using [start:end]
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])
# Output: ['cherry', 'orange', 'kiwi']

# 10. SLICE FROM START - Omit start index to begin from start
print(mylist[:4])
# Output: ['apple', 'banana', 'cherry', 'orange']

# 11. SLICE TO END - Omit end index to go to end
print(mylist[2:])
# Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# 12. NEGATIVE RANGE - Use negative indexes in slicing
print(mylist[-4:-1])
# Output: ['orange', 'kiwi', 'melon']

# 13. CHECK EXISTENCE - Use 'in' keyword to check if item exists
if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")
# Output: Yes, 'apple' is in the fruits list

# 14. CHANGE ITEM - Modify item by referring to index
mylist[1] = "blackcurrant"
print(mylist)
# Output: ['apple', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# 15. CHANGE RANGE - Replace multiple items at once
mylist[1:3] = ["banana", "watermelon"]
print(mylist)
# Output: ['apple', 'banana', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']

# 16. INSERT - Add item at specific position without replacing
mylist.insert(2, "cherry")
print(mylist)
# Output: ['apple', 'banana', 'cherry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']

# 17. APPEND - Add item to end of list
mylist.append("grape")
print(mylist)
# Output: ['apple', 'banana', 'cherry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'grape']

# 18. EXTEND - Add all items from another list
tropical = ["pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)
# Output: ['apple', 'banana', 'cherry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya']

# 19. EXTEND WITH TUPLE - Can extend with any iterable
mytuple = ("lemon", "lime")
mylist.extend(mytuple)
print(mylist)
# Output: ['apple', 'banana', 'cherry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon', 'lime']

# 20. REMOVE - Remove first occurrence of specified value
mylist.remove("watermelon")
print(mylist)
# Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon', 'lime']

# 21. POP INDEX - Remove item at specified index
mylist.pop(1)
print(mylist)
# Output: ['apple', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon', 'lime']

# 22. POP LAST - Remove last item (no index specified)
mylist.pop()
print(mylist)
# Output: ['apple', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon']

# 23. DEL INDEX - Delete item using del keyword
del mylist[0]
print(mylist)
# Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon']

# 24. FOR LOOP - Iterate through list items
for x in mylist[:3]:
    print(x)
# Output:
# cherry
# orange
# kiwi

# 25. LOOP WITH INDEX - Use range and len to loop by index
for i in range(3):
    print(mylist[i])
# Output:
# cherry
# orange
# kiwi

# 26. WHILE LOOP - Loop using while with counter
i = 0
while i < 3:  # Only first 3 for brevity
    print(mylist[i])
    i = i + 1
# Output:
# cherry
# orange
# kiwi

# 27. LIST COMPREHENSION LOOP - Shortest syntax for looping
[print(x) for x in mylist[:3]]
# Output:
# cherry
# orange
# kiwi

# 28. LIST COMPREHENSION WITH CONDITION - Filter items while creating new list
newlist = [x for x in mylist if "a" in x]
print(newlist)
# Output: ['orange', 'mango', 'grape', 'papaya']

# 29. LIST COMPREHENSION EXCLUDE - Filter out specific items
newlist = [x for x in mylist if x != "cherry"]
print(newlist)
# Output: ['orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon']

# 30. LIST COMPREHENSION NO CONDITION - Copy all items
newlist = [x for x in mylist]
print(newlist)
# Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon']

# 31. LIST COMPREHENSION WITH RANGE - Create list from range
newlist = [x for x in range(10)]
print(newlist)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 32. RANGE WITH CONDITION - Filter range values
newlist = [x for x in range(10) if x < 5]
print(newlist)
# Output: [0, 1, 2, 3, 4]

# 33. TRANSFORM WITH COMPREHENSION - Apply function to each item
newlist = [x.upper() for x in mylist]
print(newlist)
# Output: ['CHERRY', 'ORANGE', 'KIWI', 'MELON', 'MANGO', 'GRAPE', 'PINEAPPLE', 'PAPAYA', 'LEMON']

# 34. SET ALL VALUES - Create list with same value repeated
newlist = ['hello' for x in mylist]
print(newlist[:3])  # Show only first 3
# Output: ['hello', 'hello', 'hello']

# 35. CONDITIONAL EXPRESSION - Use if-else in comprehension
newlist = [x if x != "cherry" else "strawberry" for x in mylist]
print(newlist)
# Output: ['strawberry', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'pineapple', 'papaya', 'lemon']

# 36. SORT ALPHABETICALLY - Sort list in ascending order
mylist.sort()
print(mylist)
# Output: ['cherry', 'grape', 'kiwi', 'lemon', 'mango', 'melon', 'orange', 'papaya', 'pineapple']

# 37. SORT DESCENDING - Sort in reverse order
mylist.sort(reverse=True)
print(mylist)
# Output: ['pineapple', 'papaya', 'orange', 'melon', 'mango', 'lemon', 'kiwi', 'grape', 'cherry']

# 38. SORT NUMERICALLY - Works with numbers
numlist = [100, 50, 65, 82, 23]
numlist.sort()
print(numlist)
# Output: [23, 50, 65, 82, 100]

# 39. CUSTOM SORT FUNCTION - Sort by custom criteria
def myfunc(n):
    return abs(n - 50)  # Sort by proximity to 50
numlist.sort(key=myfunc)
print(numlist)
# Output: [50, 65, 23, 82, 100]

# 40. CASE INSENSITIVE SORT - Sort ignoring case
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort(key=str.lower)
print(mylist)
# Output: ['banana', 'cherry', 'Kiwi', 'Orange']

# 41. REVERSE ORDER - Reverse current order (not sorting)
mylist.reverse()
print(mylist)
# Output: ['Orange', 'Kiwi', 'cherry', 'banana']

# 42. COPY WITH COPY() - Create independent copy
mylist = ["apple", "banana", "cherry"]
newlist = mylist.copy()
print(newlist)
# Output: ['apple', 'banana', 'cherry']

# 43. COPY WITH LIST() - Another way to copy
newlist = list(mylist)
print(newlist)
# Output: ['apple', 'banana', 'cherry']

# 44. COPY WITH SLICE - Copy using slice operator
newlist = mylist[:]
print(newlist)
# Output: ['apple', 'banana', 'cherry']

# 45. JOIN WITH + OPERATOR - Concatenate two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# Output: ['a', 'b', 'c', 1, 2, 3]

# 46. JOIN WITH LOOP - Append items one by one
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
# Output: ['a', 'b', 'c', 1, 2, 3]

# 47. JOIN WITH EXTEND - Add all items from another list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# Output: ['a', 'b', 'c', 1, 2, 3]

# 48. CLEAR LIST - Remove all items but keep list
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)
# Output: []

# ====================
# 5. Python tuples.
# ====================

# Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Output: ('apple', 'banana', 'cherry')
# Defines a tuple with three string items and prints it.

# Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')
# Shows that tuples can contain duplicate items (here “apple” and “cherry” appear twice).

# Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# Output: 3
# Uses the built-in len() function to get the length (number of items) of the tuple.

# One item tuple (remember the comma)
thistuple = ("apple",)
print(type(thistuple))
# Output: <class 'tuple'>
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# Output: <class 'str'>
# Illustrates how to create a tuple with a single item (requires trailing comma) and what happens without the comma.

# A tuple with strings, integers and boolean values
tuple1 = ("abc", 34, True, 40, "male")
# No print output
# Demonstrates that tuple items can be of different data types.

# Using the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
# Output: ('apple', 'banana', 'cherry')
# Uses the tuple() built-in constructor (with an iterable) to create a tuple.

# Access tuple item via positive index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# Output: banana
# Accesses the item at index 1 (second item) in the tuple.

# Access tuple item via negative index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
# Output: cherry
# Accesses the last item via negative indexing.

# Return a slice/range (third, fourth, fifth item)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Output: ('cherry', 'orange', 'kiwi')
# Demonstrates slicing: from index 2 inclusive up to index 5 exclusive.

# Slice from beginning up to index 4 (not included)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# Output: ('apple', 'banana', 'cherry', 'orange')
# Omitting the start index means start from the first item up to index 4 (exclusive).

# Slice from index 2 through end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')
# Omitting the end index means go from index 2 to the end of the tuple.

# Slice using negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
# Output: ('orange', 'kiwi', 'melon')
# Uses negative-index slicing: start at -4 inclusive, end at -1 exclusive (counts from end).

# Unpacking a tuple into variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Output:
# apple
# banana
# cherry
# Packs values into a tuple, then “unpacks” them into three separate variables.

# Unpacking with asterisk to collect the rest of values as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# Output:
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']
# Uses * syntax so that `red` gets the remaining values as a list.

# Another unpacking example: asterisk in the middle
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# Output:
# apple
# ['mango', 'papaya', 'pineapple']
# cherry
# The *tropic variable collects all middle elements, showing flexible unpacking.

# Loop through tuple items (for loop)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# Output:
# apple
# banana
# cherry
# Iterates over each item in the tuple using a for-loop.

# Loop through tuple items using index number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
# Output:
# apple
# banana
# cherry
# Uses range() + len() to iterate over indices and access tuple items.

# Loop through tuple items using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
# Output:
# apple
# banana
# cherry
# A while-loop alternative to iterate through tuple items by index.

# Join two tuples via + operator
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# Output: ('a', 'b', 'c', 1, 2, 3)
# Demonstrates concatenation of two tuples with +, producing a new tuple.

# Multiply a tuple content by integer
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
# Shows repetition of tuple elements: the fruits tuple repeated twice.

# Change tuple values by converting to list, modifying list, and converting back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# Output: ('apple', 'kiwi', 'cherry')
# Since tuples are immutable, this workaround converts to list to modify and back.

# Add an item by converting to list and back
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'orange')
# Adds “orange” by converting tuple to list, appending, then back to tuple.

# Add a tuple to a tuple (single-item tuple must end with comma)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'orange')
# Because tuples are immutable, you can add by concatenation; note single-item tuple uses comma.

# Delete a tuple completely using del
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # this will raise an error because the tuple no longer exists
# Output: NameError: name 'thistuple' is not defined
# Demonstrates that while individual items can't be removed, you can delete the entire tuple.

# Using tuple.index() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
# Output: 3
# Finds the first index of value 8 in the tuple using the index() method.

# Using tuple.count() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(8)
print(x)
# Output: 2
# Counts how many times value 8 appears in the tuple using count().

# =========================
# 6. Python Sets.
# =========================

# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Output: {'apple', 'banana', 'cherry'}
# Defines a set with three items and prints it. (sets are unordered)

# Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# Output: {'apple', 'banana', 'cherry'}
# Demonstrates that duplicates in a set are ignored.

# True and 1 are considered the same value in sets
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# Output: {True, 1, 2, 'apple', 'banana', 'cherry'}  
# (Learning: On many runs, True and 1 collapse to one value so you may see something like {1,2,'apple','banana','cherry'})
# Shows how Boolean and integer duplicates behave in a set.

# False and 0 are considered the same value in sets
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
# Output: {0, True, 'apple', 'banana', 'cherry'}
# Demonstrates that False and 0 are treated as duplicates in a set.

# Get the number of items in a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Output: 3
# Uses len() to determine how many items are in the set.

# Sets can contain different data types
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# Output: {True, 34, 40, 'male', 'abc'}  (order may vary)
# Shows that a set can include strings, integers, booleans in the same set.

# Using the set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Output: {'apple', 'banana', 'cherry'}
# Demonstrates using the set() constructor with an iterable to create a set.

# Loop through set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# Output:
# apple
# banana
# cherry
# (Order is not guaranteed; it may differ.)
# Shows how to iterate through each item in the set.

# Check if an item exists in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# Output: True
# Checks membership using 'in'.

# Check if an item does NOT exist in the set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
# Output: False
# Checks non-membership using 'not in'.

# Add an item to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Output: {'apple', 'banana', 'cherry', 'orange'}
# Demonstrates adding a single item to a set using add().

# Add items from another set (update)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Output: {'apple', 'banana', 'cherry', 'pineapple', 'mango', 'papaya'}
# Shows update() to add multiple items from another set.

# Add items from an iterable (list)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# Output: {'apple', 'banana', 'cherry', 'kiwi', 'orange'}
# update() accepts other iterable types, like lists.

# Remove an item using remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Output: {'apple', 'cherry'}
# remove() deletes the specified item; raises error if item not present.

# Remove an item using discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Output: {'apple', 'cherry'}
# discard() deletes the specified item; does not raise error if item not present.

# Remove a random item using pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Output: apple ( for example, may not always be this, since its a set and pop can remove any random value )
#         {'banana', 'cherry'}
# pop() removes and returns a random item from the set (since sets are unordered).

# Clear all items from the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# Output: set()
# clear() removes all items, leaving an empty set.

# Delete the entire set using del
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)  # would raise NameError because thisset no longer exists
# del keyword deletes the set variable entirely.

# Union of two sets (returns new set)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Output: {1, 2, 3, 'a', 'b', 'c'}
# union() returns a new set containing items from both sets (duplicates removed).

# Union using | operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
# Output: {1, 2, 3, 'a', 'b', 'c'}
# Alternative using | operator for union.

# Union of multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
# Output: {'Elena', 1, 2, 3, 'John', 'b', 'c', 'a', 'apple', 'bananas', 'cherry'}
# union() with more than two sets. Order is arbitrary.

# Join set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
# Output: {1, 2, 3, 'a', 'b', 'c'}
# union() can join a set with other iterable types (tuple here).

# Update (join in place)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Output: {1, 2, 3, 'a', 'b', 'c'}
# update() adds items from set2 into set1, modifying set1.

# Intersection of two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
# Output: {'apple'}
# intersection() returns common items between sets.

# Intersection using & operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
# Output: {'apple'}
# & operator is alternative for intersection().

# Difference of sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
# Output: {'banana', 'cherry'}
# difference() returns items in set1 not in set2.

# Difference using - operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
# Output: {'banana', 'cherry'}
# - operator is alternative for difference().

# Symmetric difference (items not in both)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# Output: {'banana', 'cherry', 'google', 'microsoft'}
# symmetric_difference() returns elements not common to both sets.

# Symmetric difference using ^ operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
# Output: {'banana', 'cherry', 'google', 'microsoft'}
# ^ operator is alternate for symmetric_difference().

# =========================
# 7. Python Dictionaries
# =========================

# Create and print a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Defines a dictionary with keys “brand”, “model”, “year” and prints it.

# Print a value by key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
# Output: Ford
# Accesses and prints the value associated with key “brand”.

# Duplicate keys will overwrite existing values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
# Demonstrates that if a dictionary has two entries with the same key, the last one overwrites the previous.

# Print dictionary length
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))
# Output: 3
# Uses len() to find how many key-value pairs are in the dictionary.

# Dictionary with different data types as values
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
# Output: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}
# Shows that values can be of any data type: string, boolean, integer, list.

# Print the data type of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))
# Output: <class 'dict'>
# Uses type() to show that the object is of type dict.

# Creating a dictionary using the dict() constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# Output: {'name': 'John', 'age': 36, 'country': 'Norway'}
# Uses the dict() built-in constructor with keyword arguments to create a dictionary.

# Accessing items: get value using key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)
# Output: Mustang
# Uses get() method to access the value for key “model”.

# Accessing items: keys(), values(), items()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before change
car["color"] = "white"
print(x)  # after change
# Output: dict_keys(['brand', 'model', 'year'])
#         dict_keys(['brand', 'model', 'year', 'color'])
# keys() returns a view object reflecting dictionary’s keys; when dictionary is changed, view updates.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)  # before change
car["year"] = 2020
print(x)  # after change
# Output: dict_values(['Ford', 'Mustang', 1964])
#         dict_values(['Ford', 'Mustang', 2020])
# values() returns view of dictionary values; changing the dictionary updates the view.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before change
car["year"] = 2022
print(x)  # after change
# Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#         dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2022)])
# items() returns view of key:value pairs; view reflects changes.

# Check if a key exists using 'in'
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Output: Yes, 'model' is one of the keys in the thisdict dictionary
# Uses membership test to check whether a key is present in the dictionary.

# Change dictionary item value via assignment
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
# Demonstrates modifying an existing value by key assignment.

# Update dictionary using update()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
# Uses update() to modify or add key:value pairs in one go.

# Adding an item by key assignment
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
# Adds a new key “color” with value “red”.

# Loop through dictionary keys
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)
# Output:
# brand
# model
# year
# Iterates over the keys in the dictionary.

# Loop through dictionary values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.values():
    print(x)
# Output:
# Ford
# Mustang
# 1964
# Uses values() method and iterates over dictionary values.

# Loop through dictionary keys and values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():
    print(x, y)
# Output:
# brand Ford
# model Mustang
# year 1964
# items() returns pairs; the loop unpacks key and value.

# Nested dictionary example
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily["child2"]["name"])
# Output: Tobias
# A dictionary inside a dictionary (nested); accessing nested items by chained keys.


