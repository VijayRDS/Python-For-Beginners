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

# ============================================
# 📘 Python Data Types — Explained in Depth
# ============================================

# Python has several built-in data types that help structure and manage data.
# These can be broadly classified into:
# 1️⃣ Numeric Types
# 2️⃣ Sequence Types
# 3️⃣ Set Types
# 4️⃣ Mapping Types
# 5️⃣ Boolean Type
# 6️⃣ None Type

# ------------------------------------------------
# 1️⃣ NUMERIC TYPES: int, float, complex
# ------------------------------------------------

# Integers: Whole numbers
x = 42
print("Integer:", x, type(x))

# Floats: Decimal numbers
price = 99.99
print("Float:", price, type(price))

# Complex numbers: used in scientific and engineering calculations
z = 3 + 4j
print("Complex:", z, type(z))

# 🔹 Practical Use Case:
# - Bank balance calculations (float)
# - Machine learning computations (float)
# - Electrical circuit calculations (complex)

# Example: Calculating compound interest
principal = 10000
rate = 5
time = 2
amount = principal * (1 + rate/100) ** time
print("Compound Interest:", amount)


# ------------------------------------------------
# 2️⃣ SEQUENCE TYPES: str, list, tuple
# ------------------------------------------------

# Strings
message = "Python is powerful!"
print("String:", message.upper())

# Lists (Mutable)
shopping_list = ["Milk", "Bread", "Eggs"]
shopping_list.append("Butter")
print("List:", shopping_list)

# Tuples (Immutable)
coordinates = (27.2046, 77.4977)
print("Tuple:", coordinates)

# 🔹 Practical Use Case:
# - String: Sentiment analysis in NLP
# - List: Managing inventory
# - Tuple: Storing fixed configuration data


# ------------------------------------------------
# 3️⃣ SET TYPES: set, frozenset
# ------------------------------------------------

# Set: Unique, unordered elements
unique_items = {"apple", "banana", "apple", "cherry"}
print("Set:", unique_items)

# Frozenset: Immutable set
frozen = frozenset(["python", "java", "python"])
print("Frozenset:", frozen)

# 🔹 Practical Use Case:
# - Removing duplicates from user data
# - Tag management system
# - Ensuring unique records in a dataset


# ------------------------------------------------
# 4️⃣ MAPPING TYPE: dict
# ------------------------------------------------

# Dictionary: key-value pairs
user = {
    "name": "Vijay Rastogi",
    "role": "Banking Operations Manager",
    "goals": ["Data Science", "UPSC", "Startups"]
}
print("Dictionary:", user)

# Access value
print("User Role:", user["role"])

# 🔹 Practical Use Case:
# - JSON data handling in APIs
# - Employee database
# - Configuration settings


# ------------------------------------------------
# 5️⃣ BOOLEAN TYPE: bool
# ------------------------------------------------

is_logged_in = True
has_permission = False

# Example: Access control system
if is_logged_in and has_permission:
    print("Access Granted ✅")
else:
    print("Access Denied ❌")

# 🔹 Practical Use Case:
# - Security systems
# - Decision-making in automation


# ------------------------------------------------
# 6️⃣ NONE TYPE
# ------------------------------------------------

result = None
print("Result:", result)

# 🔹 Practical Use Case:
# - Database NULL values
# - Default return values in functions


# ============================================
# 💡 Summary of Real-World Use Cases
# ============================================

# ✅ Shopping cart management → list, dict
# ✅ Currency conversion → float, dict
# ✅ Access control → bool
# ✅ Removing duplicates → set
# ✅ Input validation → str, bool

# ============================================
# 🚀 Practice Exercise
# ============================================
# Write a program that:
# - Takes a list of expenses
# - Removes duplicates
# - Calculates total and average
# - Displays them neatly

expenses = [120, 150, 120, 80, 200, 150]
unique_expenses = set(expenses)
total = sum(unique_expenses)
average = total / len(unique_expenses)
print(f"\nExpenses Summary:\nUnique Expenses: {unique_expenses}\nTotal: ₹{total}\nAverage: ₹{average:.2f}")




# 03_data_types.py
# Understanding Python Data Types with Examples and Practical Use Cases
# Added: explicit examples for
#  - Shopping cart management
#  - Currency conversion
#  - Access control
#  - Removing duplicates
#  - Input validation

import re
from typing import List, Dict, Tuple

# ---------------------------
# Core data-type examples (brief)
# ---------------------------
def core_examples():
    # int, float, str, bool (quick show)
    age = 30
    price = 99.99
    name = "Vijay"
    is_active = True
    print("Core Types:", age, price, name, is_active)


# ---------------------------
# Practical Use Case 1:
# Shopping cart management
# ---------------------------
def add_item(cart: List[Dict], name: str, price: float, qty: int = 1):
    """Add an item; if exists, increase quantity."""
    for item in cart:
        if item["name"] == name:
            item["qty"] += qty
            return
    cart.append({"name": name, "price": price, "qty": qty})


def remove_item(cart: List[Dict], name: str):
    """Remove item by name."""
    cart[:] = [item for item in cart if item["name"] != name]


def cart_total(cart: List[Dict]) -> float:
    return sum(item["price"] * item["qty"] for item in cart)


def shopping_cart_example():
    print("\n--- Shopping Cart Management Example ---")
    cart = []
    add_item(cart, "milk", 45.0, 2)
    add_item(cart, "bread", 30.0, 1)
    add_item(cart, "eggs", 5.0, 12)
    add_item(cart, "milk", 45.0, 1)  # increments milk qty

    print("Cart items:", cart)
    print("Total (INR):", cart_total(cart))

    remove_item(cart, "bread")
    print("After removing bread:", cart)
    print("Total after removal (INR):", cart_total(cart))


# ---------------------------
# Practical Use Case 2:
# Currency conversion (simple, direct rates)
# ---------------------------
def convert_currency(amount: float, from_curr: str, to_curr: str, rates: Dict[Tuple[str, str], float]) -> float:
    """Convert amount using a direct-rate mapping: rates[(from,to)] = multiplier"""
    key = (from_curr.upper(), to_curr.upper())
    if key not in rates:
        raise ValueError(f"Conversion rate not found for {from_curr} -> {to_curr}")
    return amount * rates[key]


def currency_conversion_example():
    print("\n--- Currency Conversion Example ---")
    rates = {
        ("USD", "INR"): 83.14,
        ("INR", "USD"): 1 / 83.14,
        ("EUR", "USD"): 1.08,
    }
    usd_amount = 250.0
    inr = convert_currency(usd_amount, "USD", "INR", rates)
    print(f"{usd_amount} USD = {inr:.2f} INR")

    # chaining example (EUR -> USD -> INR)
    eur_amount = 100.0
    usd_from_eur = convert_currency(eur_amount, "EUR", "USD", rates)
    inr_from_eur = convert_currency(usd_from_eur, "USD", "INR", rates)
    print(f"{eur_amount} EUR ≈ {inr_from_eur:.2f} INR")


# ---------------------------
# Practical Use Case 3:
# Access control (simple login + role check)
# ---------------------------
USERS = {
    "vijay": {"password": "pass123", "roles": ["user", "editor"]},
    "admin": {"password": "root", "roles": ["admin", "user", "editor"]},
}


def authenticate(username: str, password: str) -> bool:
    user = USERS.get(username)
    return user is not None and user["password"] == password


def has_permission(username: str, required_role: str) -> bool:
    user = USERS.get(username)
    return user is not None and required_role in user["roles"]


def access_control_example():
    print("\n--- Access Control Example ---")
    uname = "vijay"
    pwd = "pass123"
    if authenticate(uname, pwd):
        print(f"{uname} authenticated.")
        if has_permission(uname, "admin"):
            print("Access granted: admin operations allowed.")
        else:
            print("Access limited: admin operations denied.")
    else:
        print("Authentication failed.")


# ---------------------------
# Practical Use Case 4:
# Removing duplicates (emails) and preserving order
# ---------------------------
def remove_duplicates_keep_order(seq: List[str]) -> List[str]:
    seen = set()
    out = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def duplicates_example():
    print("\n--- Removing Duplicates Example ---")
    emails = ["a@example.com", "b@example.com", "a@example.com", "c@example.com", "b@example.com"]
    print("Original:", emails)
    unique_unordered = list(set(emails))  # may reorder
    print("Unique (unordered):", unique_unordered)
    unique_ordered = remove_duplicates_keep_order(emails)
    print("Unique (preserve order):", unique_ordered)


# ---------------------------
# Practical Use Case 5:
# Input validation (age and email)
# ---------------------------
def validate_age(age_str: str) -> Tuple[bool, int]:
    """Return (is_valid, age_int_or_0). Accepts ages 0-120."""
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            return True, age
        return False, 0
    except ValueError:
        return False, 0


EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')


def validate_email(email: str) -> bool:
    return EMAIL_REGEX.match(email) is not None


def input_validation_example():
    print("\n--- Input Validation Example ---")
    tests = ["25", "0", "-2", "abc", "130"]
    for t in tests:
        valid, val = validate_age(t)
        print(f"Age input '{t}': valid={valid}, value={val}")

    emails = ["vijay@example.com", "invalid-email@", "a.b@co.in"]
    for e in emails:
        print(f"Email '{e}' valid? -> {validate_email(e)}")


# ---------------------------
# Runner
# ---------------------------
def main():
    core_examples()
    shopping_cart_example()
    currency_conversion_example()
    access_control_example()
    duplicates_example()
    input_validation_example()


if __name__ == "__main__":
    main()
