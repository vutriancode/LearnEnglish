import pandas as pd
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

from src.google_sheet.config import *



# Kết nối đến Google Sheets
def connect():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    # 2) Khởi tạo service cho Google Sheets
    googles_sheets_service = build('sheets', 'v4', credentials=credentials)
    drive_service = build('drive', 'v3', credentials=credentials)
    return googles_sheets_service, drive_service

#get vocabulary for today
def get_vocabulary_for_today():
    service, drive_service = connect()
    range_ = 'vocabulary'
    result = service.spreadsheets().values().get(
        spreadsheetId=WORD_SPREADSHEET_ID, range=range_).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
        return None
    else:
        # Giả sử hàng đầu là header
        header = values[0]
        print(header)
        rows = values[1:]
        print(rows)
        df = pd.DataFrame(rows, columns=header)
        return df
if __name__ == "__main__":
    vocabulary = get_vocabulary_for_today()
    print(vocabulary)