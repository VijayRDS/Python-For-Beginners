# ============================================
# ⚙️ Python Operators — The Power Behind Logic
# ============================================
# Operators are symbols that perform operations on variables and values.
# They are the *decision-makers* of your code — the logic engine.

# ------------------------------------------------
# 1️⃣ ARITHMETIC OPERATORS
# ------------------------------------------------
# +, -, *, /, %, **, //

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)

# 🔹 Practical Use Case:
# - Banking app interest computation
# - E-commerce billing and discounts
# - EMI calculator

# Example: EMI Calculation Formula (Simplified)
principal = 100000
rate = 10 / 100 / 12
tenure = 12
emi = principal * rate * (1 + rate)**tenure / ((1 + rate)**tenure - 1)
print("\nMonthly EMI:", round(emi, 2))


# ------------------------------------------------
# 2️⃣ COMPARISON OPERATORS
# ------------------------------------------------
# ==, !=, >, <, >=, <=

x = 20
y = 25

print("\nEqual to:", x == y)
print("Not Equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal:", x >= y)
print("Less than or equal:", x <= y)

# 🔹 Practical Use Case:
# - Eligibility checking (loan approval, age validation)
# - Ranking systems (students, employees)
# - Conditional execution in workflows

# Example: Loan eligibility check
age = 27
salary = 40000
if age > 21 and salary >= 30000:
    print("Eligible for Loan ✅")
else:
    print("Not Eligible ❌")


# ------------------------------------------------
# 3️⃣ LOGICAL OPERATORS
# ------------------------------------------------
# and, or, not

is_logged_in = True
has_subscription = False

print("\nAND Operator:", is_logged_in and has_subscription)
print("OR Operator:", is_logged_in or has_subscription)
print("NOT Operator:", not has_subscription)

# 🔹 Practical Use Case:
# - Access control (Admin panels)
# - Workflow automation
# - AI decision logic

# Example: Access system
if is_logged_in and has_subscription:
    print("Access Granted to Premium Dashboard")
elif is_logged_in:
    print("Access Granted to Basic Dashboard")
else:
    print("Login Required")


# ------------------------------------------------
# 4️⃣ ASSIGNMENT OPERATORS
# ------------------------------------------------
# =, +=, -=, *=, /=, %=, //=, **=

count = 10
count += 5  # equivalent to count = count + 5
print("\nUpdated Count:", count)

balance = 1000
balance -= 200  # deduction
balance += 500  # credit
print("Updated Balance:", balance)

# 🔹 Practical Use Case:
# - Wallet updates
# - Game score tracking
# - Inventory stock management


# ------------------------------------------------
# 5️⃣ MEMBERSHIP OPERATORS
# ------------------------------------------------
# in, not in

users = ["Vijay", "Riya", "Amit"]

print("\nIs Vijay a user?", "Vijay" in users)
print("Is Rahul not a user?", "Rahul" not in users)

# 🔹 Practical Use Case:
# - Authentication systems
# - Access validation
# - Keyword search in NLP

# Example: Email whitelist system
allowed_domains = ["gmail.com", "icicibank.com"]
email = "vijay@icicibank.com"
if any(domain in email for domain in allowed_domains):
    print("Corporate Access Granted ✅")
else:
    print("Access Denied ❌")


# ------------------------------------------------
# 6️⃣ IDENTITY OPERATORS
# ------------------------------------------------
# is, is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nCheck Identity (is):", a is b)
print("Check Equality (==):", a == c)
print("Check Identity (is not):", a is not c)

# 🔹 Practical Use Case:
# - Memory optimization
# - Reference checking (useful in large data structures)


# ------------------------------------------------
# 7️⃣ BITWISE OPERATORS
# ------------------------------------------------
# &, |, ^, ~, <<, >>

x = 10  # 1010
y = 4   # 0100

print("\nAND:", x & y)
print("OR:", x | y)
print("XOR:", x ^ y)
print("NOT (~x):", ~x)
print("Left Shift (x << 1):", x << 1)
print("Right Shift (x >> 1):", x >> 1)

# 🔹 Practical Use Case:
# - Cryptography
# - Network programming
# - Image compression and optimization


# ============================================
# 💡 PRACTICAL MINI PROJECT
# ============================================

# 🧾 Billing System Simulation
# Calculate total price after discount and tax

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
print(f"Total Price (with tax): ₹{round(total_price, 2)}")

# 🔹 Use Cases:
# ✅ Finance — invoice computation
# ✅ Retail — shopping cart engine
# ✅ SaaS — subscription billing system


# ============================================
# 📊 SUMMARY CHART
# ============================================

# | Operator Type      | Examples             | Business Use Case                 |
# |--------------------|---------------------|-----------------------------------|
# | Arithmetic         | +, -, /, %          | Billing, interest calc            |
# | Comparison         | ==, >, <=           | Eligibility, validation           |
# | Logical            | and, or, not        | Access control                    |
# | Assignment         | +=, -=, *=          | Updating balance, score           |
# | Membership         | in, not in          | Authentication, search            |
# | Identity           | is, is not          | Reference tracking                |
# | Bitwise            | &, |, ^, <<, >>     | Networking, encryption            |
