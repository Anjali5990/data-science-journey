**Python Notes**

**Setting up somewhere to write code**

Python code needs something to run it. Your computer does not understand Python directly, so you need a program that reads your code and executes it and shows you the result. These tools are broadly of two types.

**Notebooks (best for learning and data science)**

A notebook is a document where you write small chunks of code called cells, run them one at a time, and immediately see results right below that cell, mixed with your own notes. Data scientists like this because you can explore data step by step and explain your thinking alongside the code. Common tools are Google Colab (runs in the browser, free, nothing to install, needs a Google account) and Jupyter Notebook (similar, but installed on your own computer).

**Code editors and IDEs (best for building real software)**

A text editor made for writing full programs, running the whole file at once. Common tools are VS Code and PyCharm.

**Core Definitions**

Programming language: a way to give instructions to a computer, written in a form humans can understand and write, which then gets converted into machine code the computer can execute.

High level language: a programming language that is close to human language, easy to read and write, and hides the complex hardware details from the programmer. Example: Python.

Low level language: closer to machine code, harder for humans to read, but very fast and closer to hardware. Example: C, Assembly.

Interpreted language: one where the code is read and executed line by line by an interpreter at runtime, instead of being converted into machine code all at once beforehand. Python is an interpreted language.

Compiled language: one where the entire code is translated into machine code beforehand using a compiler, before it is run. Example: C, C++.

Python: a high level, interpreted, general purpose programming language, known for its simple and readable syntax. Widely used in Data Science, AI, web development, and automation.

**Why Python Is Used In Data Science Despite Being Slow**

Python is a high level, interpreted language, easy to read and write, but slower than low level languages like C. For Data Science this speed issue does not matter in practice because libraries like NumPy and Pandas are written in Python on the outside, but their internal heavy calculations are done using C and sometimes Fortran, which are much faster. So Python gives a simple interface while C and Fortran act as the fast engine underneath. The result is easy readable Python code with near C speed for calculations.

**Why Python Specifically For Data Science**

Easy readable syntax, closer to plain English than most languages, so you can focus on logic instead of fighting the language.

Huge ecosystem of libraries built for data work: NumPy for numeric arrays, Pandas for tabular data, Matplotlib and Seaborn for visualization, Scikit learn for classic ML, TensorFlow and PyTorch for deep learning.

Industry standard, almost every Data Science and ML job expects Python, so skills transfer directly to real jobs.

Same language for the whole pipeline, you can clean data, analyze it, build a model, and even deploy it, all in Python.

**Where Programming Fits Into The Data Scientist Role**

The role broadly looks like this: business problem, get data, clean data, explore data, build model, evaluate model, communicate results or deploy.

Programming in Python is the tool used at every step of that chain, pulling data from a database with SQL, transforming it with Pandas, running statistics, training ML models, and increasingly calling AI or LLM APIs to automate parts of the workflow. This is exactly why the learning order is Python, then data handling, then SQL, then stats, then EDA, then ML, then the AI and LLM layer. The AI and LLM part comes last because it is most useful once you already understand what is happening underneath, otherwise you are just trusting a black box instead of directing it.

**Syntax**

Syntax is the set of rules that define how code must be written so Python can understand and run it. If the rules are broken, Python throws a SyntaxError. Think of it like grammar rules in English, but for code.

**Key Syntax Rules In Python**

No semicolons required. Python uses a newline to mark the end of a statement.

```python
x = 5
print(x)
```

Indentation is a syntax rule, not just style. Indentation defines code blocks in Python, and wrong indentation causes an IndentationError.

```python
if x > 0:
    print("Positive")
```

**Indentation In Detail**

Indentation is the spaces or tabs added at the beginning of a line, used to show which lines of code belong together as a group, called a code block. In most languages indentation is just for looks, but in Python it is mandatory and part of the actual syntax.

Rules of indentation:

The standard is 4 spaces, following the PEP8 recommendation.

```python
if x > 0:
    print("Positive")
```

All lines in the same block must be indented equally.

```python
if x > 0:
    print("Positive")
    print("Still inside the block")
print("Outside the block")
```

Mixing tabs and spaces causes errors, so always use spaces. Most editors convert the Tab key to 4 spaces automatically.

Nested blocks require extra indentation.

```python
if x > 0:
    print("Positive")
    if x > 10:
        print("Also greater than 10")
```

Wrong indentation causes an IndentationError.

```python
if x > 0:
print("Positive")
```

**Case Sensitivity**

```python
name = "Aarav"
Name = "Riya"
```

name and Name are two different variables. This applies to variables, function names, and keywords, everything.

**Reserved Keywords**

Reserved keywords cannot be used as variable names because they already have built in meaning in Python. Examples include if, else, for, while, def, return, class, True, False, None, import, in, not, and, or.

```python
if = 5
```

The above causes a SyntaxError.

**Comments Start With A Hash**

```python
# This is a comment
print("Hello")  # inline comment
```

Python ignores anything after the hash symbol on that line.

**One Statement Per Line**

This is best practice.

```python
x = 5
y = 10
```

Multiple statements on one line using a semicolon is possible but not recommended, since it violates PEP8.

```python
x = 5; y = 10
```

**Statement**

A statement is one single instruction or line of code that tells Python to do something. Any complete line of working code is one statement, just like a sentence in English is one complete thought.

```python
x = 5          # assignment statement
print(x)       # function call statement
if x > 0:      # conditional statement
    print("Positive")
for i in range(5):   # loop statement
    print(i)
```

**Code Style, PEP8**

PEP8 is Python's official style guide, a document that recommends how to write clean, readable, and consistent Python code. PEP stands for Python Enhancement Proposal, and PEP8 is proposal number 8, specifically about style. PEP8 is not enforced by Python itself, code still runs even if you ignore it, but professionally it is expected, and interviewers or reviewers do notice messy code.

**Key PEP8 Rules**

Indentation uses 4 spaces, not tabs.

Naming conventions: variables and functions use lowercase with underscores, for example total_price and calculate_discount. Classes use capitalized words, for example class Customer. Constants use all capitals with underscores, for example MAX_LIMIT equals 100.

Line length should be a maximum of 79 characters, to keep code readable without horizontal scrolling.

Spacing around operators should be consistent.

```python
x = 5 + 3
y = x * 2
```

Spacing after commas.

```python
print(1, 2, 3)
```

Blank lines separate logical sections, conventionally two blank lines between function definitions.

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

One statement per line, and meaningful variable names, for example customer_age instead of ca.

**Why PEP8 Matters**

Your code will be read by others, teammates and interviewers reviewing your GitHub projects, and messy code looks unprofessional even if it works. Since GitHub is being built as proof of work, PEP8 clean code directly improves how projects are perceived. Many companies check code style as part of interviews and code reviews.

**Variables**

A variable is a name given to a location in memory that stores a value, so you can use and change that value later in your code. Think of it like a labeled box, you put something inside and refer to it later using the label. Variables are containers for storing data values.

```python
age = 25
```

Here age is the variable name, and 25 is the value stored in it. Python has no command for declaring a variable, it is created the moment you first assign a value to it.

**Key Points About Variables**

No need to declare a type. Unlike Java or C, Python figures out the type automatically.

```python
age = 25
name = "Aarav"
```

Variables can change value, and even type. This is called dynamic typing, the type is decided at the time of assignment and can change.

```python
x = 5
x = "hello"
```

The assignment operator is a single equals sign, which means store the value on the right into the variable on the left, not mathematical equality.

Multiple assignment allows assigning different values in one line, or the same value to multiple variables.

```python
x, y, z = 1, 2, 3
a = b = c = 10
```

**Unpacking A Collection**

If you have a collection of values in a list or tuple, Python allows you to extract the values into variables, called unpacking.

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

**Naming Rules For Variables**

Must start with a letter or underscore, not a number. Can contain letters, numbers, and underscores. Cannot use Python keywords. Case sensitive.

```python
age = 25        # valid
_age = 25       # valid
age2 = 25       # valid
```

**Naming Convention, PEP8**

```python
total_price = 100
```

is recommended lowercase with underscores style. TotalPrice = 100 is not PEP8 style for variables, that style is for classes.

**Multi Word Variable Names**

When a variable name has more than one word, writing it as one unbroken word is hard to read, so programmers use different styles.

Camel case: first word lowercase, every other word starts with a capital letter, for example myVariableName. Common in JavaScript and Java.

Pascal case: every word starts with a capital letter including the first, for example MyVariableName. In Python this is used only for class names, not variables.

Snake case: all lowercase, words separated by underscores, for example my_variable_name. This is the Python standard for variables and functions, per PEP8.

So in Python, use snake_case for variables and functions, and PascalCase only for classes. camelCase is not used in standard Python style.

```python
x = "Python "
y = "is "
z = "awesome "
print(x, y, z)
```

Notice the space character after "Python " and "is ", without them the result would run together as one word.

**Global Keyword And Variable Scope**

Scope is the area of your code where a variable can be accessed or used. A local variable is created inside a function and only usable inside that function. A global variable is created outside any function and usable anywhere in the code.

```python
x = "awesome"

def myfunc():
    y = "hello"
    print(y)

myfunc()
print(x)   # works, x is global
```

Printing y outside the function would cause an error, since y is local and does not exist outside myfunc.

A common problem is that you cannot normally change a global variable from inside a function.

```python
x = "awesome"

def myfunc():
    x = "fantastic"

myfunc()
print(x)   # still prints "awesome", global x was untouched
```

This surprises beginners, since inside the function x is treated as a separate local variable by default.

The solution is the global keyword. If you want to modify the actual global variable from inside a function, you must tell Python explicitly.

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)   # Output: Python is fantastic
```

You can also create a global variable from inside a function using the same keyword.

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

**Data Types**

A data type tells Python what kind of value a variable holds, a number, text, true or false, a list of items, and so on. This matters because different types support different operations, you can do math on numbers but not directly on text the same way. Python is dynamically typed because variable types are determined automatically at runtime, and the same variable can reference objects of different types during program execution.

**Categories Of Data Types**

Text type: str, for example name = "Aarav".

Numeric types: int for whole numbers, float for decimal numbers, complex for numbers with a real and imaginary part, rarely used in data science but good to know it exists.

```python
age = 25
price = 99.99
complex_num = 3 + 4j
```

Sequence types: list is ordered and changeable, tuple is ordered and unchangeable. A sequence is a collection of items arranged in a specific order.

```python
fruits = ["apple", "banana", "mango"]
coordinates = (10, 20)
```

Mapping type: dict, key value pairs, called mapping because it maps one thing to another.

```python
person = {"name": "Aarav", "age": 25}
```

Set type: unordered, no duplicates.

```python
unique_ids = {1, 2, 3}
```

Boolean type: bool, only two values, True or False.

```python
is_active = True
```

None type: represents no value, empty, or nothing here yet.

```python
result = None
```

**Checking A Variable's Type**

The built in type function tells you the data type of any variable, useful when debugging.

```python
x = 25
print(type(x))   # <class 'int'>

y = "hello"
print(type(y))   # <class 'str'>
```

**Quick Table For Revision**

int, example 25, numeric.
float, example 99.99, numeric.
complex, example 3 plus 4j, numeric.
str, example "Aarav", text.
list, example [1, 2, 3], sequence.
tuple, example (1, 2, 3), sequence.
dict, example {"a": 1}, mapping.
set, example {1, 2, 3}, set.
bool, example True or False, boolean.
NoneType, example None, none.

**New Words Explained**

Data type: the category or kind of value a variable holds, which determines what operations are valid on it.

Ordered: the items keep a fixed position or sequence, first item stays first unless changed.

Unordered: items do not have a guaranteed fixed position.

Changeable, also called mutable: you can modify the contents after creation, for example lists.

Unchangeable, also called immutable: once created, contents cannot be modified, for example tuples and strings.

Key value pair: a way of storing data where each key points to a value, like a real dictionary, word maps to meaning.

Built in function: a function that comes ready made with Python, no need to create it yourself, for example print and type.

**Setting The Specific Data Type**

Normally Python automatically decides the data type based on the value assigned. Sometimes you want to force a variable to be a specific type instead of letting Python guess, done using constructor functions, built in functions named after each type.

A constructor function is a function that creates an object of a particular data type. Examples: int, float, str, list, tuple, set, dict, bool.

The outer parentheses are always used for the function call. Inner brackets belong to the data being passed, not to the constructor. list, tuple, and set convert an existing iterable into another data type. The constructor does not decide whether the inner brackets are round, square, or curly, the object you pass decides. dict is different because it can create a dictionary using keyword arguments with equals signs rather than colons, and can also create a dictionary from a collection of key value pairs.

Memory trick: outer parentheses are the function call, inner parentheses, square brackets, or curly braces are the data being passed.

**How To Set A Specific Data Type**

```python
x = str("Hello")
y = int(20)
z = float(20.5)
fruits = list(("apple", "banana"))
person = dict(name="Aarav", age=25)
```

**Constructor Function Versus Type Casting**

This looks similar to type casting, but there is a subtle difference. Type casting converts an existing variable from one type to another.

```python
age = "25"
age = int(age)
```

Setting a specific type means deciding the type at the moment of creation, usually to force a particular structure.

```python
fruits = list(("apple", "banana"))
```

In practice both use the same constructor functions, so this is really just type casting applied at creation time, not a separate mechanism.

**New Words Explained**

Constructor function: a built in function that constructs a value of a specific type, named exactly after the type.

Double parentheses: used when constructing a list, tuple, or set from a constructor function, because the outer parentheses belong to the function call and the inner parentheses hold the actual items.

**Python Numbers**

Python has three numeric types.

```python
x = 10        # int
y = 10.5      # float
z = 1 + 2j    # complex
```

**Int**

Whole numbers, positive or negative, no decimal point, and no limit on length, Python handles very large numbers automatically.

```python
x = 5
y = -300
z = 987654321987654321
print(type(x))   # <class 'int'>
```

**Float**

Numbers with a decimal point, positive or negative.

```python
x = 10.5
y = -3.14
z = 1e5
print(type(x))   # <class 'float'>
```

The letter e in scientific notation means times ten to the power of, common in scientific or large number notation, and appears often in datasets.

**Complex Numbers**

Numbers with a real and imaginary part, written with j for the imaginary part. Almost never used in Data Science or ML work, good to just recognize it exists.

```python
x = 3 + 4j
print(type(x))   # <class 'complex'>
```

**Type Conversion Between Numbers**

```python
x = 1       # int
y = 2.8     # float

x = float(x)   # 1.0
y = int(y)     # 2, decimal part dropped, not rounded

print(x)
print(y)
```

Important: converting float to int truncates the decimal, it does not round.

```python
print(int(9.9))   # 9, not 10
```

**Common Number Operations**

```python
print(10 + 3)    # 13, addition
print(10 - 3)    # 7, subtraction
print(10 * 3)    # 30, multiplication
print(10 / 3)    # 3.333..., division, always returns a float
print(10 // 3)   # 3, floor division, drops decimal
print(10 % 3)    # 1, modulus, remainder
print(10 ** 3)   # 1000, exponent, power
```

**Why This Matters For Data Science**

Almost all real world data, prices, quantities, ratings, scores, will be int or float. Knowing exactly how Python treats them, especially the int and float conversion truncation and division always returning a float, avoids silent bugs later in Pandas and NumPy calculations.

**New Words Explained**

Scientific notation: a compact way to write very large or very small numbers using e, common in datasets with very large or small values.

Truncate: to cut off the decimal part of a number without rounding.

Floor division: division that drops the decimal part, giving only the whole number result.

Modulus: gives the remainder left over after division, useful for checking things like whether a number is even or odd.

Exponent: raises a number to a power.

**Casting, Type Conversion**

Casting is manually converting one data type into another, using constructor functions such as int, float, and str.

**Why Casting Is Needed**

Python decides a variable's type automatically, but sometimes the type it picks is not the type you need for an operation. A classic example is that input always returns a string, even if the user types a number.

```python
age = input("Enter your age: ")
print(age + 1)   # TypeError
```

Fixed with casting:

```python
age = int(input("Enter your age: "))
print(age + 1)   # works
```

**The Three Main Casting Functions**

int converts to integer.

```python
x = int(1)         # 1
x = int(2.8)        # 2, truncated, not rounded
x = int("3")        # 3
```

Note that int cannot convert a decimal looking string directly.

float converts to float.

```python
x = float(1)         # 1.0
x = float("3.5")      # 3.5
x = float("3")        # 3.0
```

str converts to string.

```python
x = str(3)         # '3'
x = str(3.0)        # '3.0'
x = str(True)       # 'True'
```

**Common Casting Error To Watch For**

```python
int("3.5")   # ValueError
```

Correct way if needed:

```python
int(float("3.5"))   # first string to float, then float to int
```

**Why This Matters For Data Science**

Data from files such as CSV, user input, or web scraping often comes in as strings, even if it looks like a number. Casting columns or values to the correct type before doing math on them is one of the most common early bugs in real datasets, for example a price column read as text instead of numbers.

**New Words Explained**

Casting: manually converting a value from one data type to another.

TypeError: an error Python raises when an operation is done between incompatible types.

ValueError: an error Python raises when the value itself cannot be converted to the target type.

**Casting Versus Conversion**

In Python, casting and conversion mean the same thing, there is no strict technical difference, and Python's own documentation uses the word casting for this. Some other languages such as C and Java technically separate these two ideas, but Python does not.

If you want the deeper distinction from programming in general: type conversion, also called implicit conversion, happens automatically without writing any code, Python does it silently in the background.

```python
x = 5        # int
y = 2.0      # float
z = x + y    # Python automatically converts x to float before adding
print(z)     # 7.0
```

Type casting, also called explicit conversion, happens manually, you write the code yourself telling Python exactly what to convert.

```python
x = "25"
y = int(x)
```

**Input And Output**

Output is displaying information from your program to the screen, using print. Input is getting information from the user while the program is running, using input.

**Output With Print**

Basic use:

```python
print("Hello, World!")
```

Printing multiple items, comma separated:

```python
print("Name:", "Aarav", "Age:", 25)
```

By default Python puts a space between each item when using commas.

The sep argument changes the separator:

```python
print("Aarav", "Delhi", "India", sep=", ")
```

The end argument changes what is printed at the end, default is a newline:

```python
print("Loading", end="...")
print("Done")
```

Normally print moves to a new line after each call, end="" stops that.

f strings are the modern way to format output, and are used constantly.

```python
name = "Aarav"
age = 25
print(f"{name} is {age} years old")
```

Put f before the quotes, and anything inside curly braces is treated as actual code, not text.

```python
print(f"Next year, {name} will be {age + 1}")
print(f"{3.14159:.2f}")   # formatting a float to 2 decimal places
```

**Input With Input**

Basic use:

```python
name = input("Enter your name: ")
print("Hello", name)
```

Whatever the user types is stored in the variable, and the text inside input is just a prompt message shown to the user.

Critical rule, input always returns a string.

```python
age = input("Enter your age: ")
print(type(age))   # <class 'str'>, even if user typed 25
```

If you need a number, you must cast it.

```python
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

A common beginner bug:

```python
age = input("Enter your age: ")
print(age + 1)   # TypeError
```

Fix:

```python
age = int(input("Enter your age: "))
print(age + 1)
```

**New Words Explained**

Prompt: the message shown to the user asking them to type something.

Separator: the character placed between multiple items in print.

Newline: an invisible character that moves the cursor to the next line, what happens by default after every print.

F string: short for formatted string, a way to insert variables or expressions directly inside a string using curly braces, prefixed with f.

**Comments**

A comment is a line in your code that Python completely ignores when running the program. Comments are meant for humans reading the code, to explain why something is done, not what the code does, since the code already shows what.

**How To Write Comments In Python**

Single line comment, using the hash symbol. Everything after the hash on that line is ignored by Python.

```python
# This calculates the total price
total = price * quantity
```

Inline comment, placed at the end of a code line.

```python
x = 5   # default retry count
```

Multiple single line comments used as a block. Python has no true multi line comment symbol, so for longer explanations people stack multiple hash lines one after another.

```python
# This function calculates discount
# based on customer loyalty tier
# and current promotional offers
def calculate_discount():
    pass
```

Triple quoted strings used like a comment, technically not a real comment. This is often used like a comment block, but it is actually just an unassigned string.

```python
"""
This is often used like a comment block,
but it's actually just an unassigned string.
"""
```

Important distinction: this is not truly ignored the way hash comments are, it is a real string object that Python creates in memory and just does not do anything with, since it is not assigned to a variable. It is commonly used like a comment but technically it is not one. In an interview, say it is sometimes used like a comment block but it is really a string literal.

**Rules For Good Commenting**

Explain why, not what, since the code already shows what it does.

```python
x = 10   # bad: set x to 10, obvious and adds no value
x = 10   # good: default retry limit for API calls
```

Keep comments updated. An outdated comment that contradicts the code is worse than no comment at all, since it misleads whoever reads it later, including future you.

Do not over comment obvious code.

```python
x = x + 1   # unnecessary: increment x by 1, self explanatory
```

Use comments to explain tricky or non obvious logic.

```python
# Using floor division here to avoid decimal pricing errors
price_per_item = total // quantity
```

**New Words Explained**

Comment: a line ignored by Python, written for humans to read, explaining the reasoning behind the code.

String literal: a fixed piece of text written directly in the code, enclosed in quotes. Literal means it is the actual value written as is, not calculated or stored in a variable purposefully.

Unassigned: a value that exists but is not stored in any variable, so it just gets created and then discarded, Python does not error on this, it just does nothing useful with it.

**Quick Definition For Interviews**

A comment in Python is a line prefixed with a hash symbol, ignored by the interpreter and used to explain the reasoning behind code to other developers. Python does not have a dedicated multi line comment symbol, developers either use multiple hash lines or informally a triple quoted string, though the latter is technically a string literal, not a true comment.
