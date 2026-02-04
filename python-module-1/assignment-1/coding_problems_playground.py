'''
Idea behind this python file is to demonstrate whatever has been learnt in the first class is reflected in solving near real world problems.

This is much more fun learning experience hence I have compiled this list of mini-programs.

Some concepts can overlap to session 2 as well, which I have already gone through quickly in the last days.
'''

# =====================================================================================
'''
1. Collect marks for 3 students, calculate average, and assign a letter grade (A/B/C/D/F).
'''

# Input marks
marks = []
for i in range(3):
    score = int(input(f"Enter marks of student {i+1}: "))
    marks.append(score)

# Calculate average
average = sum(marks) / len(marks)
print("Average marks:", average)

# Assign grades
for idx, mark in enumerate(marks):
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Student {idx+1}: Marks={mark}, Grade={grade}")

# =====================================================================================

# =====================================================================================
'''
2. Take two numbers and an operator (+, -, *, /) from the user and print the result.
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator")

# =====================================================================================

# =====================================================================================
'''
3. Let the user guess a number between 1 and 10 until they get it right.
'''

import random
number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

# =====================================================================================

# =====================================================================================
'''
4. Ask the user to enter 5 numbers, store them in a list, and calculate sum and average.
'''

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)

# =====================================================================================

# =====================================================================================
'''
5. Ask the user for 5 numbers and print the largest and smallest number.
'''

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# =====================================================================================

# =====================================================================================
'''
6. Take a number from the user and print its multiplication table up to 10.
'''

num = int(input("Enter a number for its multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# =====================================================================================

# =====================================================================================
'''
7. Convert a temperature in Celsius to Fahrenheit.
'''

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# =====================================================================================

# =====================================================================================
'''
8. Ask the user for a number and check if it’s prime.
'''

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# =====================================================================================

# =====================================================================================
'''
9. Ask the user for 5 items, store them in a list, and print the list in reverse order.
'''

items = []
for i in range(5):
    item = input(f"Enter item {i+1}: ")
    items.append(item)

print("Original list:", items)
print("Reversed list:", items[::-1])

# =====================================================================================

# =====================================================================================
'''
10. Average marks with Pass/Fail Status

 -> Accept any number of students

 -> Print average, highest, lowest

 -> Print pass/fail for each
'''

num_students = int(input("Enter number of students: "))
marks = []

for i in range(num_students):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print(f"Average marks: {average}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")

for idx, mark in enumerate(marks):
    status = "Passed" if mark >= 50 else "Failed"
    print(f"Student {idx+1}: Marks={mark}, Status={status}")

# =====================================================================================

# =====================================================================================
'''
11. Print an equilateral triangle with 5 rows

    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''

rows = 5  # Number of rows in the triangle

for i in range(1, rows + 1):
    print(" " * (rows - i), end="") # using end here since we want to have the stars printed in the same line.
    print("* " * i) # this actually prints the star.

# =====================================================================================

# =====================================================================================
'''
12. Print an equilateral triangle with n rows (depends on user input)

    * 
   * * 
  * * * 
 * * * * 
.......... so on...

'''

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# =====================================================================================
