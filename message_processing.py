from exceptions import check_exceptions


def get_processed_message(message_text):
    bot_response = check_exceptions(message_text)
    if bot_response is None:
        if len(message_text) >= 2 and message_text[1] == 'ы':
            replacement = 'хуи'
            modified_text = replacement + message_text[2:]
            return modified_text
        elif len(message_text) >= 3 and message_text[3] == 'о':
            replacement = 'хуе'
            modified_text = replacement + message_text[4:]
            return modified_text
        elif len(message_text.split()) == 1 and len(message_text) >= 3:
            third_char = message_text[2]  # Already lowercase due to earlier conversion
            if third_char in 'а':
                replacement = 'хуя'
            elif third_char in 'у':
                replacement = 'хую'
            elif third_char in 'о':
                replacement = 'хуё'
            elif third_char in 'е':
                replacement = 'хуе'
            else:
                replacement = 'хуе'
            modified_text = replacement + message_text[3:]
            return modified_text
        else:
            return "Я не могу это хуефицировать! Дай одно слово, пёс 🦮"
    return bot_response
