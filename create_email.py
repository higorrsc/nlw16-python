import requests

payload = {
    "requestor": "Higor",
    "version": "1.0",
}

API_URL = "https://api.nodemailer.com/user"

response = requests.post(
    API_URL,
    json=payload,
    timeout=10,
)

if response.status_code == 200:
    account = response.json()
    print(account)
else:
    raise Exception(f"Could not create Ethereal account: {response.text}")
