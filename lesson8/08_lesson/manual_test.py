import requests

BASE_URL = "https://ru.yougile.com"
TOKEN = "XBwbTnfNXJJG45S+TxkAn7j+d8UxdzeB-n+3TzixbEUKQYbQXBl-FK7gPZpopIRX"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Попробуем создать проект
payload = {"name": "TestProject"}
response = requests.post(f"{BASE_URL}/api-v2/projects", json=payload, headers=headers)
print("Create Project:", response.status_code)
print(response.text)