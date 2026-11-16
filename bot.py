import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

app = Flask(__name__)

INFOBIP_API_KEY = os.environ["INFOBIP_API_KEY"]
INFOBIP_BASE_URL = "https://2yedyz.api.infobip.com"
INFOBIP_SENDER = "447860088970"


def send_whatsapp_message(to_number, message_text):
    url = f"{INFOBIP_BASE_URL}/whatsapp/1/message/text"
    headers = {
        "Authorization": f"App {INFOBIP_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "from": INFOBIP_SENDER,
        "to": to_number,
        "content": {"text": message_text},
    }
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()
def get_legacy_reply(user_msg):
    msg = (user_msg or "").strip().lower().replace("ronmossmaitha7", "").strip()



def get_legacy_reply(user_msg):
    msg = (user_msg or "").strip().lower()

    if msg in {"hi", "hello", "hey", "menu", "start"}:
        return (
            "Karibu to *Legacy Fitness Club Mombasa*! 💪\n"
            "How can we help you today? Reply with a number:\n\n"
            "1️⃣ Membership Prices & GlobalPay\n"
            "2️⃣ Branch Locations & Hours\n"
            "3️⃣ Ladies-Only & Group Classes\n"
            "4️⃣ Book a Free Trial Session"
        )
    elif msg == "1" or any(keyword in msg for keyword in ["price", "cost", "globalpay"]):
        return (
            "*Membership Plans (All 3 Branches Access)* 💳\n\n"
            "• *Monthly Auto-Bill:* KSh 2,500/month (via M-Pesa GlobalPay or Visa)\n"
            "• *Walk-in / Daily Pass:* KSh 500\n\n"
            "One membership gives you full access to Mwembe Tayari, Bamburi, and Bombolulu!\n"
            "Reply *4* to book a free visit or *Menu* to go back."
        )
    elif msg == "2" or any(keyword in msg for keyword in ["location", "branch", "hours"]):
        return (
            "*Our 3 Mombasa Branches* 📍\n\n"
            "🏢 *Mwembe Tayari:* Mombasa Mall (Naivas), 3rd Floor (24 Hrs Mon–Fri)\n"
            "🏢 *Bamburi:* Bamburi Mwisho, Petrocity (Open 24 Hours)\n"
            "🏢 *Bombolulu:* Bombolulu Petrocity / Naivas, next to VOK\n\n"
            "Reply *Menu* for main options."
        )
    elif msg == "3" or any(keyword in msg for keyword in ["ladies", "class"]):
        return (
            "*Classes & Special Sections* 🏋️‍♀️\n\n"
            "• *Mwembe Tayari:* Dedicated Ladies-Only gym section + Juice Bar\n"
            "• *Bamburi:* Group Aerobics, Katabox & Martial Arts\n"
            "• *Bombolulu:* Strength, Cardio & Personal Training\n\n"
            "Reply *4* to book a free trial class!"
        )
    elif msg == "4" or any(keyword in msg for keyword in ["trial", "book"]):
        return (
            "*Book Your Free Trial!* 🎉\n\n"
            "Please reply with your *Full Name* and which branch you want to visit (*Mwembe Tayari*, *Bamburi*, or *Bombolulu*), and our front desk will reserve your spot!"
        )
    else:
        return (
            "Thanks for messaging *Legacy Fitness Club*! 🙌\n"
            "If you just sent your booking details, our team has noted them.\n\n"
            "Reply *Menu* at any time to see prices, branches, and classes."
        )


@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json(silent=True) or {}

    try:
        for result in data.get("results", []):
            sender_number = result.get("from")
            message = result.get("message", {})
            if message.get("type") != "TEXT":
                continue

            text_body = message.get("text")
            if not sender_number or not text_body:
                continue

            reply = get_legacy_reply(text_body)
            send_whatsapp_message(sender_number, reply)
    except Exception as exc:
        print("Error processing message:", exc)

    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)

