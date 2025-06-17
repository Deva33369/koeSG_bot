from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from handlers.utils import back_button
import random
import os
from handlers.support_handler import support

async def care(update: Update, context):
    text = (
        "💖 *Self-Care & Healing* 💖\n\n"
        "Thank you for staying, for trying and for taking the step to be there for YOU. "
        "Recognising that what happened was not your fault is crucial and taking the steps towards being kinder to yourself is important. "
        "How would you like to heal?"
    )
    keyboard = [
        [InlineKeyboardButton("Share Your Story", callback_data='care_story')],
        [InlineKeyboardButton("Support Groups", callback_data='care_support_groups')],
        [InlineKeyboardButton("Self Care Tips", callback_data='care_tips')],
        [InlineKeyboardButton("Other Support & Resources", callback_data='support')],
        [InlineKeyboardButton("Helplines", callback_data='care_helplines')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_story(update: Update, context):
    text = (
        "📝 *Share Your Story* 📝\n\n"
        "Sharing your story and speaking out is a great way to heal and move forward. "
        "When we share our stories with others, not only are we able to finally lift a weight off our shoulders, "
        "but we also remind ourselves and others that we are not alone.\n\n"
        "KOE builds our platform on amplifying voices of sexual assault survivors and we hope that by sharing each other's stories, "
        "we can allow others to share their voice, build their confidence as well as form a community of shared understanding and care for one another.\n\n"
        "*Note:* By sharing your story via this bot, you are consenting to KOE using this story for publicity purposes via our telegram channel or via instagram. "
        "Your identity and your story will remain anonymous even to the admin.\n\n"
        "Please type your story below:"
    )
    keyboard = [back_button('care')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)
    context.user_data['expecting_story'] = True

async def care_support_groups(update: Update, context):
    text = (
        "👥 *Support Groups* 👥\n\n"
        "Support groups can be very useful. We hope for any survivor that would like to join our support groups "
        "to be able to share freely, without judgement, and find themselves in a space where others can understand and relate to them.\n\n"
        "Support groups can be beneficial, where it has been proven to support in increasing our ability to process our emotions and trauma, "
        "reduce isolation, and overall improve interpersonal well-being.\n\n"
        "*Note:* Our support groups are peer-led and are not therapy/counselling sessions. We hope to provide a safe space for sharing to all survivors "
        "but we also welcome you to approach any of the free counselling/therapy services provided in Singapore for survivors."
    )
    keyboard = [
        [InlineKeyboardButton("Join our support group", callback_data='care_join_group')],
        [InlineKeyboardButton("Counselling Resources", callback_data='care_counselling')],
        back_button('care')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_tips(update: Update, context):
    text = (
        "💡 *Self Care Tips* 💡\n\n"
        "Self care might seem straightforward or common sense, but do we actually practise it? "
        "We have a few self care tips that we would like to share that might help you."
    )
    keyboard = [
        [InlineKeyboardButton("Journaling", callback_data='care_journaling')],
        [InlineKeyboardButton("Grounding Techniques", callback_data='care_grounding')],
        [InlineKeyboardButton("Crochet Workshops", callback_data='care_crochet')],
        [InlineKeyboardButton("Encouragement Letters", callback_data='care_letters')],
        [InlineKeyboardButton("Letter to my younger self", callback_data='care_younger_self')],
        back_button('care')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_journaling(update: Update, context):
    text = (
        "📔 *Journaling* 📔\n\n"
        "Journaling can be an effective way to process your thoughts, feelings and experience. "
        "The human mind can work in mysterious ways, where it can become common to suppress or misremember what happened, "
        "or what we felt. Journaling allows us to write how we feel freely with no judgement, and when we keep doing it, "
        "we might one day also process and heal from what has happened as well as reframe our mindsets into being kinder to ourselves.\n\n"
        "Grab an empty book or paper and a pen and let's write down what's in our mind. "
        "Or if you would like some prompts, feel free to request for some below."
    )
    keyboard = [
        [InlineKeyboardButton("I would like some prompts", callback_data='care_journaling_prompts')],
        back_button('care_tips')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_journaling_prompts(update: Update, context):
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
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_grounding(update: Update, context):
    text = (
        "🌱 *Grounding Techniques* 🌱\n\n"
        "Grounding methods are useful in helping to gain a sense of stability especially in overwhelming, "
        "anxiety-inducing or stressful moments. Try this technique in a quiet and safe environment:\n\n"
        "1. *5 things you see* - Look around and name 5 things you can see\n"
        "2. *4 things you can touch* - Name 4 things you can touch\n"
        "3. *3 sounds you can hear* - Listen for 3 distinct sounds\n"
        "4. *2 things you can smell* - Identify 2 different smells\n"
        "5. *1 thing you can taste* - Focus on 1 thing you can taste\n\n"
        "Take your time with each step. This technique can help during anxiety or panic attacks."
    )
    keyboard = [back_button('care_tips')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_letters(update: Update, context):
    # Get a random encouragement image
    images_folder = "images"
    encouragement_images = [f for f in os.listdir(images_folder) if f.startswith("encourage_mess") and f.endswith(".jpg")]
    
    if encouragement_images:
        random_image = random.choice(encouragement_images)
        image_path = os.path.join(images_folder, random_image)
        
        # Send the image with caption
        with open(image_path, 'rb') as photo:
            await update.callback_query.message.reply_photo(
                photo=photo,
                caption="💌 *Encouragement Letters* 💌\n\nHere are some letters from the public for survivors of sexual assault! We hope that these letters will serve as a reminder and as an encouragement, that we are here with you.",
                parse_mode='Markdown'
            )
        
        # Edit the original message to show the button options
        text = "💌 *Encouragement Letters* 💌\n\nHere's an encouragement letter for you! 💖"
        keyboard = [
            [InlineKeyboardButton("Send another letter", callback_data='care_letters')],
            back_button('care_tips')
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)
    else:
        # Fallback if no images found
        text = (
            "💌 *Encouragement Letters* 💌\n\n"
            "Here are some letters from the public for survivors of sexual assault! "
            "We hope that these letters will serve as a reminder and as an encouragement, that we are here with you."
        )
        keyboard = [
            [InlineKeyboardButton("Send another letter", callback_data='care_letters')],
            back_button('care_tips')
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_younger_self(update: Update, context):
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
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care_resources(update: Update, context):
    await support(update, context)