# 02_variables.py
# Understanding Variables in Python

# A variable is like a labeled box that stores data in memory.
# You can assign values to variables using '='.

# Example 1: Assigning values
name = "Vijay"
age = 30
height = 5.9
is_student = True

# Example 2: Printing variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Example 3: Dynamic Typing
# In Python, you can reassign a variable to a different type
age = "Thirty"
print("Age (after reassignment):", age)

# Example 4: Multiple Assignments
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Example 5: Constants (by convention, written in uppercase)
PI = 3.14159
print("PI:", PI)

# Example 6: Type Checking
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
