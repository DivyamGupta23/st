from flask import Flask, request
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

# Replace this with your actual Slack webhook
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

@app.route('/')
def track_click():
    user = request.args.get('user', 'Unknown')
    ist = pytz.timezone('Asia/Kolkata')
    timestamp = datetime.now(ist).strftime('%Y-%m-%d %I:%M:%S %p IST')

    message = {
        "text": f"🔐 *Security Test Clicked!*\n👤 *User:* {user}\n🕒 *Time:* {timestamp}"
    }

    try:
        requests.post(SLACK_WEBHOOK_URL, json=message)
    except Exception as e:
        print("Slack failed:", e)

    return f"""
    <h2>You’ve failed this security test, {user}.</h2>
    <p>You were supposed to verify the URL before clicking this link.</p>
    <p>The person who posted this comment could have been compromised.</p>
    """



if __name__ == '__main__':
    app.run(debug=False, port=5000)
