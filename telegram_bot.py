import telebot

"""Exercise 2: String Methods Using Bot

Objective:
    1. Create a bot that will convert the text to uppercase
    2. Check if the text contains prohibited words
    3. If the text contains prohibited words, delete the message
    4. If the text does not contain prohibited words, convert the text to uppercase and reply to the user

Hints:
    1. Figure how to change "nama saya rahman" to -> ["nama", "saya", "rahman"]
    2. Figure out how to check if the text contains prohibited words using set intersection
    3. Use If Else statement to manage, Example: -
        if check_text_message(text) == True:
            reply_message(message, "Please don't use prohibited words!")
            delete_message(message)
        else:
            reply_message(message, text.upper())

"""

API_KEY = '7311222613:AAGCZXox2vbXy0vzs_1VsJJJlSc-VFf-qfY' #This is not the best practice!
bot = telebot.TeleBot(API_KEY)


PROHIBITED_WORDS = {'dap', 'pas', 'pkr', 'umno', 'barisan nasional', 'pakatan harapan'}

def start(message):
    bot.reply_to(message, "Send me any text, and I'll convert it to uppercase!")

def delete_message(message):
    bot.delete_message(message.chat.id, message.message_id)

def reply_message(message, reply_message):
    bot.reply_to(message, reply_message)


# Register a handler for all text messages
def handle_text_messages(message):
    """Accept a message class as parameter

    Args:
        message (telebot.types.Message): A message class from telebot library
    
    Action:
        1. Get the text from the message
        2. Check if the text contains prohibited words
        3. If it contains prohibited words, delete the message
        4. If it does not contain prohibited words, convert the text to uppercase and reply to the user
    
    How To Use:
        1. Delete Message - delete_message(message)
        2. Reply Message - reply_message(message, reply_message)
    """
    text = message.text
    text = set(text.split())

    check_intersect = PROHIBITED_WORDS.intersection(text)
    

    if text == "Teh o beng":
        reply_message(message, text)
    else:
        delete_message(message)


    
# Register command handler
bot.message_handler(commands=['start'])(start)
bot.message_handler(content_types=['text'])(handle_text_messages)
print("Bot is running....")
bot.polling(none_stop=True)
