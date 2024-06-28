import os
from datetime import datetime


def log_message(username, message_text, bot_response):
    print(f"Logging: {username}, {message_text}, {bot_response}")
    message_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{message_time} - {username}: {message_text} -> Bot: {bot_response}\n"

    try:
        with open("user_messages.log", "a", encoding="utf-8") as file:
            file.write(log_entry)
    except Exception as e:
        print(f"Failed to write to log file: {e}")
