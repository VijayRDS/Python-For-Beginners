# ===============================================================
# ⚙️ PYTHON OPERATORS — The Logic Engine of Your Code
# ===============================================================
# Operators are special symbols that perform operations on variables and values.
# They are the *decision-makers* of every program — enabling logic, math, and automation.

# ===============================================================
# 1️⃣ ARITHMETIC OPERATORS
# ===============================================================
# +, -, *, /, %, **, //

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)  # Removes decimals
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)

# 🔹 Real-World Example — EMI Calculation
principal = 100000
rate = 10 / 100 / 12   # 10% annual → monthly
tenure = 12            # months

emi = principal * rate * (1 + rate)**tenure / ((1 + rate)**tenure - 1)
print("\nMonthly EMI:", round(emi, 2))


# ===============================================================
# 2️⃣ COMPARISON OPERATORS
# ===============================================================
# ==, !=, >, <, >=, <=

x = 20
y = 25

print("\nEqual to:", x == y)
print("Not Equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal:", x >= y)
print("Less than or equal:", x <= y)

# 🔹 Example — Loan Eligibility
age = 27
salary = 40000
if age > 21 and salary >= 30000:
    print("Eligible for Loan ✅")
else:
    print("Not Eligible ❌")


# ===============================================================
# 3️⃣ LOGICAL OPERATORS
# ===============================================================
# and, or, not

is_logged_in = True
has_subscription = False

print("\nAND Operator:", is_logged_in and has_subscription)
print("OR Operator:", is_logged_in or has_subscription)
print("NOT Operator:", not has_subscription)

# 🔹 Example — Access Control System
if is_logged_in and has_subscription:
    print("Access: Premium Dashboard")
elif is_logged_in:
    print("Access: Basic Dashboard")
else:
    print("Please Log In")


# ===============================================================
# 4️⃣ ASSIGNMENT OPERATORS
# ===============================================================
# =, +=, -=, *=, /=, %=, //=, **=

count = 10
count += 5  # same as count = count + 5
print("\nUpdated Count:", count)

balance = 1000
balance -= 200  # debit
balance += 500  # credit
print("Updated Balance:", balance)

# 🔹 Example — Wallet Update System


# ===============================================================
# 5️⃣ MEMBERSHIP OPERATORS
# ===============================================================
# in, not in

users = ["Vijay", "Riya", "Amit"]

print("\nIs Vijay a user?", "Vijay" in users)
print("Is Rahul not a user?", "Rahul" not in users)

# 🔹 Example — Email Domain Check
allowed_domains = ["gmail.com", "icicibank.com"]
email = "vijay@icicibank.com"
if any(domain in email for domain in allowed_domains):
    print("Corporate Access Granted ✅")
else:
    print("Access Denied ❌")


# ===============================================================
# 6️⃣ IDENTITY OPERATORS
# ===============================================================
# is, is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nCheck Identity (a is b):", a is b)   # Same object
print("Check Equality (a == c):", a == c)     # Same value
print("Check Identity (a is not c):", a is not c)

# 🔹 Use Case: Object reference and memory optimization


# ===============================================================
# 7️⃣ BITWISE OPERATORS
# ===============================================================
# &, |, ^, ~, <<, >>

x = 10  # 1010 (binary)
y = 4   # 0100 (binary)

print("\nAND:", x & y)        # 0000 → 0
print("OR:", x | y)           # 1110 → 14
print("XOR:", x ^ y)          # 1110 → 14
print("NOT (~x):", ~x)
print("Left Shift (x << 1):", x << 1)
print("Right Shift (x >> 1):", x >> 1)

# 🔹 Example — Network / Encryption Applications


# ===============================================================
# 💡 MINI PROJECT: SMART BILLING SYSTEM
# ===============================================================
# Task: Calculate total amount after discount and tax.

price = 500
quantity = 3
discount = 10  # percent
tax = 5        # percent

subtotal = price * quantity
discount_amount = subtotal * discount / 100
after_discount = subtotal - discount_amount
total_price = after_discount + (after_discount * tax / 100)

print(f"\nSubtotal: ₹{subtotal}")
print(f"After Discount: ₹{after_discount}")
print(f"Total Price (with Tax): ₹{round(total_price, 2)}")

# ✅ Used in: Retail Billing, Finance Systems, E-commerce Pricing


# ===============================================================
# 📊 QUICK REFERENCE TABLE
# ===============================================================

# | Operator Type  | Examples         | Real-World Use Case           |
# |----------------|------------------|-------------------------------|
# | Arithmetic     | +, -, *, /       | Billing, Interest Calc        |
# | Comparison     | ==, >, <=        | Eligibility, Validation       |
# | Logical        | and, or, not     | Access Control, Decision Tree |
# | Assignment     | +=, -=, *=       | Score, Wallet, Inventory      |
# | Membership     | in, not in       | Authentication, Search        |
# | Identity       | is, is not       | Memory, Reference             |
# | Bitwise        | &, |, ^, <<, >>  | Encryption, Networking        |


# ===============================================================
# 🧠 PRACTICAL EXERCISES
# ===============================================================

# 1️⃣ Shopping Cart Total
prices = [250, 399, 150, 99]
total = 0
for price in prices:
    total += price
print("\n🛒 Cart Total:", total)

# 2️⃣ Currency Conversion
usd_to_inr = 83.2
dollars = 100
print(f"${dollars} = ₹{dollars * usd_to_inr}")

# 3️⃣ Access Control Logic
age = 17
has_permission = True
if age >= 18 or has_permission:
    print("Access Granted ✅")
else:
    print("Access Denied ❌")

# 4️⃣ Removing Duplicates (using `in`)
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Unique List:", unique)

# 5️⃣ Simple Login Validation
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful 🔓")
else:
    print("Invalid Credentials 🚫")

# ===============================================================
# 🏁 End of Lesson — Operators Mastered!
# ===============================================================
