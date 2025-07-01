from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def community(update: Update, context):
    text = (
        "🌟 Join our Community! 🌟"
        "Stay updated on KOE happenings and sexual assault news in Singapore via our [Telegram Channel](https://t.me/KOECO)\n\n"
        "Check out our [Link Tree](http://linkt.ree/koe.co_/) for our socials and website!"
    )
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)