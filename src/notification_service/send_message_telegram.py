import requests
from datetime import datetime

from src.notification_service.config import BOT_TOKEN, CHAT_ID
from src.english_service.learn_vocabulary import vocabulary_for_today
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    #send html message
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    response = requests.post(url, json=payload)
    return response.json()

def notify_vocabulary():
    message = vocabulary_for_today().replace("```html", "").replace("```", "")
    send_message(CHAT_ID, message)

# if __name__ == "__main__":
#     notify_tasks_for_today()