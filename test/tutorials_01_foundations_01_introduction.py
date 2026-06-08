# Block 1
# R: my_list <- list(1, "apple", TRUE)
my_list = [1, "apple", True]

# Accessing (Note: Python starts at 0!)
# R: my_list[[1]] 
print(my_list[0]) # Returns 1

# Block 2
# R: my_dict <- list(name = "Alice", age = 30)
my_dict = {"name": "Alice", "age": 30}

# Accessing
# R: my_dict$name
print(my_dict["name"]) # Returns "Alice"

# Block 3
# R: lapply(1:5, function(x) x^2)
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# With a condition (like filter + map)
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# Block 4
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

# Block 5
def calculate_total(price, tax=0.05):
    """Calculates the total price including tax."""
    return price * (1 + tax)

# Block 6
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

