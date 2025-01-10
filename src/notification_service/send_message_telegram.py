import requests
from datetime import datetime
from src.notification_service.config import BOT_TOKEN, CHAT_ID,GRAMMAR_CHAT_ID
from src.english_service.learn_vocabulary import vocabulary_for_today
from src.english_service.learn_grammar import grammar_for_today
def escape_markdown_v2(text: str) -> str:
    """
    Escapes special characters for Telegram Markdown V2.
    
    :param text: The input string to be escaped.
    :return: Escaped string suitable for Markdown V2 formatting.
    """
    special_chars = r"*"
    for char in special_chars:
        text = text.replace(char, f"")
    return text

def send_message(chat_id, text,type_ ='HTML'):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    #send html message
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': type_}
    response = requests.post(url, json=payload)
    return response.json()

def notify_vocabulary():
    message = vocabulary_for_today().replace("```html", "").replace("```", "")
    send_message(CHAT_ID, message)

def notify_grammar():
    message = grammar_for_today().replace("```html", "").replace("```", "")
    message = escape_markdown_v2(message)
    send_message(GRAMMAR_CHAT_ID, message,type_ ='HTML')
# if __name__ == "__main__":
#     notify_tasks_for_today()