# Advanced Python Features for Analysts

## 1. Functional Programming: Moving beyond `purrr`
Python offers powerful ways to iterate without explicit `for` loops, similar to the `map` family in R.

### List Comprehensions
The most concise and readable way to transform data.
```python
# R: map(1:10, ~ .x^2)
squares = [x**2 for x in range(1, 11)]

# Conditional logic inside
evens = [x for x in range(1, 11) if x % 2 == 0]
```

### Lambda Functions
Anonymous, one-line functions. Useful for quick operations.
```python
# R: map(data, function(x) x + 1)
data = [1, 2, 3]
plus_one = list(map(lambda x: x + 1, data))
```

## 2. Decorators: Enhancing Functions
Decorators allow you to "wrap" a function with extra functionality. This is common in performance tuning and web development.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_computation():
    time.sleep(1)
    return "Done"

slow_computation()
```

## 3. High Performance: Numba
If you have a heavy numerical calculation, the `@jit` (Just-In-Time) decorator from **Numba** can make it run at the speed of C.

```python
from numba import jit

@jit(nopython=True)
def sum_array(arr):
    s = 0
    for x in arr:
        s += x
    return s
```

---

## 🏆 Challenge Exercise: The Performance Optimizer
1.  Create a list of 1 million random numbers.
2.  Write a standard Python function to calculate the square root of each number.
3.  Write a **List Comprehension** to do the same.
4.  Write a function using **NumPy** (`np.sqrt`) to do the same.
5.  Use the `@timer` decorator (from the example above) to compare the performance of all three methods.
6.  **Bonus:** Try to use **Numba**'s `@jit` on a custom loop and see if it can beat NumPy.

---
[⬅️ Previous](../07_ml_deep_learning/02_pytorch_neural_networks.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_databases.md)
