import requests

url = "https://masar-class-api.a-f-almatrafi.workers.dev/api/posts"
while url:
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        break
    data = resp.json()
    for post in data["data"]:
        print(post["id"], post["title"])
    url = data["next"]
