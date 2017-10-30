import json

from flask import Flask, render_template, request
import requests

API_ACCESS_TOKEN = "" # Replace this
API_BASE = 'https://api.intercom.io/'
YOUR_ADMIN_ID = "" # Replace this
HEADERS = {
      'Authorization': 'Bearer {}'.format(API_ACCESS_TOKEN),
      'Accept': 'application/json',
      'Content-Type' : 'application/json'
      }

app = Flask(__name__)


def send_reply(convo_id):
  url = API_BASE + "conversations/{}/reply".format(convo_id) 
  payload = {
  "type": "admin",
  "message_type": "comment",
  "admin_id": YOUR_ADMIN_ID,
  "body": "Thanks for the message! Someone wil be with you soon!"
  }
  r = requests.post(url, headers=HEADERS, json=payload)


@app.route('/handle_webhook', methods = ['POST'])
def handle_webhook():
    content = request.get_json()
    convo_id = content['data']['item']['id']
    send_reply(convo_id)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3333)  
    