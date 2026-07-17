Python Notes

Setting up somewhere to write code

Python code needs something to run it. Your computer does not understand Python directly, so you need a program that reads your code and executes it and shows you the result. These tools are of two types.

1. Notebooks - best for learning and data science
A notebook is a document where you write small chunks of code called cells, run them one at a time, and see results right below that cell, mixed with your own notes. Data scientists like this because you can explore data step by step and explain your thinking alongside the code. Common tools are Google Colab and Jupyter Notebook.

2. Code editors and IDEs - best for building real software
This is a text editor made for writing full programs, running the whole file at once. Common tools are VS Code and PyCharm.

Definitions

Programming language - a way to give instructions to a computer, written in a form humans can understand and write, which then gets converted into machine code the computer can execute.

High-level language - a programming language that is close to human language, easy to read and write, and hides the complex hardware details from the programmer. Example: Python.

Low-level language - closer to machine code, harder for humans to read, but very fast and closer to hardware. Example: C, Assembly.

Interpreted language - one where the code is read and executed line by line by an interpreter at runtime, instead of being converted into machine code all at once beforehand. Python is an interpreted language.

Compiled language - one where the entire code is translated into machine code beforehand using a compiler, before it is run. Example: C, C++.

Python - a high-level, interpreted, general-purpose programming language, known for its simple and readable syntax. It is widely used in Data Science, AI, web development, and automation.

Why is Python used in Data Science despite being slow

Python is a high-level, interpreted language, easy to read and write, but slower than low-level languages like C. For Data Science this speed issue does not matter in practice because libraries like NumPy and Pandas are written in Python on the outside, but their internal heavy calculations are done using C and sometimes Fortran, which are much faster. So Python gives a simple interface while C and Fortran act as the fast engine underneath. Result: you write easy readable Python code but get near C speed for calculations.

Why Python specifically for Data Science

Easy readable syntax, closer to plain English than most languages, so you can focus on logic instead of fighting the language.

Huge ecosystem of libraries built for data work: NumPy for numeric arrays, Pandas for tabular data, Matplotlib and Seaborn for visualization, Scikit-learn for classic ML, TensorFlow and PyTorch for deep learning.

Industry standard, almost every Data Science and ML job expects Python, so skills transfer directly to real jobs.

Same language for the whole pipeline, you can clean data, analyze it, build a model, and even deploy it, all in Python.

Comments

Definition

A comment is a line in your code that Python completely ignores when running the program. Comments are meant for humans reading the code, to explain why something is done, not what the code does, since the code already shows what.

How to write comments in Python

1. Single line comment, use hash symbol
Example: hash This calculates the total price, then total = price times quantity. Everything after the hash on that line is ignored by Python.

2. Inline comment, comment placed at the end of a code line
Example: x = 5 hash default retry count

3. Multiple single line comments used as a block
Python has no true multi line comment symbol, so for longer explanations people just stack multiple hash lines one after another.

4. Triple quoted strings used like a comment, technically not a real comment
This is often used like a comment block, but it is actually just an unassigned string. Important distinction: this is not truly ignored the way hash comments are, it is a real string object that Python creates in memory and just does not do anything with, since it is not assigned to a variable. It is commonly used like a comment but technically it is not one. In an interview say it is sometimes used like a comment block but it is really a string literal.

Rules for good commenting

1. Explain why, not what, since the code already shows what it does. Bad example: x = 10 hash set x to 10, this is obvious and adds no value. Good example: x = 10 hash default retry limit for API calls.

2. Keep comments updated. An outdated comment that contradicts the code is worse than no comment at all, since it misleads whoever reads it later, including future you.

3. Do not over comment obvious code. Example: x = x + 1 hash increment x by 1, this is unnecessary since the code is self explanatory.

4. Use comments to explain tricky or non obvious logic. Example: hash using floor division here to avoid decimal pricing errors, then price_per_item = total divided by quantity using floor division.

New words explained

Comment - a line ignored by Python, written for humans to read, explaining the reasoning behind the code.

String literal - a fixed piece of text written directly in the code, enclosed in quotes. Literal means it is the actual value written as is, not calculated or stored in a variable purposefully.

Unassigned - a value that exists but is not stored in any variable, so it just gets created and then discarded, Python does not error on this, it just does nothing useful with it.

Quick definition for interviews

A comment in Python is a line prefixed with a hash symbol, ignored by the interpreter and used to explain the reasoning behind code to other developers. Python does not have a dedicated multi line comment symbol, developers either use multiple hash lines or informally a triple quoted string, though the latter is technically a string literal, not a true comment.
