import requests

url = "https://jsonplaceholder.typicode.com/users/2"
response = requests.get(url)

# Unpack the JSON into a dictionary
user = response.json()

# Print the whole thing first so you can see it
print("Full Data:", user)

# Now, extract specific pieces of data:
print("Name:", user["name"])
print("Email:", user["email"])
print("Company Name:", user["company"]["name"])