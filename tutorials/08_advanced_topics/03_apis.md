# Interacting with APIs

## Overview
In R, you use `httr` or `httr2`. In Python, the gold standard is the **Requests** library.

## 1. Making a GET Request
The most common way to get data from a web service.

```python
import requests

# Example: Getting data from a public API (GitHub)
response = requests.get('https://api.github.com/repos/psf/requests')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON directly into a Python dictionary
    print(f"Repository Name: {data['name']}")
    print(f"Stars: {data['stargazers_count']}")
else:
    print(f"Error: {response.status_code}")
```

## 2. Passing Parameters
Just like `query = list(...)` in `httr`.

```python
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)
```

## 3. Authentication
Many APIs require a key or token.

```python
headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE'}
response = requests.get('https://api.example.com/protected', headers=headers)
```

## 4. Turning API Data into a DataFrame
Since `response.json()` returns a list of dictionaries, Pandas can handle it immediately.

```python
import pandas as pd

json_data = response.json()
df = pd.DataFrame(json_data)
print(df.head())
```

---

## 🏆 Challenge Exercise: The Weather Reporter
1.  Find a free public API (like `Open-Meteo` which doesn't require a key).
2.  Write a script to get the current temperature for your city (or any coordinates).
3.  Parse the JSON response and print a friendly message: "The current temperature in [City] is [Temp]°C."
4.  **Bonus:** Try to get the forecast for the next 7 days and load it into a Pandas DataFrame.

---
[⬅️ Previous](02_databases.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](04_local_ui.md)
