import requests

url = "https://masar-class-api.a-f-almatrafi.workers.dev/api/posts"
resp = requests.get(url, params={"page": 1, "limit": 5}, timeout=10)
print(resp.status_code)
if resp.status_code == 200:
    for post in resp.json()["data"]:
        print(post["title"])
