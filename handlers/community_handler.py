from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def community(update: Update, context):
    text = (
        "🌟 *Join our Community!* 🌟\n\n"
        "Connect with survivors and allies in a safe, moderated space.\n"
        "- [Public Awareness Channel](https://t.me/KOECO) (Updates/resources)\n\n"
        "Rules:\n"
        "1. Respect anonymity.\n"
        "2. No victim-blaming.\n"
        "3. Trigger warnings for sensitive content."
    )
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)