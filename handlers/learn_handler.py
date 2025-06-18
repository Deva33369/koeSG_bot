from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button, next_button
from telegram.ext import ContextTypes


async def learn(update: Update, context):
    text = (
        "📢 *Learn & Volunteer* 📢\n\n"
        "Welcome to our educational and volunteering hub! Here, you can:\n\n"
        "🎓 *Learn More*\n"
        "- Understand how to support survivors\n"
        "- Learn about consent and sexual assault\n"
        "- Educate yourself about common misconceptions\n\n"
        "🤝 *Volunteer With Us*\n"
        "- Join our community initiatives\n"
        "- Help create awareness\n"
        "- Make a difference in survivors' lives\n\n"
        "Choose an option below to get started:"
    )
    keyboard = [
        [InlineKeyboardButton("I want to know how to support survivors 🫂", callback_data='learn_tips')],
        [InlineKeyboardButton("I want to learn more about sexual assault 💡", callback_data='learn_sa')],
        [InlineKeyboardButton("I want to volunteer 💯", callback_data='volunteer')],
        back_button()
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_tips(update: Update, context):
    text = (
        "🫂 *Supporting Survivors* 🫂\n\n"
        "Response towards sexual assault is critical whereby negative reactions can spiral into something much worse. Here are some tips and reminders when responding to a survivor ❤️‍🩹\n\n"
        "*Click next to learn more!*"
    )

    keyboard = [
        next_button('learn_tips2'),
        back_button('learn')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_tips2(update: Update, context):
    text = (
        "🫂 *Supporting Survivors* 🫂\n\n"
        "*Reminders 💞:*\n\n"
        "1. Sexual assault happens because of someone else's decision to violate another person\n" 
        "2. Many survivors suffer in silence because they fear being disbelieved or judged\n" 
        "3. Do not judge. Believe the survivor\n"
        "4. Your job is to not give advice. Your job is to be there and support their decisions\n\n"
    )

    keyboard = [
        next_button('learn_tips3'),
        back_button('learn_tips'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]   
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_tips3(update: Update, context):
    text = (
        "🫂 *Supporting Survivors* 🫂\n\n"
        "*Tips:*\n\n"
        "1. Do not blame the victim. Do not ask detailed questions if they are not comfortable sharing and do not ask questions you do not need to know (eg, what were you wearing? Why didn't you leave? Why were you alone?) You are not an investigator, you are a friend trying to be there for them. Allow them to share how they feel. Allow them to react, and support them in processing what has happened.\n\n"
        "2. Ensure their safety. If they are calling you immediately after it has happened, ensure they are away from the perpetrator and in a safe place. Check in with them on whether they would like to call the police or if they are physically hurt, to seek medical attention\n\n"
        "3. Practise Active Listening. Use phrases such as \"I hear you\", \"do you want to share more?\" \"What were you feeling?\"\n\n"
        "4. Empathise with them. Remind them that it was not their fault, that what they went through is traumatic and their feelings are valid. Remind them that you are here for them.\n\n" 
        "5. Refer them to helplines, counselling or legal help. Offer to join them if they make a decision to report, or receive support as they could use a loved one there with them."
    )

    keyboard = [
        next_button('learn_tips4'),
        back_button('learn_tips2'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]   
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_tips4(update: Update, context):
    text = (
        "🫂 *Supporting Survivors* 🫂\n\n"
        "If you would like to learn more and be more confident in supporting sexual assault survivors or your loved ones, "
        "Sexual Assault First Responder Training (SAFRT) conducted by AWARE is meant to train the community to respond and support survivors. "
        "Check our their [website](https://www.aware.org.sg/training/community-programmes) for more information and to attend the next workshop")

    keyboard = [
        back_button('learn_tips3'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]   
   
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def volunteer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Get the pinned message from @koetrial channel
        channel_username = "@koetrial"
        
        # Get the chat object which includes pinned message
        chat = await context.bot.get_chat(chat_id=channel_username)
        
        if hasattr(chat, 'pinned_message') and chat.pinned_message:
            # Create keyboard with options
            keyboard = [
                [InlineKeyboardButton("Visit Our Channel", url="https://t.me/KOECO")],
                [InlineKeyboardButton("Visit Our Instagram", url="https://www.instagram.com/koe.co_/")],
                back_button('learn')
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            # Forward the pinned message with buttons
            await chat.pinned_message.forward(
                chat_id=update.effective_chat.id,
                reply_markup=reply_markup
            )
        else:
            # No pinned message found - send fallback message
            text = (
                "💫 *Volunteer with KOE* 💫\n\n"
                "Thank you for your interest in volunteering with us! We're always looking for passionate individuals to help make a difference.\n\n"
                "Please check these links for current opportunities:"
            )
            keyboard = [
                [InlineKeyboardButton("Visit Our Channel", url="https://t.me/KOECO")],
                [InlineKeyboardButton("Visit Our Instagram", url="https://www.instagram.com/koe.co_/")],
                back_button('learn')
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)
    
    except Exception as e:
        print(f"Error in volunteer function: {e}")
        # Fallback if any error occurs
        text = "💫 *Volunteer with KOE* 💫\n\nThank you for your interest! Please check our channels for current opportunities."
        keyboard = [
            [InlineKeyboardButton("Visit Our Channel", url="https://t.me/KOECO")],
            [InlineKeyboardButton("Visit Our Instagram", url="https://www.instagram.com/koe.co_/")],
            back_button('learn')
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_sa(update: Update, context):
    text = (
            "⚠️ *Content Warning* ⚠️\n\n"
            "The following sections contain detailed information about sexual assault, "
            "grooming, and related topics. This content may be triggering or distressing. "
            "Please take care of yourself and proceed only if you feel ready.\n\n"
            "💡 *Learning more* 💡\n\n"
            "Learning more about sexual assault and consent can be a great way to ensure we continue to teach ourselves and our loved ones the right thing!\n\n"
            "We also hope education can be a way to remind survivors that it was not "
            "their fault. We hope these topics (and more to come) will support your learning and understanding about sexual assault 🤍"
        )
  
    keyboard = [
        [InlineKeyboardButton("What is Sexual Assault?", callback_data='learn_sexual_assault')],
        [InlineKeyboardButton("What is Sexual Grooming?", callback_data='learn_sexual_grooming')],
        [InlineKeyboardButton("What is Consent?", callback_data='learn_consent')],
        [InlineKeyboardButton("About Victim Blaming & Rape Myths", callback_data='learn_victim_blaming')],
        back_button('learn')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text=text, parse_mode='Markdown', reply_markup=reply_markup)


async def learn_sexual_assault(update: Update, context):
    text = (
        "⛔ *Sexual Assault* ⛔\n\n"
        "Sexual assault can include:\n\n"
        "🔹 Any penetration without consent (e.g. vaginal, oral or anal), using any part of the body (penis, fingers) or object.\n"
        "🔹 Any unwanted sexual touching, stroking, kissing, groping, etc.\n"
        "🔹 Unwanted sexual requests, messages or gestures, including electronically, in the workplace or elsewhere.\n"
        "🔹 Being made to view pornography against your will.\n"
        "🔹 Unwanted taking and/or sharing of nude or intimate photographs or videos, e.g. upskirting.\n\n"
        "*If you feel like you or any of your loved ones have experienced something similar, you can find support by clicking on the button below*"
    )
   
    keyboard = [
        [InlineKeyboardButton("Get Support", callback_data='help')],
        back_button('learn_sa'),
        [InlineKeyboardButton("Learn More ➡️", callback_data='learn_sexual_assault2')],
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_sexual_assault2(update: Update, context):
    text = (
        "Sexual assault can leave physical and emotional scars that last a long time. Some victims find that emotional scars never go away. Some possible effects of sexual assault would be: \n\n"
        "*Shame:* thinking they are bad, wrong, dirty, or permanently flawed\n"
        "*Guilt:* blaming themselves for what happened\n"
        "*Denying* or *minimizing* the assault as a coping strategy (eg, \"It wasn't that bad.\" \"It only happened once.\")\n"
        "Struggling to set and reinforce *boundaries* due to the violation that occurred\n\n"
        "Read more [here](https://www.instagram.com/p/CeGFlTGhZ0p/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)"
        )
   
    keyboard = [

        back_button('learn_sexual_assault'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)



async def learn_sexual_grooming(update: Update, context):
    text = (
        "🚫 *Sexual Grooming* 🚫\n\n"
        "Sexual grooming is the process by which a sexual predator cultivates a relationship with a potential victim. Through grooming, the abuser builds trust and an emotional connection to the targeted victim in order to manipulate and abuse them.\n\n"
    )
    keyboard = [
        next_button('learn_sexual_grooming2'),
        back_button('learn_sa'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_sexual_grooming2(update: Update, context):
    text = (
        "🚫 *Sexual Grooming* 🚫\n\n"
        "Sexual grooming can happen to anyone, including adults, but more often towards children as they are more vulnerable.\n"
        "It is the gradual exposure of sexual ideas and thoughts brought into normal conversations.\n"
        "They build trust and an emotional relationship before gradually exposing sexual ideas and thoughts brought into normal conversations, which can also be done online.\n"
        "The purpose being sexual exploitation, gratification or abuse. "
    
    )
    keyboard = [
        next_button('learn_sexual_grooming3'),
        back_button('learn_sexual_grooming'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_sexual_grooming3(update: Update, context):
    text = (
        "🚫 *Sexual Grooming* 🚫\n\n"
        "\"Grooming can also happen in domestic and relationship settings where the abusive partner, over time, introduces abusive acts that you feel coerced into allowing. In these situations, consent is coerced and therefore is not consent.\"\n\n"
        "Read more about [sexual grooming](https://www.instagram.com/p/C5K5s3Qh_vj/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==) or check out [our podcast with Dewy Choo](https://youtu.be/ARb7-qQ10qc?si=8Szp1yQFBVDujj1f)"
    )
    keyboard = [
        back_button('learn_sexual_grooming2'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)


async def learn_consent(update: Update, context):
    text = (
        "🤝 *Consent* 🤝\n\n"
        "Consent is an agreement between participants to engage in sexual activity. It is volatile and can change at any point during the interaction between both parties. You can withdraw consent at any point in time if you feel uncomfortable.\n\n" 
        "When you're engaging in sexual activity, consent communication should happen *every* time for *every* type of activity. Consenting to one activity, at one time does not mean someone gives consent for other activities or for the same activity on other occasions (eg, kissing someone doesn't give them permission to remove your clothes)\n\n"
        "*Click next to learn more*"
    )
    keyboard = [
        next_button('learn_consent2'),
        back_button('learn_sa'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_consent2(update: Update, context):
    text = (
        "🤝 *Consent* 🤝\n\n"
        "Our bodily pleasure during sexual intercourse does not naturally equate to consent by the victim. Physiological responses like an erection, "
        "lubrication, arousal, or orgasm are involuntary, meaning your body might react one way even when you are not consenting to the activity.\n\n" 
        "Read more [here](https://www.instagram.com/p/CfaZQaOB8JU/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)\n"
        
    )
    keyboard = [
        next_button('learn_consent3'),
        back_button('learn_consent'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)



async def learn_consent3(update: Update, context):
    text = (
        "🤝 *Consent* 🤝\n\n"
        "Consent *cannot* be given by:\n\n"
        "🔹 individuals who are underage, intoxicated or incapacitated by drugs or alcohol, or asleep or unconscious.\n"
        "🔹 someone who agrees to an activity under the pressure of intimidation or threat\n"
        "🔹 those in unequal power dynamics (such as engaging in sexual activity with an employee or student)\n\n"
        "Read more about [consent](https://www.instagram.com/p/Ce-L3pNhpYm/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)\n"
        "Read more about [enthusiastic consent](https://www.instagram.com/p/CihJKZuBRZ9/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)")
   
    keyboard = [
        back_button('learn_consent2'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)




async def learn_victim_blaming(update: Update, context):
    text = (
        "❌ *Victim Blaming* ❌\n\n"
        "Victim blaming is common among rape or sexual assault cases, where the victim is accused of inviting the perpetration due to either their clothing or behaviour.")
    keyboard = [
        next_button('learn_victim_blaming2'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_victim_blaming2(update: Update, context):
    text = (
        "❌ *Victim Blaming* ❌\n\n"
        "Blaming the victim makes it more difficult for that person to come forward and report the assault. On a societal level, it means fewer crimes get reported and fewer predators get prosecuted.\n\n"
        "Victim blaming can lead to increased and unnecessary suffering for the victims. They may experience ridicule while at the same time watching their predators avoid punishment instead of getting the justice they deserve.\n\n"
        "This may increase unhelpful emotions like shame and guilt as it delays their healing. It may also add to their toxic self-blame.\n\n"
        "Read more about victim blaming [here](https://www.instagram.com/p/CkArdp3hWKd/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)"
    )
    keyboard = [
        [InlineKeyboardButton("➡️ Rape Myths", callback_data='learn_rape_myths')],
        back_button('learn_victim_blaming'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn_rape_myths(update: Update, context):
    text = (
        "❌ *Rape Myths* ❌\n\n"
        "Rape Myths can also perpetuate victim blaming and discourage survivors from speaking out.\n\n"
        "Rape myths can be in these forms:\n"
        "- Blaming the victim (e.g. \"they should have resisted the attacker more\")\n"
        "- Doubting the allegations (e.g. \"she just regrets having sex with him and is now looking for a way to feel better\")\n"
        "- Excusing the accused's behaviour (e.g. \"he was too drunk to know what he was doing\")\n"
        "- Insists that sexual violence only happens to specific types of people (e.g. \"men don't get raped\").\n\n"
        "Read more about [rape myths](https://www.instagram.com/p/C2jCbS3B7-p/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)"
    )
    keyboard = [
        back_button('learn_victim_blaming2'),
        [InlineKeyboardButton("Main menu 🏠", callback_data='learn')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_journaling_prompts(update: Update, context):
    trigger_warning = (
        "⚠️ *Content Warning* ⚠️\n\n"
        "The following journaling prompts may bring up difficult emotions and memories. "
        "Please take care of yourself and only engage with prompts that feel safe for you. "
        "You can skip any prompt that feels too difficult.\n\n"
    )
    text = (
        "📝 *Journaling Prompts* 📝\n\n"
        "*General prompts:*\n"
        "• How are you feeling today? List down 3 emotions you are currently feeling\n"
        "• What is 1 thing on your mind you want to write about today?\n"
        "• What are 3 things that happened this week? How did it make you feel?\n\n"
        "*Focusing on the assault:*\n"
        "• How do you feel when you recall the assault that happened?\n"
        "• How do you feel about the person that sexually assaulted you?\n\n"
        "*Focusing on being kinder to yourself:*\n"
        "• What is 1 thing about yourself that you love?\n"
        "• What is 1 good thing that happened this week?\n"
        "• What are 3 things you are grateful for today?"
    )
    keyboard = [back_button('care_journaling')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text + trigger_warning, parse_mode='Markdown', reply_markup=reply_markup)

async def care_younger_self(update: Update, context):
    trigger_warning = (
        "⚠️ *Content Warning* ⚠️\n\n"
        "Writing to your younger self can bring up strong emotions and memories. "
        "Please take care of yourself and take breaks if needed. "
        "Remember that you can stop at any time.\n\n"
    )
    text = (
        "✍️ *Letter to my younger self* ✍️\n\n"
        "Writing a letter to your younger self can be incredibly healing. If you are a survivor, "
        "writing a letter to the person you were that had to go through that assault, can be even more healing.\n\n"
        "Write a letter to the person that had to face the assault. What would you say to them? "
        "What would they want to hear when that happened? Do you want to remind them about how strong they were, "
        "about how they did everything they could, about how it was not their fault?\n\n"
        "Write to them. Show them the love you hoped to receive. And that's the love that you will receive as you finish the letter to yourself."
    )
    keyboard = [back_button('care_tips')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(trigger_warning + text, parse_mode='Markdown', reply_markup=reply_markup)
