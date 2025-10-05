# =====================================================
# 🧮 06_functions.py
# Understanding Functions — Reusability & Modular Design
# =====================================================
# A function is a reusable block of code designed to perform a single task.
# Think of it like a machine: Input → Process → Output.

# -----------------------------------------------------
# 1️⃣ DEFINING AND CALLING A FUNCTION
# -----------------------------------------------------

def greet_user():
    print("Hello, welcome to the Python learning journey!")

# Function call
greet_user()

# 🔹 Use Case: Welcome message, logging, notification system


# -----------------------------------------------------
# 2️⃣ FUNCTION PARAMETERS & ARGUMENTS
# -----------------------------------------------------

def greet(name):
    print(f"Welcome, {name}! Ready to master Python?")

greet("Vijay")
greet("Riya")

# 🔹 Use Case: Personalized email templates, chatbots, or user onboarding.


# -----------------------------------------------------
# 3️⃣ RETURN STATEMENTS
# -----------------------------------------------------

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("\nSum of 10 and 20 is:", result)

# 🔹 Use Case: Mathematical models, billing systems, calculators.


# -----------------------------------------------------
# 4️⃣ DEFAULT ARGUMENTS
# -----------------------------------------------------

def power(base, exponent=2):
    return base ** exponent

print("\nSquare of 5:", power(5))
print("Cube of 3:", power(3, 3))

# 🔹 Use Case: Default configurations, power computations, AI model parameters.


# -----------------------------------------------------
# 5️⃣ KEYWORD ARGUMENTS
# -----------------------------------------------------

def order_summary(item, quantity, price):
    print(f"\nOrder Summary → Item: {item}, Quantity: {quantity}, Total: ₹{quantity * price}")

order_summary(price=50, item="Notebook", quantity=3)

# 🔹 Use Case: E-commerce order APIs, dynamic report generation.


# -----------------------------------------------------
# 6️⃣ VARIABLE LENGTH ARGUMENTS (*args, **kwargs)
# -----------------------------------------------------

def total_bill(*items):
    return sum(items)

print("\nTotal bill for items ₹100, ₹250, ₹50:", total_bill(100, 250, 50))

def user_profile(**info):
    print("\nUser Profile Data:")
    for key, value in info.items():
        print(f"{key}: {value}")

user_profile(name="Vijay", role="Manager", department="Operations")

# 🔹 Use Case: Dynamic data handling (CRM systems, API data ingestion)


# -----------------------------------------------------
# 7️⃣ VARIABLE SCOPE — LOCAL VS GLOBAL
# -----------------------------------------------------

tax_rate = 0.18  # Global variable

def calculate_tax(amount):
    local_tax = amount * tax_rate  # Accessing global variable
    return local_tax

print("\nTax on ₹1000:", calculate_tax(1000))

# 🔹 Use Case: Constants like interest rates, discount rates.


# -----------------------------------------------------
# 8️⃣ LAMBDA FUNCTIONS (Anonymous functions)
# -----------------------------------------------------

square = lambda x: x * x
print("\nSquare of 6 using lambda:", square(6))

# 🔹 Use Case: Inline short operations (sorting, filtering, functional programming)


# -----------------------------------------------------
# 9️⃣ RECURSION — FUNCTION CALLING ITSELF
# -----------------------------------------------------

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))

# 🔹 Use Case: Mathematical models, data structures (trees, graphs), simulations.


# -----------------------------------------------------
# 🔟 PRACTICAL MINI PROJECTS
# -----------------------------------------------------

# 🧾 1. GST CALCULATOR
def gst_calculator(amount, gst_rate=18):
    gst = amount * gst_rate / 100
    total = amount + gst
    return gst, total

gst, total = gst_calculator(1000)
print(f"\nGST: ₹{gst}, Total after GST: ₹{total}")

# 🧮 2. BANK INTEREST CALCULATOR
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print("Interest on ₹50000 at 8% for 2 years:", calculate_interest(50000, 8, 2))

# 📊 3. STUDENT RESULT AUTOMATION
def calculate_grade(scores):
    avg = sum(scores) / len(scores)
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    else:
        grade = "C"
    return avg, grade

scores = [85, 78, 92, 88]
average, grade = calculate_grade(scores)
print(f"\nAverage Score: {average}, Grade: {grade}")


# -----------------------------------------------------
# 🔁 FUNCTION AS INPUT (HIGHER ORDER FUNCTION)
# -----------------------------------------------------

def apply_operation(numbers, func):
    return [func(num) for num in numbers]

result = apply_operation([1, 2, 3, 4], lambda x: x * 2)
print("\nResult after doubling:", result)

# 🔹 Use Case: Data transformation in analytics pipelines.


# -----------------------------------------------------
# 📊 SUMMARY TABLE
# -----------------------------------------------------
# | Concept                | Syntax Example                          | Use Case                               |
# |------------------------|-----------------------------------------|----------------------------------------|
# | Basic Function         | def f(): return x                      | Reusable logic blocks                  |
# | Parameters             | def f(a, b):                           | Input customization                    |
# | Default Parameters     | def f(x=5):                            | Configuration defaults                 |
# | *args / **kwargs       | def f(*a, **kw):                       | Dynamic inputs                         |
# | Lambda Function        | lambda x: x*x                          | Short operations                       |
# | Recursion              | def f(): f()                           | Algorithms & tree traversals           |
# | Higher Order Function  | def f(func): func(x)                   | Functional data pipelines              |

print("\n✅ All function concepts executed successfully!")
