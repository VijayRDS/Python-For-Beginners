# 03_data_types.py
# Understanding Python Data Types with Examples and Use Cases

"""
Python is dynamically typed — that means you don’t need to declare
a variable’s data type. Python figures it out at runtime.

Major Built-in Data Types:
1. int
2. float
3. str
4. bool
5. list
6. tuple
7. dict
8. set
"""

# -------------------------------------------------------------------
# 1. Integers (int)
# -------------------------------------------------------------------
# Integers are whole numbers, positive or negative.

age = 30
temperature = -5
score = 1023

print("Age:", age)
print("Temperature:", temperature)
print("Score:", score)
print("Type of score:", type(score))

# Use Case Example: Calculating total marks
math = 85
science = 90
english = 88
total_marks = math + science + english
print("Total Marks:", total_marks)

# -------------------------------------------------------------------
# 2. Floats (float)
# -------------------------------------------------------------------
# Floats represent decimal numbers.

price = 99.99
discount = 0.15
final_price = price * (1 - discount)
print("\nFinal Price after Discount:", final_price)

# Use Case Example: Currency conversion
usd_to_inr = 83.14
amount_usd = 250
amount_inr = amount_usd * usd_to_inr
print("250 USD in INR:", amount_inr)

# -------------------------------------------------------------------
# 3. Strings (str)
# -------------------------------------------------------------------
# Strings represent text enclosed in quotes.

name = "Vijay Rastogi"
profession = 'Data Scientist'
quote = """Learning Python step by step builds a solid foundation."""

print("\nName:", name)
print("Profession:", profession)
print("Quote:", quote)
print("First Letter of Name:", name[0])
print("Substring (first 5 letters):", name[:5])

# Use Case Example: Creating a formatted message
welcome_message = f"Hello {name}, welcome to Python learning!"
print(welcome_message)

# -------------------------------------------------------------------
# 4. Booleans (bool)
# -------------------------------------------------------------------
# Represents logical True or False values.

is_logged_in = True
has_permission = False

print("\nIs Logged In:", is_logged_in)
print("Has Permission:", has_permission)
print("Type of is_logged_in:", type(is_logged_in))

# Use Case Example: Access control simulation
if is_logged_in and has_permission:
    print("Access Granted!")
else:
    print("Access Denied.")

# -------------------------------------------------------------------
# 5. Lists (list)
# -------------------------------------------------------------------
# Lists are ordered, mutable (changeable) collections.

fruits = ["apple", "banana", "cherry"]
print("\nFruits List:", fruits)

# Accessing elements
print("First Fruit:", fruits[0])

# Modifying list
fruits.append("mango")
fruits.remove("banana")
print("Updated Fruits List:", fruits)

# Use Case Example: Managing a shopping cart
shopping_cart = ["milk", "bread"]
shopping_cart.append("eggs")
shopping_cart.append("butter")
print("Shopping Cart Items:", shopping_cart)

# -------------------------------------------------------------------
# 6. Tuples (tuple)
# -------------------------------------------------------------------
# Tuples are ordered but immutable collections.

coordinates = (28.7041, 77.1025)  # (latitude, longitude)
print("\nCoordinates:", coordinates)
print("Latitude:", coordinates[0])

# Use Case Example: Storing constant configuration
server_config = ("192.168.1.10", 8080)
print("Server Config:", server_config)

# -------------------------------------------------------------------
# 7. Dictionaries (dict)
# -------------------------------------------------------------------
# Dictionaries store data in key-value pairs.

person = {
    "name": "Vijay",
    "age": 30,
    "profession": "Data Scientist"
}

print("\nPerson Dictionary:", person)
print("Name:", person["name"])

# Modifying values
person["age"] = 31
print("Updated Person:", person)

# Use Case Example: Storing user data
user_data = {
    "username": "vijay_r",
    "email": "vijay@example.com",
    "logged_in": True
}
print("User Logged In:", user_data["logged_in"])

# -------------------------------------------------------------------
# 8. Sets (set)
# -------------------------------------------------------------------
# Sets are unordered collections of unique elements.

colors = {"red", "green", "blue", "green"}  # Duplicate removed automatically
print("\nColors Set:", colors)

# Adding a new color
colors.add("yellow")
print("Updated Colors:", colors)

# Use Case Example: Removing duplicate entries from a list
duplicate_emails = ["a@example.com", "b@example.com", "a@example.com"]
unique_emails = set(duplicate_emails)
print("Unique Emails:", unique_emails)

# -------------------------------------------------------------------
# 9. Type Conversion (Casting)
# -------------------------------------------------------------------
# Converting one data type to another.

num_str = "100"
num_int = int(num_str)
print("\nConverted String to Int:", num_int)

price_float = 9.99
price_str = str(price_float)
print("Converted Float to String:", price_str)

# Use Case Example: Input handling
user_input = "45"
result = int(user_input) + 5
print("Result after Conversion:", result)

# -------------------------------------------------------------------
# 10. None Type
# -------------------------------------------------------------------
# Represents the absence of a value.

data = None
print("\nData:", data)
print("Type of data:", type(data))

# Use Case Example: Placeholder variable before value assignment
config = None
if config is None:
    print("Configuration not loaded yet.")
