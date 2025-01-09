from src.notification_service.send_message_telegram import notify_vocabulary
import schedule
import time
from datetime import datetime, timedelta

def job():
    print("Đã bắt đầu chạy tác vụ")

    # Kiểm tra thời gian hiện tại để đảm bảo chỉ chạy từ 06:00 đến 23:00
    current_time = datetime.utcnow() + timedelta(hours=7) # UTC+7
    current_time = current_time.time()
    if current_time >= datetime.strptime("06:00", "%H:%M").time() and current_time <= datetime.strptime("23:00", "%H:%M").time():
        notify_vocabulary()

# Lên lịch chạy mỗi 5 phút
schedule.every(10).minutes.do(job)

def main():
    print("Đã bắt đầu chạy tác vụ theo lịch trình.")
    while True:
        schedule.run_pending()  # Kiểm tra các công việc cần chạy
        time.sleep(1)  # Kiểm tra mỗi giây

if __name__ == "__main__":
    main()
