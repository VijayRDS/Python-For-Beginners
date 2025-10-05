# ================================================================
# 📘 03_data_types.py
# Author: Vijay Rastogi
# Purpose: Learn Python Data Types with Real-World Use Cases
# Version: 1.2 (Updated: Oct 2025)
# ================================================================

"""
Python is dynamically typed — you don’t need to declare variable types.
The interpreter figures them out at runtime.

📚 Major Built-in Data Types:
1️⃣ int
2️⃣ float
3️⃣ str
4️⃣ bool
5️⃣ list
6️⃣ tuple
7️⃣ dict
8️⃣ set
9️⃣ NoneType
"""

import re
from typing import List, Dict, Tuple


# ================================================================
# Helper Function for Readable Output
# ================================================================
def print_header(title: str):
    """Prints a formatted section header"""
    print("\n" + "=" * 60)
    print(f"🔹 {title.upper()}")
    print("=" * 60)


# ================================================================
# Core Data Type Examples
# ================================================================
def core_examples():
    print_header("Core Python Data Types")

    age = 30                     # int
    price = 99.99                # float
    name = "Vijay"               # str
    is_active = True             # bool

    print("Core Values:", age, price, name, is_active)
    print("Types:", type(age), type(price), type(name), type(is_active))

    # Use Case Example: Simple math
    total = age + 10
    print("Age after 10 years:", total)


# ================================================================
# Practical Use Case 1: Shopping Cart Management
# ================================================================
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
    """Compute total price"""
    return sum(item["price"] * item["qty"] for item in cart)


def shopping_cart_example():
    print_header("Shopping Cart Management")

    cart = []
    add_item(cart, "Milk", 45.0, 2)
    add_item(cart, "Bread", 30.0, 1)
    add_item(cart, "Eggs", 5.0, 12)
    add_item(cart, "Milk", 45.0, 1)  # increments milk qty

    print("Cart Items:", cart)
    print(f"Total (INR): ₹{cart_total(cart):.2f}")

    remove_item(cart, "Bread")
    print("After removing Bread:", cart)
    print(f"Total after removal: ₹{cart_total(cart):.2f}")


# ================================================================
# Practical Use Case 2: Currency Conversion
# ================================================================
def convert_currency(amount: float, from_curr: str, to_curr: str, rates: Dict[Tuple[str, str], float]) -> float:
    """Convert amount using a direct-rate mapping: rates[(from,to)] = multiplier"""
    key = (from_curr.upper(), to_curr.upper())
    if key not in rates:
        raise ValueError(f"Conversion rate not found for {from_curr} -> {to_curr}")
    return amount * rates[key]


def currency_conversion_example():
    print_header("Currency Conversion")

    rates = {
        ("USD", "INR"): 83.14,
        ("INR", "USD"): 1 / 83.14,
        ("EUR", "USD"): 1.08,
    }

    usd_amount = 250.0
    inr = convert_currency(usd_amount, "USD", "INR", rates)
    print(f"{usd_amount} USD = ₹{inr:.2f} INR")

    # Chained Conversion (EUR → USD → INR)
    eur_amount = 100.0
    usd_from_eur = convert_currency(eur_amount, "EUR", "USD", rates)
    inr_from_eur = convert_currency(usd_from_eur, "USD", "INR", rates)
    print(f"{eur_amount} EUR ≈ ₹{inr_from_eur:.2f} INR")

    # Demonstrate Error Handling
    try:
        convert_currency(100, "GBP", "INR", rates)
    except ValueError as e:
        print("Error:", e)


# ================================================================
# Practical Use Case 3: Access Control System
# ================================================================
USERS = {
    "vijay": {"password": "pass123", "roles": ["user", "editor"]},
    "admin": {"password": "root", "roles": ["admin", "user", "editor"]},
}


def authenticate(username: str, password: str) -> bool:
    """Check login credentials"""
    user = USERS.get(username)
    return user is not None and user["password"] == password


def has_permission(username: str, required_role: str) -> bool:
    """Check role permissions"""
    user = USERS.get(username)
    return user is not None and required_role in user["roles"]


def access_control_example():
    print_header("Access Control System")

    uname = "vijay"
    pwd = "pass123"

    if authenticate(uname, pwd):
        print(f"{uname} authenticated ✅")
        if has_permission(uname, "admin"):
            print("Admin access granted.")
        elif has_permission(uname, "editor"):
            print("Editor access granted: You can edit content.")
        else:
            print("Basic user access only.")
    else:
        print("Authentication failed ❌")


# ================================================================
# Practical Use Case 4: Removing Duplicates
# ================================================================
def remove_duplicates_keep_order(seq: List[str]) -> List[str]:
    """Remove duplicates while preserving order"""
    seen = set()
    out = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def duplicates_example():
    print_header("Removing Duplicates")

    emails = ["a@example.com", "b@example.com", "a@example.com", "c@example.com", "b@example.com"]
    print("Original:", emails)

    unique_unordered = list(set(emails))  # may reorder
    print("Unique (unordered):", unique_unordered)

    unique_ordered = remove_duplicates_keep_order(emails)
    print("Unique (order preserved):", unique_ordered)


# ================================================================
# Practical Use Case 5: Input Validation
# ================================================================
EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')


def validate_age(age_str: str) -> Tuple[bool, int]:
    """Return (is_valid, age_int). Accepts ages 0-120."""
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            return True, age
        return False, 0
    except ValueError:
        return False, 0


def validate_email(email: str) -> bool:
    """Validate email format"""
    return EMAIL_REGEX.match(email) is not None


def input_validation_example():
    print_header("Input Validation")

    # Age Validation
    tests = ["25", "0", "-2", "abc", "130"]
    for t in tests:
        valid, val = validate_age(t)
        print(f"Age '{t}': valid={valid}, value={val}")

    # Email Validation
    emails = ["vijay@example.com", "invalid-email@", "a.b@co.in"]
    for e in emails:
        print(f"Email '{e}': valid? {validate_email(e)}")


# ================================================================
# Data Type Summary
# ================================================================
def summary():
    print_header("Python Data Type Summary")
    print("Numeric     → int, float, complex")
    print("Sequence    → str, list, tuple")
    print("Mapping     → dict")
    print("Set Type    → set, frozenset")
    print("Boolean     → bool")
    print("None Type   → None")
    print("\n✅ Real-World Examples:")
    print(" - Shopping cart → list, dict")
    print(" - Currency conversion → float, dict")
    print(" - Access control → bool, dict")
    print(" - Removing duplicates → set")
    print(" - Input validation → str, bool")


# ================================================================
# Main Runner
# ================================================================
def main():
    core_examples()
    shopping_cart_example()
    currency_conversion_example()
    access_control_example()
    duplicates_example()
    input_validation_example()
    summary()


if __name__ == "__main__":
    main()
