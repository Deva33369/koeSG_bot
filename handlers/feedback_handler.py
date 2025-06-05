from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.utils import back_button
import os


#ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "123456789")  # Replace with your actual admin chat ID

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💬 *Have Some Feedback?* 💬\n\n"
        "We value your thoughts and ideas to improve this bot!\n"
        "Please type your feedback below. It will be sent anonymously to our admin team."
    )
    context.user_data['expecting_feedback'] = True

    keyboard = [
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text=text, parse_mode='Markdown', reply_markup=reply_markup)


async def handle_user_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if context.user_data.get('expecting_feedback'):
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"💬 *New Feedback:*\n{text}",
            parse_mode='Markdown'
        )
        await update.message.reply_text("Thank you for your feedback! It has been sent anonymously.")
        context.user_data['expecting_feedback'] = False
