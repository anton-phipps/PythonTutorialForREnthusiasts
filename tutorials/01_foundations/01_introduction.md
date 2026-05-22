# Lesson 01: Python Language Overview for R Users

## 1. The Mental Shift: Vectors vs. Objects
In R, almost everything is a vector. If you add `1 + 1`, R treats it as two vectors of length 1 being added. In Python, types are more distinct.

### Basic Types Comparison
| Feature | R | Python | Why it matters |
| --- | --- | --- | --- |
| **Numeric** | `numeric`, `integer` | `int`, `float` | Python distinguishes between whole numbers and decimals more strictly. |
| **Text** | `character` | `str` | Python strings are "objects" with many built-in methods (e.g., `"hello".upper()`). |
| **Logic** | `TRUE`, `FALSE` | `True`, `False` | Note the capitalization! `TRUE` will throw an error in Python. |
| **Missing** | `NA`, `NULL` | `None`, `np.nan` | `None` is for "nothing," `np.nan` (from NumPy) is for "Not a Number" in data. |

### Pro-Tip: Missing Values
In R, `NA` is a logical value that can exist in any vector. In Python:
*   `None` is the generic "null" (like `NULL` in R).
*   `np.nan` is used specifically for missing numbers in DataFrames (like `NA_real_`).
*   **Gotcha:** `np.nan == np.nan` is **False**! Use `pd.isna()` or `np.isnan()`.

## 2. Collections: Lists and Dictionaries
R users are used to `list()` and `c()`. Python has four main collection types, but you'll use **Lists** and **Dictionaries** the most.

### Lists (The "Unordered" Collection)
Think of a Python list as an R list that doesn't have names.
```python
# R: my_list <- list(1, "apple", TRUE)
my_list = [1, "apple", True]

# Accessing (Note: Python starts at 0!)
# R: my_list[[1]] 
print(my_list[0]) # Returns 1
```

### Dictionaries (The "Named List" Equivalent)
Dictionaries are Key-Value pairs. This is exactly like a named list in R.
```python
# R: my_dict <- list(name = "Alice", age = 30)
my_dict = {"name": "Alice", "age": 30}

# Accessing
# R: my_dict$name
print(my_dict["name"]) # Returns "Alice"
```

### Iteration: List Comprehensions (The `lapply` Equivalent)
R users love `lapply` and `purrr::map`. In Python, we use **List Comprehensions**.

```python
# R: lapply(1:5, function(x) x^2)
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# With a condition (like filter + map)
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
```

## 3. Operations and Indentation
Python handles math and strings through a mix of operators and object methods.

### Math Operations
| Operation | R | Python |
| --- | --- | --- |
| Division | `10 / 3` | `10 / 3` (3.33) |
| Floor Division | `10 %/% 3` | `10 // 3` (3) |
| Modulo | `10 %% 3` | `10 % 3` (1) |
| Power | `10 ^ 2` or `10 ** 2` | `10 ** 2` (100) |

### String Manipulation
Strings in Python are objects, meaning they have built-in "methods."
```python
text = "  Research Analysis  "

# R: trimws(text)
print(text.strip()) # "Research Analysis"

# R: toupper(text)
print(text.upper()) # "  RESEARCH ANALYSIS  "

# R: paste("A", "B", "C", sep = "-")
print("-".join(["A", "B", "C"])) # "A-B-C"

# Modern Formatting (F-Strings) - Preferred over paste()
name = "Alice"
print(f"Project Lead: {name}") 
```

### Indentation and Control Flow
Python does not use curly braces `{}` to define code blocks for loops or functions. It uses **Indentation** (usually 4 spaces).

## 4. Functions: Defining Logic
Functions in Python are very similar to R, but the syntax is cleaner.

**R Version:**
```r
calculate_total <- function(price, tax = 0.05) {
  return(price * (1 + tax))
}
```

**Python Version:**
```python
def calculate_total(price, tax=0.05):
    """Calculates the total price including tax."""
    return price * (1 + tax)
```

## 5. Classes and Objects
R has several OOP systems (S3, S4, R6). Python has one unified system. Everything you interact with (a DataFrame, a Plot, a String) is an "Object" belonging to a "Class."

```python
class ResearchProject:
    def __init__(self, title):
        self.title = title
        self.status = "Started"

    def update_status(self, new_status):
        self.status = new_status

# In R, you'd likely use a list or a specialized R6 object
project = ResearchProject("Climate Study")
project.update_status("Data Collected")
print(f"Project '{project.title}' is currently: {project.status}")
```

---

## 🏆 Challenge Exercise: The Analyst's Calculator
1.  **Task:** Create a function `get_stats` that takes a list of numbers.
2.  **Requirement:** Return a dictionary with three keys: `sum`, `count`, and `average`.
3.  **Comparison:** How would you do this in R using `list(sum = sum(x), ...)`?

**Example Input:** `[10, 20, 30, 40]`
**Expected Output:** `{'sum': 100, 'count': 4, 'average': 25.0}`

---
[⬅️ Previous](00_environment.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_jupyter.md)
