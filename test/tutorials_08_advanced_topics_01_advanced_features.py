# Block 1
def calculate_growth(initial: float, final: float) -> float:
    """
    Calculates the percentage growth between two values.
    
    Args:
        initial: The starting value.
        final: The ending value.
        
    Returns:
        The percentage growth as a decimal.
    """
    return (final - initial) / initial

# Block 2
squares = [x**2 for x in range(1, 11)]

# Block 3
evens = [x for x in range(1, 11) if x % 2 == 0]

# Block 4
results = {"Model A": 0.85, "Model B": 0.92, "Model C": 0.78}

# Get only the keys (Model names)
for model in results:
    print(model)

# Get both key and value
for model, score in results.items():
    print(f"{model} achieved a score of {score}")

# Block 5
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

# Block 6
# R: tryCatch({ 10 / 0 }, error = function(e) print("Error!"))

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("This block always runs (e.g., to close a database connection).")

