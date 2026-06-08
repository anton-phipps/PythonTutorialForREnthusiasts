# Block 1
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

# Block 2
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)

# Block 3
# Use httpbin.org for a working authentication example
headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE'}
response = requests.get('https://httpbin.org/bearer', headers=headers)
print(f"Status: {response.status_code}")

# Block 4
import pandas as pd

# If data is a single dictionary, wrap it in a list
json_data = response.json()
df = pd.DataFrame([json_data])
print(df.head())

