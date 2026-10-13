from datetime import datetime

def send_notification(user, message):
    print(f"[{datetime.now():%Y-%m-%d %H:%M}]")
    print(f"To: {user}")
    print(message)

send_notification("Ali", "Your task is completed!")
