from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import TelegramError
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN, ADMIN_ID
from handlers.start_handler import start
from handlers.community_handler import community
from handlers.help_handler import help, emergency_police, emergency_sos, helplines
from handlers.support_handler import (
    support, support_counselling, support_legal,
    support_legal_clinic, support_legal_police,
    support_legal_poha, support_legal_ppo, support_legal_other,
)
from handlers.care_handler import (
    care, care_story, care_story_another, care_support_groups, care_tips, care_journaling,
    care_journaling_prompts, care_grounding, care_letters, care_younger_self
)



from handlers.learn_handler import (
    learn, learn_tips, learn_tips2, learn_tips3, learn_tips4,
    volunteer, learn_sa, learn_sexual_assault, learn_sexual_grooming,
    learn_sexual_grooming2, learn_sexual_grooming3, learn_consent,
    learn_consent2, learn_consent3, learn_victim_blaming,
    learn_victim_blaming2, learn_rape_myths
)
from handlers.feedback_handler import feedback, handle_feedback

def myid(update: Update, context):
    """Command handler to show the user's Telegram ID"""
    user_id = update.effective_user.id
    update.message.reply_text(
        f"Your Telegram ID is: `{user_id}`\n\n"
        "If you are the admin, please copy this ID and update it in the config.py file.",
        parse_mode='Markdown'
    )

def handle_story(update: Update, context):
    if context.user_data.get('expecting_story'):
        # Forward the story to admin
        story_text = (
            "📨 *New Story Submission* 📨\n\n"
            f"From User ID: `{update.effective_user.id}`\n"
            f"Story:\n{update.message.text}"
        )
        try:
            print(f"Attempting to forward story to admin ID: {ADMIN_ID}")  # Debug log
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=story_text,
                parse_mode='Markdown'
            )
            print("Story successfully forwarded to admin")  # Debug log
            
            # Send confirmation message with option to share another story
            keyboard = [
                [InlineKeyboardButton("Share Another Story", callback_data='care_story_another')],
                [InlineKeyboardButton("Back to Self-Care", callback_data='care')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            update.message.reply_text(
                "Thank you for sharing your story. It has been received anonymously and will be reviewed by our team.\n\n"
                "If you have more stories to share, you can click the button below.",
                reply_markup=reply_markup
            )
        except Exception as e:
            print(f"Error forwarding story to admin: {e}")  # Debug log
            print(f"Admin ID being used: {ADMIN_ID}")  # Debug log
            print(f"Story content: {update.message.text}")  # Debug log
            update.message.reply_text(
                "We're sorry, but there was an error sending your story. Please try again later."
            )
        context.user_data['expecting_story'] = False

def handle_message(update: Update, context):
    """Handle both story and feedback submissions based on user state"""
    if context.user_data.get('expecting_story'):
        handle_story(update, context)
    elif context.user_data.get('expecting_feedback'):
        handle_feedback(update, context)

def main():
    try:
        # Initialize the updater with error handling
        updater = Updater(token=TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        
        # Main menu handlers
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(CommandHandler('myid', myid))
        dispatcher.add_handler(CallbackQueryHandler(start, pattern='^start$'))
        dispatcher.add_handler(CallbackQueryHandler(community, pattern='^community$'))
        dispatcher.add_handler(CallbackQueryHandler(help, pattern='^help$'))
        dispatcher.add_handler(CallbackQueryHandler(support, pattern='^support$'))
        dispatcher.add_handler(CallbackQueryHandler(care, pattern='^care$'))
        dispatcher.add_handler(CallbackQueryHandler(learn, pattern='^learn'))
        dispatcher.add_handler(CallbackQueryHandler(feedback, pattern='^feedback$'))
        
        # Help menu handlers
        dispatcher.add_handler(CallbackQueryHandler(emergency_police, pattern='^emergency_police$'))
        dispatcher.add_handler(CallbackQueryHandler(emergency_sos, pattern='^emergency_sos$'))
        dispatcher.add_handler(CallbackQueryHandler(helplines, pattern='^helplines$'))
        
        # Support menu handlers
        dispatcher.add_handler(CallbackQueryHandler(support_counselling, pattern='^support_counselling$'))
        dispatcher.add_handler(CallbackQueryHandler(support_legal, pattern='^support_legal$'))
        dispatcher.add_handler(CallbackQueryHandler(support_legal_clinic, pattern='^support_legal_clinic$'))
        dispatcher.add_handler(CallbackQueryHandler(support_legal_police, pattern='^support_legal_police$'))
        dispatcher.add_handler(CallbackQueryHandler(support_legal_poha, pattern='^support_legal_poha$'))
        dispatcher.add_handler(CallbackQueryHandler(support_legal_ppo, pattern='^support_legal_ppo$'))
        dispatcher.add_handler(CallbackQueryHandler(support_legal_other, pattern='^support_legal_other$'))
        
        # Care menu handlers
        dispatcher.add_handler(CallbackQueryHandler(care_story, pattern='^care_story$'))
        dispatcher.add_handler(CallbackQueryHandler(care_story_another, pattern='^care_story_another$'))
        dispatcher.add_handler(CallbackQueryHandler(care_support_groups, pattern='^care_support_groups$'))
        dispatcher.add_handler(CallbackQueryHandler(care_tips, pattern='^care_tips$'))
        dispatcher.add_handler(CallbackQueryHandler(care_journaling, pattern='^care_journaling$'))
        dispatcher.add_handler(CallbackQueryHandler(care_journaling_prompts, pattern='^care_journaling_prompts$'))
        dispatcher.add_handler(CallbackQueryHandler(care_grounding, pattern='^care_grounding$'))
        dispatcher.add_handler(CallbackQueryHandler(care_letters, pattern='^care_letters$'))
        dispatcher.add_handler(CallbackQueryHandler(care_younger_self, pattern='^care_younger_self$'))

        #learn and volunteer handlers
        dispatcher.add_handler(CallbackQueryHandler(learn_tips, pattern="^learn_tips$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_tips2, pattern="^learn_tips2$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_tips3, pattern="^learn_tips3$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_tips4, pattern="^learn_tips4$"))
        dispatcher.add_handler(CallbackQueryHandler(volunteer, pattern="^volunteer$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_sa, pattern="^learn_sa$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_sexual_assault, pattern="^learn_sexual_assault$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_sexual_grooming, pattern="^learn_sexual_grooming$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_sexual_grooming2, pattern="^learn_sexual_grooming2$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_sexual_grooming3, pattern="^learn_sexual_grooming3$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_consent, pattern="^learn_consent$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_consent2, pattern="^learn_consent2$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_consent3, pattern="^learn_consent3$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_victim_blaming, pattern="^learn_victim_blaming$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_victim_blaming2, pattern="^learn_victim_blaming2$"))
        dispatcher.add_handler(CallbackQueryHandler(learn_rape_myths, pattern="^learn_rape_myths$"))
        
        # Story submission handler
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_story))

        # Message handler for both story and feedback submissions
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

        print('Bot is running...') 
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        print(f"Error starting bot: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()