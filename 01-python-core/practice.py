"""
Day 1 — Python Fundamentals: Practice Script
=============================================
This file is proof-of-work: every concept from today's notes,
written as runnable code, not just theory.

Run it with: python day-01-practice.py
"""

# ---------------------------------------------------------
# 1. VARIABLES, DATA TYPES & CASTING
# ---------------------------------------------------------
print("=" * 50)
print("1. VARIABLES, DATA TYPES & CASTING")
print("=" * 50)

name = "Aarav"
age = 25
height = 5.9
is_student = False

print(f"{name} is {age} years old, {height} ft tall. Student? {is_student}")
print(type(name), type(age), type(height), type(is_student))

# Casting in action
user_input = "30"          # imagine this came from input()
age_as_int = int(user_input)
print("Casted age:", age_as_int, type(age_as_int))


# ---------------------------------------------------------
# 2. STRINGS
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("2. STRINGS")
print("=" * 50)

sentence = "  Data Science is Fun  "
cleaned = sentence.strip()
print("Cleaned:", repr(cleaned))
print("Uppercase:", cleaned.upper())
print("Word count:", len(cleaned.split()))
print("Reversed:", cleaned[::-1])
print("First 4 chars:", cleaned[:4])

product = "Laptop"
price = 55499.5
print(f"Product: {product}, Price: ₹{price:.2f}")


# ---------------------------------------------------------
# 3. LISTS, TUPLES, SETS, DICTS
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("3. DATA STRUCTURES")
print("=" * 50)

# List — mutable, ordered
scores = [85, 92, 78, 95, 60]
scores.append(88)
scores.sort(reverse=True)
print("Sorted scores (desc):", scores)
print("Above 80:", [s for s in scores if s > 80])   # list comprehension

# Tuple — immutable, fixed record
coordinates = (28.6, 77.2)
lat, lon = coordinates   # unpacking
print(f"Lat: {lat}, Lon: {lon}")

# Set — unique values, fast membership
tags_a = {"python", "sql", "excel"}
tags_b = {"python", "pandas", "numpy"}
print("Union:", tags_a | tags_b)
print("Shared:", tags_a & tags_b)
print("Only in A:", tags_a - tags_b)

# Dict — labeled data
student = {
    "name": "Priya",
    "grade": "A",
    "subjects": ["Math", "Physics"]
}
student["age"] = 22   # add new key
for key, value in student.items():
    print(f"{key} -> {value}")


# ---------------------------------------------------------
# 4. CONTROL FLOW
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("4. CONTROL FLOW")
print("=" * 50)

def grade_from_marks(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

for m in [95, 80, 55, 30]:
    print(f"Marks {m} -> Grade {grade_from_marks(m)}")

# while loop example
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Liftoff!")


# ---------------------------------------------------------
# 5. FUNCTIONS (incl. *args, lambda)
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("5. FUNCTIONS")
print("=" * 50)

def total_price(*items, discount=0):
    """Sums prices, applies an optional discount %."""
    subtotal = sum(items)
    return subtotal * (1 - discount / 100)

print("Total with 10% discount:", total_price(299, 149, 599, discount=10))

# Lambda used the way it's actually useful — as a sort key
people = [("Priya", 85), ("Rohan", 72), ("Meera", 91)]
people.sort(key=lambda person: person[1])
print("Sorted by score:", people)


# ---------------------------------------------------------
# 6. MINI DATA-CLEANING EXERCISE (preview of what's next)
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("6. MINI DATA-CLEANING PREVIEW")
print("=" * 50)

raw_prices = ["  ₹1,299.00  ", "₹599.50", "  ₹2,000  ", "₹undefined"]

def clean_price(raw):
    """Strips currency symbol/commas/spaces; returns None if not a number."""
    text = raw.strip().replace("₹", "").replace(",", "")
    try:
        return float(text)
    except ValueError:
        return None

cleaned_prices = [clean_price(p) for p in raw_prices]
print("Raw:    ", raw_prices)
print("Cleaned:", cleaned_prices)

valid_prices = [p for p in cleaned_prices if p is not None]
print("Average of valid prices:", round(sum(valid_prices) / len(valid_prices), 2))

print("\n✅ All Day 1 concepts executed successfully.")
