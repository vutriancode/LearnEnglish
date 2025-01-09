# from src.notification_service.reply import *
from src.google_sheet.utils import get_vocabulary_for_today
if __name__ == "__main__":
    vocabulary = get_vocabulary_for_today()
    print(vocabulary.values.tolist())