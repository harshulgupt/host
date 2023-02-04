import os
import requests

# retrieve token from environment variable
token = os.getenv("PAT")

# fetch data from private repository using GitHub API
url = "https://api.github.com/repos/<user>/json_pvt/data.txt"
headers = {
    "Authorization": "Token " + token
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()["content"]
else:
    raise Exception("Could not fetch data from private repository")

# write data to output.txt file
with open("output.txt", "w") as f:
    f.write(data)
