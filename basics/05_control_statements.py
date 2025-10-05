# =====================================================
# 🧭 05_control_statements.py
# Decision Making and Control Flow in Python
# =====================================================
# Control statements determine *how* and *when* code executes.
# They form the logic gates of software automation.

# -----------------------------------------------------
# 1️⃣ CONDITIONAL STATEMENTS (if, elif, else)
# -----------------------------------------------------
# They help your program make decisions based on conditions.

# Example 1: Simple if-else
balance = 1500
withdrawal = 1000

if balance >= withdrawal:
    print("✅ Withdrawal Successful!")
else:
    print("❌ Insufficient Balance!")

# Example 2: Multiple conditions using elif
temperature = 38

if temperature > 40:
    print("High Fever — Seek medical help immediately.")
elif temperature >= 37:
    print("Mild Fever — Take rest and fluids.")
else:
    print("Normal Temperature.")

# 🔹 Practical Use Case:
# - Fraud detection: Flag transactions above limit
# - Risk management: Conditional scoring
# - Workflow automation: Different action triggers

# Example 3: Fraud detection
amount = 250000
is_verified = False

if amount > 100000 and not is_verified:
    print("🚨 Suspicious Transaction: Needs Verification!")
else:
    print("✅ Transaction Approved!")


# -----------------------------------------------------
# 2️⃣ NESTED IF STATEMENTS
# -----------------------------------------------------
# When a decision depends on another decision.

user_logged_in = True
user_role = "admin"

if user_logged_in:
    if user_role == "admin":
        print("Access granted to Admin Dashboard.")
    else:
        print("Access granted to User Dashboard.")
else:
    print("Please log in first!")

# 🔹 Use Case: Access control, multi-level approvals.


# -----------------------------------------------------
# 3️⃣ LOOPS (for, while)
# -----------------------------------------------------
# Loops let your code repeat actions — essential in automation.

# Example 1: for loop (iterating over a list)
transactions = [120, 340, 560, 50, 999]
total = 0

for amount in transactions:
    total += amount

print("\n💰 Total Transactions:", total)

# Example 2: while loop
count = 1
while count <= 5:
    print("Iteration:", count)
    count += 1

# 🔹 Practical Use Case:
# - Processing large datasets
# - Counting iterations in simulations
# - Auto-retry in failed operations


# -----------------------------------------------------
# 4️⃣ BREAK, CONTINUE, and PASS
# -----------------------------------------------------
# break → stops the loop entirely
# continue → skips current iteration
# pass → does nothing (placeholder for future logic)

print("\n🔁 Loop Control Demonstration")

for i in range(1, 10):
    if i == 5:
        print("🚫 Breaking the loop at 5")
        break
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue
    print(f"Processing number: {i}")
else:
    print("Loop completed successfully!")  # executes only if loop didn’t break

# 🔹 Use Case: Skip invalid data, break infinite loops, reserve future logic


# -----------------------------------------------------
# 5️⃣ ADVANCED LOOP APPLICATIONS
# -----------------------------------------------------

# Example: Fraudulent Transaction Filter
transactions = [1200, 98000, 350, 200000, 750, 45000]
fraud_threshold = 100000

for txn in transactions:
    if txn > fraud_threshold:
        print(f"🚨 Fraud Alert: Transaction ₹{txn}")
        continue
    print(f"✅ Transaction ₹{txn} processed successfully!")

# Example: Data Validation with pass
data_points = ["Valid", None, "Valid", "", "Valid"]
for d in data_points:
    if not d:
        pass  # reserved for error logging later
    else:
        print("Processing:", d)


# -----------------------------------------------------
# 6️⃣ MINI PROJECT: AUTOMATED GRADE CALCULATOR
# -----------------------------------------------------
# Real-world workflow simulation

marks = {
    "Math": 88,
    "Science": 92,
    "English": 75,
    "History": 64,
    "Computer": 97
}

total = sum(marks.values())
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("\n📘 Student Grade Report")
print("========================")
for subject, score in marks.items():
    print(f"{subject}: {score}")
print(f"\nTotal Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")

# 🔹 Practical Use Cases:
# ✅ HR: Employee performance scoring
# ✅ Banking: Credit rating logic
# ✅ Education: Result evaluation


# -----------------------------------------------------
# 7️⃣ NESTED LOOPS
# -----------------------------------------------------
# Useful when dealing with matrices or multi-level data.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatrix Elements:")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # new line for each row

# 🔹 Use Case: Data table traversal, image pixel manipulation.


# -----------------------------------------------------
# 📊 SUMMARY TABLE
# -----------------------------------------------------
# | Control Type     | Keyword         | Business Use Case                  |
# |------------------|-----------------|------------------------------------|
# | if / elif / else | Conditional     | Workflow branching, decisions      |
# | for              | Iteration       | Batch processing, ETL loops        |
# | while            | Repetitive logic| Retry systems, monitoring          |
# | break            | Stop loop       | Fraud halt, termination logic      |
# | continue         | Skip iteration  | Skip invalid or duplicate data     |
# | pass             | Placeholder     | Future feature integration         |
