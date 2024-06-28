from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def button_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton('Отхуесоситься'), KeyboardButton('О боте')]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Чё хочешь, пёс? 🦮",
                                   reply_markup=reply_markup)
