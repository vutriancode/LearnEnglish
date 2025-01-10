import google.generativeai as genai
import random
from src.english_service.config import *
# from src.notification_service.reply import *
from src.google_sheet.utils import get_topics_for_today
def grammar_for_today():
    topics = get_topics_for_today()
    topic = random.choice(topics.values.tolist())[0]
    print("topic", topic)
    genai.configure(api_key="AIzaSyCqHprbJMRlaLGGYFSFJ7au04mbpDq2KSA")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(GRAMMAR_PROMPT.format(topic))
    return response.text