# Advanced Python Features for Analysts: Beyond `purrr`

## 1. Functional Programming: The `purrr` Transition
In R, you use `map`, `map_df`, and `walk` to avoid `for` loops. In Python, while `map()` exists, the preferred way is **List Comprehensions**.

### List Comprehensions
List comprehensions are faster and more readable than loops.

**R Version (purrr):**
```r
squares <- map_dbl(1:10, ~ .x^2)
```

**Python Version:**
```python
squares = [x**2 for x in range(1, 11)]
```

### With Conditional Logic
**R Version:**
```r
evens <- keep(1:10, ~ .x %% 2 == 0)
```

**Python Version:**
```python
evens = [x for x in range(1, 11) if x % 2 == 0]
```

---

## 2. Iterating over Dictionaries
Since Dictionaries are Key-Value pairs, iterating over them is very common.

```python
results = {"Model A": 0.85, "Model B": 0.92, "Model C": 0.78}

# Get only the keys (Model names)
for model in results:
    print(model)

# Get both key and value
for model, score in results.items():
    print(f"{model} achieved a score of {score}")
```

---

## 3. Decorators: The "Wrapper" Pattern
Decorators are a powerful way to add behavior to existing functions without modifying them. Think of them as "Middlewares" for your functions.

```python
import time

def timer_decorator(func):
    """Prints the execution time of the function it wraps."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def complex_analysis():
    time.sleep(1.5) # Simulate long task
    return "Analysis Complete"

print(complex_analysis())
```

---

## 4. Error Handling: `try` / `except`
In R, you might use `tryCatch()`. Python's version is much more widely used and idiomatic.

```python
# R: tryCatch({ 10 / 0 }, error = function(e) print("Error!"))

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("This block always runs (e.g., to close a database connection).")
```

---

## 🏆 Challenge Exercise: The Performance Tracker
1.  **Create a decorator** called `logger` that prints "Starting function..." before a function runs and "Finished function..." after.
2.  **Use a list comprehension** to generate a list of all numbers between 1 and 1000 that are divisible by both 3 and 5.
3.  **Combine them:** Apply your `@logger` decorator to a function that performs this list comprehension.
4.  **Comparison:** How would you implement a "logger" in R? (Likely using a wrapper function that calls `on.exit()`).

---
[⬅️ Previous](../07_ml_deep_learning/03_pytorch_neural_networks.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_databases.md)
