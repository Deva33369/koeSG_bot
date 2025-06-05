from telegram import InlineKeyboardButton

def back_button(target='start'):
    return [InlineKeyboardButton("🔙 Back", callback_data=target)]

def next_button(target='start'):
    return [InlineKeyboardButton("➡️ Next",callback_data=target)]