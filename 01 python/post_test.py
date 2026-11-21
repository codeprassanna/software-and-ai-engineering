import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First API Request",
    "body": "I am learning software engineering.",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())