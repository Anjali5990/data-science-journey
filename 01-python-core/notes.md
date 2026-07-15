# 📘 Day 1 — Python Fundamentals

**Goal:** Build a rock-solid foundation in core Python before moving into data handling, SQL, statistics, and ML/AI.

This log is proof of what was studied and understood today — not just a list of topics, but a record of the *why* behind each one.

---

## ✅ Topics Covered

### 1. Setting Up
- Understood the two ways to write/run Python: **notebooks** (Colab/Jupyter — for exploration) vs **code editors/IDEs** (VS Code/PyCharm — for building software).
- Learned why Python is the standard for Data Science: readable syntax + huge ecosystem (NumPy, Pandas, Scikit-learn) + it powers the *entire* pipeline (data → EDA → ML → deployment).
- Key insight: Python itself is slow, but libraries like NumPy do the heavy lifting in C/Fortran under the hood — so DS work gets simplicity *and* speed.

### 2. Syntax & Style
- Indentation is **mandatory** in Python (not a style choice) — defines code blocks.
- Case-sensitivity, reserved keywords, comments (`#`), and one-statement-per-line conventions.
- **PEP8**: Python's official style guide — `snake_case` for variables/functions, `PascalCase` for classes, 4-space indentation, meaningful names.

### 3. Variables & Data Types
- Variables as labeled memory — dynamically typed, no need to declare a type.
- Multiple assignment & unpacking: `x, y, z = 1, 2, 3`
- Core types: `int`, `float`, `complex`, `str`, `list`, `tuple`, `dict`, `set`, `bool`, `NoneType`
- **Global keyword & scope**: local vs global variables, and why modifying a global from inside a function requires `global`.
- **Casting**: `int()`, `float()`, `str()` — explicit vs implicit conversion.

### 4. Input / Output & Comments
- `print()` with `sep`, `end`, and f-strings for formatting.
- `input()` always returns a string — a very common source of bugs if not cast properly.
- Comments explain *why*, not *what*.

### 5. Strings
- Indexing (positive & negative), slicing (`start:end:step`), immutability.
- Key methods: `.upper()`, `.strip()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.count()`, `.startswith()`/`.endswith()`, `.title()`, `.zfill()`, and more.
- String formatting: `%`-style (legacy), `.format()`, and **f-strings** (modern default).
- Escape characters (`\n`, `\t`, `\\`, `\"`).

### 6. Booleans & Operators
- Booleans come from comparisons; Python's "truthiness" rules (`0`, `""`, `[]`, `None` → falsy).
- Full operator set: arithmetic, assignment (`+=` etc.), comparison, logical (`and`/`or`/`not`), identity (`is` vs `==`), membership (`in`), and bitwise (rarely used in DS).
- Understood the **mutability trap**: `b = a` shares the same object; `.copy()` is needed for independence.

### 7. Data Structures
| Structure | Ordered | Mutable | Duplicates | Access |
|---|---|---|---|---|
| **List** `[]` | ✅ | ✅ | ✅ | index |
| **Tuple** `()` | ✅ | ❌ | ✅ | index |
| **Set** `{}` | ❌ | ✅ | ❌ | membership only |
| **Dict** `{k:v}` | ✅ (3.7+) | ✅ | keys: ❌ / values: ✅ | key |

- Covered methods for each in depth: adding/removing items, sorting, copying (shallow vs `deepcopy`), comprehensions, joining, and set math (`union`, `intersection`, `difference`, `symmetric_difference`).
- Understood **why each exists** — e.g., tuples for fixed/safe data, sets for fast membership checks, dicts for labeled/fast lookup (the same shape as JSON & pandas DataFrames).

### 8. Control Flow
- `if` / `elif` / `else`, nested conditionals, shorthand/ternary expressions.
- `and` / `or` / `not` to combine conditions cleanly.
- `for` loops (incl. `range()`, `enumerate()`) and `while` loops — and *why* to use one over the other.
- `break`, `continue`, `pass`, and the newer `match` statement for structural pattern matching.

### 9. Functions
- Defining vs calling — `def` just creates the function, it doesn't run it.
- Parameters vs arguments, default values, keyword arguments, `*args` / `**kwargs`.
- **Return values** vs `print()` — the difference between showing something and actually giving it back to reuse.
- Variable scope: local vs global, and why relying on `global` is usually avoided in favor of parameters + return values.
- Intro to **lambda functions**, **recursion**, **decorators**, and **generators** (`yield` vs `return`) — the more advanced building blocks used throughout real Python code (sorting keys, memory-efficient data processing, etc.).

---

## 🧠 Key Takeaways
- Every data structure is a trade-off — the goal isn't memorizing methods, but knowing *which container fits which problem*.
- Mutability is the concept that explains half of Python's "gotchas" (shared references, copy traps, default argument bugs).
- Dictionaries are the mental model for real-world structured data (JSON, APIs, pandas DataFrames) — this is why they got special attention.

## 🔜 Next Up
Data handling with Pandas → SQL → Statistics → EDA → ML → AI/LLM tooling.

---
*Log generated as part of a self-directed Python → Data Science learning roadmap.*
