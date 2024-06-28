# Define the list of special mentions
rachel_mentions = ['рейчел', 'котюха', 'рэчел', 'рэйч', 'рэя', 'рэйчэл', 'рейчэл', 'рейч', 'Rachel', 'Rach', 'рэля', 'реля']
da = ['да']


def check_exceptions(message_text):
    """
    Check if the message is exactly "да" or contains any special mentions.
    Returns the appropriate response if a match is found, else None.
    """
    # Normalize the message text to lowercase for comparison
    normalized_message = message_text.lower().strip()

    if normalized_message in rachel_mentions:
        return "Охуел? Не трожь Котюху 😾"
    elif normalized_message == 'да':
        return "Пизда!"
    return None
