from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def help(update: Update, context):
    text = (
        "🚨 *I Need Help (Reporting & Helplines)* 🚨\n\n"
        "Please contact:\n\n"
        "The Police at 999: If a sexual assault/harassment case is currently/has just happened and you would like to report it immediately. \n\n"
        "SOS at 18002214444: If you have thoughts of hurting yourself or those around you.\n\n"
        "You are not alone, and help is available 🤍. Please find a safe space, stay on the line and follow their instructions."
    )
    keyboard = [
        [InlineKeyboardButton("Show helplines", callback_data='helplines')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def helplines(update: Update, context):
    text = (
        "🫶 *Helplines & Support Services* 🫶\n\n"
        "Hello! Thank you for reaching out! KOE hopes to support you in any way possible. "
        "Below are some helplines you could reach out to depending on your needs and preference.\n\n"
        "<b>For Sexual Assault Related Matters (All Genders):</b>\n"
        "• <b><a href='https://sacc.aware.org.sg/get-help/talk-to-us/'>AWARE</a></b>\n"
        "  - Call: <code>67790282</code> (Mon-Fri, 10am-6pm)\n"
        "  - Online chat via Zoom (Mon-Fri, 10am-4:30pm)\n"
        "  - Email: sacc@aware.org.sg\n\n"
        "• <b><a href='https://www.aware.org.sg/womens-care-centre/helpline/'>AWARE</a>(Women's Specific Helpline)</b>\n"
        "  - Call: <code>1800 777 5555</code> (Mon-Fri, 10am-6pm)\n"
        "  - Schedule an <a href='https://www.aware.org.sg/womens-care-centre/callback-chat/'>online appointment</a>\n\n"
        "• <b><a href='https://www.carecorner.org.sg/services/sexual-assault-recovery/'>Care Corner</a></b>\n"
        "  - Call: <code>64761482</code>\n"
        "  - Email: projectstart@carecorner.org.sg\n\n"
        "<b>For Sex Workers:</b>\n"
        "• <b><a href='https://projectx.org.sg/'>Project X</a></b>\n"
        "  - Call: <code>90609906</code> (3pm-11:30pm)\n\n"
        "<b>For Primary School Children:</b>\n"
        "• <b><a href='https://www.tinklefriend.sg/'>Tinkle Friend</a></b>\n"
        "  - Call: <code>18002744788</code>\n\n"
        "<b>For LGBTQ+ Support:</b>\n"
        "• <b><a href='https://www.oogachaga.com/contact'>Oogachaga</a></b>\n"
        "  - WhatsApp: <code>85920609</code> (Tue & Thu: 7pm-10pm; Sat: 2pm-5pm)\n"
        "  - Email: CARE@oogachaga.com\n\n"
        "<b>For Online Sexual Harassment/Abuse:</b>\n"
        "• <b><a href='https://www.scwo.org.sg/'>Singapore Council of Women's Organisations</a></b> (Women-specific, 9am-9pm)\n"
        "  - Call: <code>8001014616</code>\n"
        "  - WhatsApp: <code>65714400</code>\n\n"
        "For more resources regarding <b>online sexual harassment/abuse</b>, visit <b><a href='https://www.solidground.sg'>Solid Ground</a></b>."
    )
    keyboard = [back_button('help')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)