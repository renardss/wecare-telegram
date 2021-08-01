import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔖Products")
    item2 = types.KeyboardButton("🛩Shipping")
    item3 = types.KeyboardButton("💶Payment")
    item4 = types.KeyboardButton("👨‍⚕Services")
    item5 = types.KeyboardButton("🔄Refund")
 
    markup.add(item1, item2, item3, item4, item5)
 
    bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nHow can I help you out today?".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🇬🇧 English':
            bot.send_message(message.chat.id, 'Great! How can I help you out today?')
        elif message.text == '🇱🇹 Lietuvių':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Puiku! Kaip aš galiu tau padėti šiandien?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Sorry, I didn't really get this🤔Can you rephrase?")
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)