from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Join our Community!", callback_data='community')],
        [InlineKeyboardButton("I Need Help (Crisis & Reporting)", callback_data='help')],
        [InlineKeyboardButton("Support & Resources", callback_data='support')],
        [InlineKeyboardButton("Self-Care & Healing", callback_data='care')],
        [InlineKeyboardButton("Learn", callback_data='learn')],
        [InlineKeyboardButton("Have some feedback?", callback_data='feedback')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    trigger_warning = (
        "\n\n⚠️ *Trigger Warning* ⚠️\n\n"
        "This bot discusses topics related to sexual assault and trauma. "
        "Some content may be triggering or distressing. Please take care of yourself "
        "and use this resource at your own pace. You can always take a break or exit.\n\n"
    )
    intro_text = (
        "🌸 *About KOE & This Bot* 🌸\n\n"
        "Hello! This bot is created by KOE (ko-eh), a project that strives to amplify voices of sexual assault survivors in Singapore. (This bot was also curated with the support of students from SIT.)\n\n"
        "We are here to support sexual assault survivors by providing a one-stop centre for all types of resources required such as resources for counselling or legal assistance, helplines self care tips, when in need. This bot can also support you (friends/families of survivors) in order to better support your loved ones when faced with such circumstances.\n\n"
        "This bot ensures privacy and confidentiality, thereby your user is kept completely anonymous. If you would like to reach out to KOE for any matters, do email us via gmail at koebusiness2022@gmail.com"
    )
    if update.message:
        await update.message.reply_text(intro_text + trigger_warning, parse_mode='Markdown')
        await update.message.reply_text("Please choose an option below:", reply_markup=reply_markup)
    elif hasattr(update, 'callback_query') and update.callback_query is not None:
        await update.callback_query.edit_message_text("Please choose an option below:", reply_markup=reply_markup)