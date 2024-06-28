from dotenv import load_dotenv
import os
from api_client import get_insult
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from log_helper import log_message
from config import bot_info_message
from button_handlers import button_command
from message_processing import get_processed_message


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load environment variables
load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
if bot_token is None:
    raise ValueError("No BOT_TOKEN found in environment variables")


# Your callback function
async def handle_button_press(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()  # Normalize text to lowercase
    if text == 'о боте':
        await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_info_message)
    elif text == 'отхуесоситься':
        insult_text = await get_insult()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=insult_text)
    else:
        # If the message is not recognized as a button press, process it with main logic.
        # This assumes process_message can be directly called with the update and context.
        await process_message(update, context)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Пошёл нахуй!")


async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username if user.username else user.full_name
    message_text = update.message.text.strip().lower()  # Ensure case-insensitive comparison

    # Directly call the synchronous function without await
    bot_response = get_processed_message(message_text)

    log_message(username, message_text, bot_response)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_response)


def main():
    application = ApplicationBuilder().token(bot_token).build()

    # Start and button command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('buttons', button_command))

    # Handler for button responses
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_button_press))

    # General message handler should be added last
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process_message))

    application.run_polling()


if __name__ == '__main__':
    main()
