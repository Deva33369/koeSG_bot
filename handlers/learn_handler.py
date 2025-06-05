from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def learn(update: Update, context):
    text = (
        "📢 <b>Learn & Volunteer</b> 📢\n\n"
        "**Educational Guides**:\n"
        "- [Understanding Consent](https://example.com/consent)\n"
        "- [How to Support Survivors](https://example.com/support-guide)\n\n"
        "**Volunteer Opportunities**:\n"
        "- Join KOE's outreach team (Email us!).\n"
        "- Help moderate our community chats."
    )
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)