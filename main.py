from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram.error import TelegramError
from config import TOKEN
from handlers.start_handler import start
from handlers.community_handler import community
from handlers.help_handler import help
from handlers.support_handler import support
from handlers.care_handler import (
    care, care_story, care_support_groups, care_tips, care_journaling,
    care_journaling_prompts, care_grounding, care_letters, care_younger_self
)
from handlers.learn_and_volunteer_handler import (
    learn_and_volunteer, learn_tips, learn_tips2, learn_tips3, learn_tips4,
    volunteer, learn_sa, learn_sexual_assault, learn_sexual_grooming, learn_sexual_grooming2, learn_sexual_grooming3,
    learn_consent, learn_consent2, learn_consent3, learn_victim_blaming, learn_victim_blaming2,
    learn_rape_myths
)

from handlers.learn_and_volunteer_handler import learn_and_volunteer
from handlers.feedback_handler import feedback

async def check_channel_access(bot):
    """Check if bot has access to channel"""
    try:
        channel_id = "@KOECO"
        await bot.get_chat(channel_id)
        print(f"Successfully connected to channel {channel_id}")
    except TelegramError as e:
        print(f"Error accessing channel: {e}")
        print("Please ensure bot is admin of @KOECO channel")

async def post_init(application: Application):
    """Called after bot initialization"""
    await check_channel_access(application.bot)

async def handle_story(update: Update, context):
    if context.user_data.get('expecting_story'):
        # TODO: Implement story handling logic (e.g., send to admin)
        await update.message.reply_text("Thank you for sharing your story. It has been received anonymously.")
        context.user_data['expecting_story'] = False

def main():
    application = Application.builder().token(TOKEN).post_init(post_init).build()


    # Main menu handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(start, pattern='^start$'))
    application.add_handler(CallbackQueryHandler(community, pattern='^community$'))
    application.add_handler(CallbackQueryHandler(help, pattern='^help$'))
    application.add_handler(CallbackQueryHandler(support, pattern='^support$'))
    application.add_handler(CallbackQueryHandler(care, pattern='^care$'))
    application.add_handler(CallbackQueryHandler(learn_and_volunteer, pattern='^learn_and_volunteer$'))
    application.add_handler(CallbackQueryHandler(feedback, pattern='^feedback$'))
    
    # Care menu handlers
    application.add_handler(CallbackQueryHandler(care_story, pattern='^care_story$'))
    application.add_handler(CallbackQueryHandler(care_support_groups, pattern='^care_support_groups$'))
    application.add_handler(CallbackQueryHandler(care_tips, pattern='^care_tips$'))
    application.add_handler(CallbackQueryHandler(care_journaling, pattern='^care_journaling$'))
    application.add_handler(CallbackQueryHandler(care_journaling_prompts, pattern='^care_journaling_prompts$'))
    application.add_handler(CallbackQueryHandler(care_grounding, pattern='^care_grounding$'))
    application.add_handler(CallbackQueryHandler(care_letters, pattern='^care_letters$'))
    application.add_handler(CallbackQueryHandler(care_younger_self, pattern='^care_younger_self$'))
    
    #learn and volunteer handlers
    application.add_handler(CallbackQueryHandler(learn_tips, pattern="^learn_tips$"))
    application.add_handler(CallbackQueryHandler(learn_tips2, pattern="^learn_tips2$"))
    application.add_handler(CallbackQueryHandler(learn_tips3, pattern="^learn_tips3$"))
    application.add_handler(CallbackQueryHandler(learn_tips4, pattern="^learn_tips4$"))
    application.add_handler(CallbackQueryHandler(volunteer, pattern="^volunteer$"))
    application.add_handler(CallbackQueryHandler(learn_sa, pattern="^learn_sa$"))
    application.add_handler(CallbackQueryHandler(learn_sexual_assault, pattern="^learn_sexual_assault$"))
    application.add_handler(CallbackQueryHandler(learn_sexual_grooming, pattern="^learn_sexual_grooming$"))
    application.add_handler(CallbackQueryHandler(learn_sexual_grooming2, pattern="^learn_sexual_grooming2$"))
    application.add_handler(CallbackQueryHandler(learn_sexual_grooming3, pattern="^learn_sexual_grooming3$"))
    application.add_handler(CallbackQueryHandler(learn_consent, pattern="^learn_consent$"))
    application.add_handler(CallbackQueryHandler(learn_consent2, pattern="^learn_consent2$"))
    application.add_handler(CallbackQueryHandler(learn_consent3, pattern="^learn_consent3$"))
    application.add_handler(CallbackQueryHandler(learn_victim_blaming, pattern="^learn_victim_blaming$"))
    application.add_handler(CallbackQueryHandler(learn_victim_blaming2, pattern="^learn_victim_blaming2$"))
    application.add_handler(CallbackQueryHandler(learn_rape_myths, pattern="^learn_rape_myths$"))

    # Story submission handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_story))
    
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()