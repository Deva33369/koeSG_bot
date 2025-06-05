from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def support(update: Update, context):
    text = (
        "📚 *Support & Resources* 📚\n\n"
        "I'm proud of you for taking the step to support yourself better 💛\n"
        "Which type of support do you need?"
    )
    keyboard = [
        [InlineKeyboardButton("🧠 Counselling Resources", callback_data='support_counselling')],
        [InlineKeyboardButton("⚖️ Legal Assistance & Reporting", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_counselling(update: Update, context):
    text = (
        "🧠 *Counselling Resources* 🧠\n\n"
        "Here are some counselling services available in Singapore:\n\n"
        "*AWARE Sexual Assault Care Centre (SACC)*\n"
        "• For all genders\n"
        "• Call: <code>67790282</code> (Mon-Fri, 10am-6pm)\n"
        "• Online chat via Zoom (Mon-Fri, 10am-4:30pm)\n"
        "• Email: sacc@aware.org.sg\n"
        "• Free counselling for survivors\n\n"
        "*Care Corner Project StART*\n"
        "• For all genders\n"
        "• Call: <code>64761482</code>\n"
        "• Email: projectstart@carecorner.org.sg\n"
        "• Free counselling and case management\n\n"
        "*Oogachaga (LGBTQ+ Support)*\n"
        "• WhatsApp: <code>85920609</code> (Tue & Thu: 7pm-10pm; Sat: 2pm-5pm)\n"
        "• Email: CARE@oogachaga.com\n"
        "• Free counselling for LGBTQ+ individuals\n\n"
        "*SCWO (Women-specific)*\n"
        "• Call: <code>8001014616</code> (9am-9pm)\n"
        "• WhatsApp: <code>65714400</code>\n"
        "• Free counselling for women\n\n"
        "*Note:* All services are confidential and many offer free or subsidized rates. Don't hesitate to ask about financial assistance if needed."
    )
    keyboard = [
        [InlineKeyboardButton("📞 Show Helplines", callback_data='helplines')],
        back_button('support')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)

async def support_legal(update: Update, context):
    text = (
        "⚖️ *Legal Assistance & Reporting* ⚖️\n\n"
        "Here are your options for legal support and reporting:\n\n"
        "*Immediate Police Reporting*\n"
        "• Call <code>999</code> for immediate assistance\n"
        "• Visit any police station\n"
        "• You can request for a female officer\n\n"
        "*Legal Aid*\n"
        "• [Legal Aid Bureau](https://lab.mlaw.gov.sg)\n"
        "  - Income-based legal aid\n"
        "  - Free legal representation\n"
        "  - Call: <code>18002255288</code>\n\n"
        "*AWARE Legal Clinic*\n"
        "• Free legal advice for women\n"
        "• Call: <code>69509191</code> (Mon-Fri, 10am-6pm)\n"
        "• Email: legalclinic@aware.org.sg\n\n"
        "*Important Notes:*\n"
        "1. You can report at any time, even if the incident happened years ago\n"
        "2. You have the right to request for a female officer\n"
        "3. You can bring a support person with you\n"
        "4. Legal aid is available based on income\n"
        "5. All services are confidential"
    )
    keyboard = [
        [InlineKeyboardButton("🚔 Emergency Police Contact", callback_data='emergency_police')],
        back_button('support')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)
