from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button
from config import ADMIN_ID

async def feedback(update: Update, context):
    text = (
        "📝 *Feedback* 📝\n\n"
        "We'd love to hear from you! Your feedback helps us improve our services and better support our community.\n\n"
        "Please share your feedback about:\n"
        "- Bot suggestions\n"
        "- Resource requests\n"
        "- General feedback\n"
        "- Anonymous testimonial\n\n"
        "Type your feedback below:"
    )
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)
    context.user_data['expecting_feedback'] = True

async def handle_feedback(update: Update, context):
    if context.user_data.get('expecting_feedback'):
        # Forward the feedback to admin
        feedback_text = (
            "📨 *New Feedback Submission* 📨\n\n"
            f"From User ID: `{update.effective_user.id}`\n"
            f"Feedback:\n{update.message.text}"
        )
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=feedback_text,
                parse_mode='Markdown'
            )
            await update.message.reply_text(
                "Thank you for your feedback! It has been received and will be reviewed by our team."
            )
        except Exception as e:
            print(f"Error forwarding feedback to admin: {e}")
            await update.message.reply_text(
                "We're sorry, but there was an error sending your feedback. Please try again later."
            )
        context.user_data['expecting_feedback'] = False