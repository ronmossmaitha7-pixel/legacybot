# Legacy Fitness Club WhatsApp Bot

An automated WhatsApp customer service chatbot built with Python, Flask, and the Infobip WhatsApp API. Designed for **Legacy Fitness Club Mombasa**, the bot handles incoming member inquiries 24/7, providing instant information on membership pricing, branch locations, classes, and free trial bookings across three gym branches.

## Features

* **Interactive Menu Navigation:** Supports both numbered menu replies (`1`–`4`) and natural keyword detection (e.g., *"price"*, *"location"*, *"ladies"*, *"trial"*).
* **Multi-Branch Information:** Delivers tailored schedules, operating hours, and facility details for the Mwembe Tayari, Bamburi, and Bombolulu branches.
* **Membership & Pricing Breakdown:** Explains monthly auto-bill (GlobalPay/Visa) and daily walk-in pass options.
* **Lead Capture for Free Trials:** Prompts prospective members for their name and preferred branch to streamline front-desk bookings.
* **Webhook Integration:** Receives and processes real-time incoming messages from Infobip via a lightweight Flask POST endpoint.

## Tech Stack

* **Language:** Python 3
* **Web Framework:** Flask
* **API Integration:** Infobip WhatsApp Business API (`requests`)
* **Environment Management:** `python-dotenv`

## Project Structure

```text
├── app.py              # Main Flask application and webhook logic
├── .env                # Environment variables (not tracked in Git)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com
cd legacy-fitness-bot
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install flask requests python-dotenv
```

### 3. Configure environment variables
Create a `.env` file in the root directory and add your Infobip API key:
```env
INFOBIP_API_KEY=your_infobip_api_key_here
```

*(Optional: Update `INFOBIP_BASE_URL` and `INFOBIP_SENDER` in the script to match your Infobip account details.)*

### 4. Run the application
```bash
python bot.py
```
The server will start locally on `http://127.0.0.1:5000`.

## Webhook Configuration

To connect the local server to Infobip for live WhatsApp messages:
1. Expose your local port `5000` using a tunneling tool like **ngrok**:
   ```bash
   ngrok http 5000
   ```
2. Copy the generated HTTPS forwarding URL (e.g., `https://ngrok-free.app`).
3. Paste the URL into your Infobip WhatsApp number configuration as the incoming message webhook.
