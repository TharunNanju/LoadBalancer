import requests
import time
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# === Twilio Setup ===
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
your_whatsapp_number = os.getenv('YOUR_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)

# === Your Backends ===
# Use IPs or Tailscale IPs based on your setup
backends = {
    "Backend 1": "http://localhost:5001/health",
    "Backend 2": "http://localhost:5002/health",
    "Backend 3": "http://localhost:5003/health",
    "Backend 4": "http://100.119.221.6:5005/health",
    "Backend 4": "http://100.119.221.6:5001/health",
    "Backend 5": "http://100.119.221.6:5002/health",
    "Backend 6": "http://100.119.221.6:5003/health",
    "Backend 7": "http://100.119.221.6:5004/health",
}

# === Track downed backends ===
down = set()

while True:
    for name, url in backends.items():
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                if name in down:
                    print(f"[RECOVERY] {name} is back ONLINE.")
                    down.remove(name)

                    # Notify recovery
                    client.messages.create(
                        from_=twilio_whatsapp_number,
                        body=f"✅ {name} is back ONLINE!",
                        to=your_whatsapp_number
                    )
            else:
                raise Exception("Non-200 status code")
        except:
            if name not in down:
                down.add(name)
                print(f"[ALERT] {name} is DOWN!")

                # Send WhatsApp alert
                client.messages.create(
                    from_=twilio_whatsapp_number,
                    body=f"🚨 {name} is DOWN!\nCheck: {url}",
                    to=your_whatsapp_number
                )
    time.sleep(10)  # Wait 10 seconds before checking again

