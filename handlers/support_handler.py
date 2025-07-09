from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def support(update: Update, context):
    text = (
        "🌷 *Support & Resources* 🌷\n\n"
        "Resources can get overwhelming and sometimes tough to find. We hope to provide a consolidated area for you to find the best support you might require! What type of resources are you looking for?"
    )
    keyboard = [
        [InlineKeyboardButton("❤️‍🩹 Counselling Resources", callback_data='support_counselling')],
        [InlineKeyboardButton("⚖️ Legal Assistance & Reporting", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_counselling(update: Update, context):
    text = (
        "❤️‍🩹 *Counselling Support* ❤️‍🩹\n\n"
        "Many sexual assault survivors often find it helpful to talk to a counsellor. You don’t need to fix anything — sometimes it’s about taking the step to learn to be kinder to yourself, or to just talk about what happened instead of keeping it in. We hope these support systems can allow you to flourish.\n\n"

        "📌 Note: Many of these services are provided mainly in English. We highly recommend bringing an English-speaking friend or family member to help with translation. If not, feel free to reach out to the National Anti-Violence & Sexual Harassment Hotline at 1800 777 0000 (24/7, available in English, Mandarin, Malay, and Tamil).\n\n"

        "For any Sexual Assault Related Counselling Matters\n"
        "AWARE’s counsellors have the experience and sensitivity needed to support sexual assault victims. All support is provided on a strictly confidential basis.\n\n"

        "• Each session is 1 hour long, by appointment only.\n"
        "• Held at AWARE Centre or via Zoom (Mon–Fri, 10 a.m. – 8 p.m., last appointment at 7 p.m.)\n"
        "• Call 6779 0282 (Helpline: Mon–Fri, 10 a.m. – 6 p.m.)\n"
        "• Online chat service: Mon–Fri, 10 a.m. – 4:30 p.m.\n"
        "• Email: sacc@aware.org.sg (Monitored every few hours)\n\n"

        "Counselling Fees:\n"
        "• Not working / salary < $3,000: Flat fee of $35 per session\n"
        "• Salary ≥ $3,000: 2% of monthly salary per session\n\n"

        "For Online Sexual Assault/Harassment Related Matters\n"
        "Singapore Council of Women’s Organisations (SCWO)'s counsellors are trained in trauma-informed care and provides free counselling sessions for victims or survivors of online harm.\n\n"

        "• Available: Mon–Fri, 9 a.m. – 6 p.m.\n"
        "• Call: 8001 01 4616\n"
        "• WhatsApp: 6571 4400\n\n"
    )
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Support & Resources Menu", callback_data='support')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_legal(update: Update, context):
    text = (
        
        "🤎 *Legal Assistance & Reporting* 🤎\n\n"

        "Taking the step towards reporting and getting involved in the law can be daunting. I’m proud of you for taking this step and finding ways for you to get justice. These are the legal resources available — feel free to explore and let us know your preference.\n\n"

        "Legal Clinics\n"
        "Volunteer lawyers provide free legal assistance at legal clinics. They can give general legal advice on your case, explain your options, and support you throughout the legal process.\n\n"

        "Criminal Proceedings\n"
        "• Making a Police Report: To initiate a criminal investigation and formal proceedings.\n"
        "• Protection from Harassment Act Order (POHA): For physical or non-physical sexual harassment.\n"
        "  → If you're experiencing harassment or stalking, POHA allows you to apply for protection orders or non-publication orders.\n"
        "• Personal Protection Order (PPO): For physical or non-physical sexual assault/harassment by a family member only.\n\n"

        "📌 Other Complaints — Additional legal avenues are available depending on your situation."
    )
    keyboard = [
        [InlineKeyboardButton("📑 Legal Clinics", callback_data='support_legal_clinic')],
        [InlineKeyboardButton("🚓 Police Reporting", callback_data='support_legal_police')],
        [InlineKeyboardButton("📄 Protection from Harassment Act (POHA)", callback_data='support_legal_poha')],
        [InlineKeyboardButton("🛡 Personal Protection Order (PPO)", callback_data='support_legal_ppo')],
        [InlineKeyboardButton("📬 Other Legal Complaints", callback_data='support_legal_other')],
        [InlineKeyboardButton("🔙 Back to Support & Resources Menu", callback_data='support')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_legal_clinic(update: Update, context):
    text = (
        "🤎 *Legal Clinics* 🤎\n\n"

        "Sexual Assault Care Centre\n"
        "[SACC](https://sacc.aware.org.sg/get-help/legal-information/)'s legal clinic offers a one-time 30-minute session where SACC’s volunteer lawyers can provide general legal information on your case and share about the options available to you. They are open to survivors of all genders, and the legal clinic is reserved for clients who do not already have legal representation on the same matter. (English-speaking only)\n\n"
        "• Call: 6779 0282\n"
        "• Email: sacc@aware.org.sg\n"
        "• Book an [online appointment](https://sacc.aware.org.sg/sacc-online-chat-service/)\n\n"

        "Singapore Council of Women’s Organisations\n"
        "[SCWO](https://www.scwo.org.sg/what-we-do/services/shecaresscwo/): Legal volunteers from Pro Bono SG will offer a free 30 minutes legal assistance session at legal clinics. Every 1st and 3rd Wednesday of the Month, 7 pm - 9 pm. \n"
        "• Call: 8001 01 4616\n"
        "• WhatsApp: 6571 4400\n"
    )
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Legal Options", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_legal_police(update: Update, context):
    text = (
    "🚔 *Making a Police Report* 🚔\n\n"
    "*Making a police report can be daunting* for many and the process can also be extremely difficult as you are required to “relive” or constantly retell what has happened to you. "
    "It can be traumatic but it’s a form of justice for you as well.\n\n"
    "We hope to prepare you mentally for what’s to come and to share the support provided for you during this process.\n\n"
    
    "If you decide to make a report, *the earlier you make a report, the easier it is* for the police to investigate and prosecute the perpetrator. "
    "But you can make a police report *any time after the incident*, no matter how long it has been. "
    "The police will be obliged to investigate whenever a report is made.\n\n"

    "📞 *How to report:*\n"
    "- Call *999*, or\n"
    "- Visit the nearest *police centre* or *police post*\n"
    "- These operate *24/7*\n"
    "- [Find your nearest police centre/post](http://www.police.gov.sg/contact/)\n\n"

    "📝 *What happens after reporting:*\n"
    "- You’ll be interviewed briefly in a *private room*\n"
    "- A specially trained *Investigation Officer (IO)* will record your statement\n"
    "- You can *request for breaks* anytime\n"
    "- *Victim Care Officer* services are available for emotional support\n"
    "- If needed, you may be taken to *OneSAFE Centre* or hospital for forensic exam\n"
    "- [More info here](https://www.police.gov.sg/Advisories/Crime/Sexual-Crime#:~:text=If%20a%20report%20is%20lodged,a%20statement%20from%20the%20victim.)\n\n"

    "❗ *Things to note:*\n"
    "- Your *identity will be protected*\n"
    "- You may testify in *closed-door hearing*, *behind a screen*, or *via video link*\n"
    "- *Inappropriate questions* cannot be asked unless allowed by court\n"
    "- You *may be asked* about clothing or sexual history—this is part of fact-finding, *not victim blaming*\n"
    "- If uncomfortable, *request a Victim Care Officer*\n"
    "- [Why these questions matter – Read here](https://www.straitstimes.com/singapore/courts-crime/why-knowing-sexual-history-and-what-victim-wore-help-police-in-rape)\n\n"

    "⏱️ *Timeline:*\n"
    "Police investigations into sexual crimes take *about 12 months* on average, but this varies based on case complexity."
    )
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Legal Options", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_legal_poha(update: Update, context):
    text = (
        "📄 *Protection from Harassment Act (POHA)* 📄\n\n"
        "If you're being harassed online or offline, you can seek help under POHA.\n\n"
        "🔹 Learn more and get guidance via [AWARE's POHA Information Page](https://sacc.aware.org.sg/get-information/protection-from-harassment-act/)\n"
        "🔹 You can also seek advice from AWARE or the Legal Aid Bureau\n"
        "🔹 Court may grant Protection Order, Expedited Order, or Counselling"
    )
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Legal Options", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_legal_ppo(update: Update, context):
    text = (
        "🛡 *Personal Protection Order (PPO)* 🛡\n\n"
        "If you're experiencing family violence, you can seek help and apply for a PPO.\n\n"
        "🔹 Learn more and get guidance via [AWARE's PPO Information Page](https://www.aware.org.sg/information/dealing-with-family-violence/getting-a-personal-protection-order/)\n"
        "🔹 You can also get counselling or mediation\n"
        "🔹 Assistance available through AWARE or Family Service Centres"
    )
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Legal Options", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support_legal_other(update: Update, context):
    text = (
        "📝 *Other Legal Complaints* 📝\n\n"
        "You may also wish to explore:\n\n"
        "• *Protection for Persons with Mental Disabilities Act (PPMDA)*\n"
        "• *Workplace harassment reporting (via HR or MOM)*\n"
        "• *University/School complaint mechanisms*\n\n"
        "Learn more and get guidance via [AWARE's Filing a Complaint Page](https://sacc.aware.org.sg/get-help/filing-a-complaint/)\n\n"
        "Legal processes can feel scary, but you’re not alone. You deserve to feel safe."
    )
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Legal Options", callback_data='support_legal')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)
