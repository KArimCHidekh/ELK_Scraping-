import json
import requests

# Create a requests.Request object
request = requests.Request(
    method="GET",
    url="http://localhost:8000//sentiment_analysis/",
    json={"text": "This is my post content."},
)

# Send the request
response = requests.Session().send(request)

# Check the response status code
if response.status_code == 201:
    # The post was created successfully
    print("Post created successfully.")
else:
    # An error occurred
    print(response.status_code, response.content)