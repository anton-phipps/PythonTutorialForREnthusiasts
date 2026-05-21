# Lesson 01: Python Language Overview

## 1. Operations & Basic Types
In R, you have vectors. In Python, you have several core types:
*   **Integers/Floats:** Numbers.
*   **Strings:** Text (single or double quotes).
*   **Lists:** `[1, 2, 3]` (Mutable, like a basic R list).
*   **Tuples:** `(1, 2, 3)` (Immutable).
*   **Dictionaries:** `{"key": "value"}` (Like a named list in R).

### Basic Operations
```python
# Math
x = 10 + 5   # 15
y = 10 / 3   # 3.333 (Float division)
z = 10 // 3  # 3 (Floor division)
w = 10 ** 2  # 100 (Exponentiation)

# Strings
greeting = "Hello" + " " + "World"  # Concatenation
name = "Analyst"
formatted = f"Welcome, {name}!"    # F-Strings (Modern & Recommended)
```

## 2. Assignments & Scoping
Python uses `=` for assignment. Unlike R's `<-`, there is no "alternative" operator.
*   **Indentation matters:** Python uses whitespace instead of curly braces `{}` to define blocks of code (loops, functions).

```python
x = 10
if x > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5")
```

## 3. Functions
Functions are defined using the `def` keyword.

```python
def calculate_growth(initial, rate, years=5):
    """
    Calculates compound growth.
    This is a docstring, similar to R's roxygen comments.
    """
    final_value = initial * (1 + rate) ** years
    return final_value

# Calling the function
result = calculate_growth(100, 0.05)
print(f"Final Value: {result:.2f}")
```

## 4. Classes (Object-Oriented Programming)
While R has S3, S4, and R6, Python is "Object-Oriented" by default. Everything is an object.

```python
class ResearchProject:
    def __init__(self, name, analyst):
        self.name = name
        self.analyst = analyst
        self.status = "In Progress"

    def complete(self):
        self.status = "Finished"
        print(f"Project '{self.name}' is now complete.")

# Creating an instance
my_project = ResearchProject("Market Analysis", "Alice")
print(my_project.status)
my_project.complete()
```

---

## 🏆 Challenge Exercise: The Analyst's Calculator
1.  Create a function called `analyze_vector` that takes a list of numbers.
2.  The function should return a dictionary containing the `sum`, `mean`, and `max` of the list.
3.  **Bonus:** Create a Class called `DataSeries` that stores the list as an attribute and has methods to return the summary dictionary you just created.

**Target Output:**
```python
series = DataSeries([10, 20, 30])
print(series.get_summary()) 
# Should output: {'sum': 60, 'mean': 20.0, 'max': 30}
```

---
[🏠 Table of Contents](../../README.md) | [Next ➡️](02_jupyter.md)
