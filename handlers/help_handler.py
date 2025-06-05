from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def help(update: Update, context):
    text = (
        "🚨 *I Need Help (Crisis & Reporting)* 🚨\n\n"
        "Hello, thank you for reaching out! Please share if you are currently in an emergency.\n\n"
        "Examples of emergencies:\n"
        "- Police: a sexual assault/harassment case is currently/has just happened and you would like to report it immediately\n"
        "- SOS: if you have thoughts of hurting yourself or those around you."
    )
    keyboard = [
        [InlineKeyboardButton("Yes, I need to call the police now", callback_data='emergency_police')],
        [InlineKeyboardButton("Yes, I need to call SOS now", callback_data='emergency_sos')],
        [InlineKeyboardButton("No, I'm not in emergency - show helplines", callback_data='helplines')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def emergency_police(update: Update, context):
    text = (
        "🚔 <b>Emergency Police Contact</b> 🚔\n\n"
        "Please call <code>999</code> immediately for police assistance.\n\n"
        "If you are in immediate danger, please:\n"
        "1. Find a safe place if possible\n"
        "2. Call 999\n"
        "3. Stay on the line with the operator\n"
        "4. Follow their instructions\n\n"
        "Remember: You are not alone, and help is available."
    )
    keyboard = [back_button('help')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)

async def emergency_sos(update: Update, context):
    text = (
        "🆘 <b>Emergency SOS Contact</b> 🆘\n\n"
        "Please call <code>18002214444</code> immediately.\n\n"
        "If you are having thoughts of hurting yourself or others:\n"
        "1. Call SOS now\n"
        "2. Stay on the line\n"
        "3. They are available 24/7\n"
        "4. You are not alone\n\n"
        "Remember: Your life matters, and help is available."
    )
    keyboard = [back_button('help')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)

async def helplines(update: Update, context):
    text = (
        "📞 <b>Helplines & Support Services</b> 📞\n\n"
        "Hello! Thank you for reaching out! KOE hopes to support you in any way possible. "
        "Below are some helplines you could reach out to depending on your needs and preference.\n\n"
        "<b>For Sexual Assault Related Matters (All Genders):</b>\n"
        "• <b><a href='https://www.aware.org.sg'>AWARE</a></b>\n"
        "  - Call: <code>67790282</code> (Mon-Fri, 10am-6pm)\n"
        "  - Online chat via Zoom (Mon-Fri, 10am-4:30pm)\n"
        "  - Email: sacc@aware.org.sg\n\n"
        "• <b><a href='https://www.carecorner.org.sg'>Care Corner</a></b>\n"
        "  - Call: <code>64761482</code>\n"
        "  - Email: projectstart@carecorner.org.sg\n\n"
        "<b>For Workplace Harassment/Discrimination:</b>\n"
        "• <b><a href='https://www.aware.org.sg'>AWARE</a></b>\n"
        "  - Call: <code>69509191</code> (Mon-Fri, 10am-6pm)\n\n"
        "<b>For Sex Workers:</b>\n"
        "• <b><a href='https://projectx.org.sg'>Project X</a></b>\n"
        "  - Call: <code>90609906</code> (3pm-11:30pm)\n\n"
        "<b>For Primary School Children:</b>\n"
        "• <b><a href='https://www.tinklefriend.sg'>Tinkle Friend</a></b>\n"
        "  - Call: <code>18002744788</code>\n\n"
        "<b>For LGBTQ+ Support:</b>\n"
        "• <b><a href='https://www.oogachaga.com'>Oogachaga</a></b>\n"
        "  - WhatsApp: <code>85920609</code> (Tue & Thu: 7pm-10pm; Sat: 2pm-5pm)\n"
        "  - Email: CARE@oogachaga.com\n\n"
        "<b>For Online Sexual Harassment/Abuse:</b>\n"
        "• <b><a href='https://www.scwo.org.sg'>SCWO</a></b> (Women-specific, 9am-9pm)\n"
        "  - Call: <code>8001014616</code>\n"
        "  - WhatsApp: <code>65714400</code>\n\n"
        "For more resources regarding <b>online sexual harassment/abuse</b>, visit <b><a href='https://www.solidground.sg'>Solid Ground</a></b>."
    )
    keyboard = [back_button('help')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)