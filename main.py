from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN, ADMIN_ID
from handlers.start_handler import start
from handlers.community_handler import community
from handlers.help_handler import help, emergency_police, emergency_sos, helplines
from handlers.support_handler import support
from handlers.care_handler import (
    care, care_story, care_support_groups, care_tips, care_journaling,
    care_journaling_prompts, care_grounding, care_letters, care_younger_self
)
from handlers.learn_handler import learn
from handlers.feedback_handler import feedback, handle_feedback

async def myid(update: Update, context):
    """Command handler to show the user's Telegram ID"""
    user_id = update.effective_user.id
    await update.message.reply_text(
        f"Your Telegram ID is: `{user_id}`\n\n"
        "If you are the admin, please copy this ID and update it in the config.py file.",
        parse_mode='Markdown'
    )

async def handle_story(update: Update, context):
    if context.user_data.get('expecting_story'):
        # Forward the story to admin
        story_text = (
            "📨 *New Story Submission* 📨\n\n"
            f"From User ID: `{update.effective_user.id}`\n"
            f"Story:\n{update.message.text}"
        )
        try:
            print(f"Attempting to forward story to admin ID: {ADMIN_ID}")  # Debug log
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=story_text,
                parse_mode='Markdown'
            )
            print("Story successfully forwarded to admin")  # Debug log
            await update.message.reply_text(
                "Thank you for sharing your story. It has been received anonymously and will be reviewed by our team."
            )
        except Exception as e:
            print(f"Error forwarding story to admin: {e}")  # Debug log
            print(f"Admin ID being used: {ADMIN_ID}")  # Debug log
            print(f"Story content: {update.message.text}")  # Debug log
            await update.message.reply_text(
                "We're sorry, but there was an error sending your story. Please try again later."
            )
        context.user_data['expecting_story'] = False

def main():
    application = Application.builder().token(TOKEN).build()
    
    # Main menu handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('myid', myid))
    application.add_handler(CallbackQueryHandler(start, pattern='^start$'))
    application.add_handler(CallbackQueryHandler(community, pattern='^community$'))
    application.add_handler(CallbackQueryHandler(help, pattern='^help$'))
    application.add_handler(CallbackQueryHandler(support, pattern='^support$'))
    application.add_handler(CallbackQueryHandler(care, pattern='^care$'))
    application.add_handler(CallbackQueryHandler(learn, pattern='^learn$'))
    application.add_handler(CallbackQueryHandler(feedback, pattern='^feedback$'))
    
    # Help menu handlers
    application.add_handler(CallbackQueryHandler(emergency_police, pattern='^emergency_police$'))
    application.add_handler(CallbackQueryHandler(emergency_sos, pattern='^emergency_sos$'))
    application.add_handler(CallbackQueryHandler(helplines, pattern='^helplines$'))
    
    # Care menu handlers
    application.add_handler(CallbackQueryHandler(care_story, pattern='^care_story$'))
    application.add_handler(CallbackQueryHandler(care_support_groups, pattern='^care_support_groups$'))
    application.add_handler(CallbackQueryHandler(care_tips, pattern='^care_tips$'))
    application.add_handler(CallbackQueryHandler(care_journaling, pattern='^care_journaling$'))
    application.add_handler(CallbackQueryHandler(care_journaling_prompts, pattern='^care_journaling_prompts$'))
    application.add_handler(CallbackQueryHandler(care_grounding, pattern='^care_grounding$'))
    application.add_handler(CallbackQueryHandler(care_letters, pattern='^care_letters$'))
    application.add_handler(CallbackQueryHandler(care_younger_self, pattern='^care_younger_self$'))
    
    # Message handlers for story and feedback submissions
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_story))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback))
    
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()