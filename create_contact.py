import requests

BASE = "https://masar-class-api.a-f-almatrafi.workers.dev/api"
me = "Mohammed"

r = requests.post(f"{BASE}/students", json={"username": me}, timeout=10)
print("register:", r.status_code) # 201 أول مرة — و409 إن كنت مسجّلاً، وكلاهما حسن

r = requests.post(
    f"{BASE}/students/{me}/contacts",
    json={"name": "Salem", "phone": "0501234567"},
    timeout=10,
)
print("create:", r.status_code)
if r.status_code == 201:
    print("new contact id:", r.json()["id"])
