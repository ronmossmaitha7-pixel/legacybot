import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://2yedyz.api.infobip.com/whatsapp/1/message/text"
headers = {
    "Authorization": f"App {os.environ['INFOBIP_API_KEY']}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "from": "447860088970",
    "to": "254701185904",
    "content": {
        "text": "LegacyBot is officially online!"
    }
}

response = requests.post(url, json=payload, headers=headers)
print("Status:", response.status_code)
print("Response:", response.text)
