import requests

# A fake URL that will definitely fail (404 Not Found)
url = "https://jsonplaceholder.typicode.com/invalid-page"

response = requests.get(url)

print("Status Code:", response.status_code)

# Check if the request was successful (200)
if response.status_code == 200:
    # If success, unpack the JSON
    data = response.json()
    print("Success! Data:", data)
else:
    # If it failed, print an honest error message
    print("Something went wrong.")
    print("Error Code:", response.status_code)
    print("We cannot process the data right now.")