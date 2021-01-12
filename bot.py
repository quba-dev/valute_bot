import telebot
from telebot import types
from parser import main

bot = telebot.TeleBot('1458572220:AAEbMXbbuc6siF23SzvIRVwwfiISPzSHFlU')


keyboard2 = types.InlineKeyboardMarkup(row_width=2)
usa2 = types.InlineKeyboardButton('USA', callback_data='USA_BUY')
euro2 = types.InlineKeyboardButton('EURO', callback_data='EURO_BUY')
rub2 = types.InlineKeyboardButton('RUB', callback_data='RUB_BUY')
tenge2 = types.InlineKeyboardButton('TENGE', callback_data='TENGE_BUY')
back = types.InlineKeyboardButton('НАЗАД', callback_data='BACK')
keyboard2.add(usa2,euro2,rub2,tenge2,back)



keyboard1 = types.InlineKeyboardMarkup(row_width=2)
usa = types.InlineKeyboardButton('USA', callback_data='USA_SELL')
euro = types.InlineKeyboardButton('EURO', callback_data='EURO_SELL')
rub = types.InlineKeyboardButton('RUB', callback_data='RUB_SELL')
tenge = types.InlineKeyboardButton('TENGE', callback_data='TENGE_SELL')
back = types.InlineKeyboardButton('НАЗАД', callback_data='BACK')
keyboard1.add(usa,euro,rub,tenge,back)


keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton('Продажа', callback_data='Sell')
btn2 = types.InlineKeyboardButton('Покупка', callback_data='Buy')
quit_ = types.InlineKeyboardButton('ВЫХОД', callback_data='QUIT_')
keyboard.add(btn1,btn2,quit_)


@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет, это курс-валютный ботяра.\nБудем брать курс с www.valuta.kg \nВыберите вариант: ', reply_markup=keyboard)


@bot.callback_query_handler(lambda call: True)
def call_data(call):
    chat_id = call.message.chat.id


    if call.data == 'USA_SELL':
        bot.edit_message_text(text=f"Курс доллара на продажу: {main()[1]} ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'EURO_SELL':
        bot.edit_message_text(text=f"Курс евро на продажу: {main()[3]} ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'RUB_SELL':
        bot.edit_message_text(text=f"Курс рубля на продажу: {main()[5]} ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'TENGE_SELL':
        bot.edit_message_text(text=f"Курс тенге на продажу: {main()[7]} ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'BACK':
        bot.edit_message_text(text="Выберите действие: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'Buy':
        bot.edit_message_text(text="Список валюты на покупку: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard2)

    if call.data == 'Sell':
        bot.edit_message_text(text="Список валюты на продажу: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard1)

    if call.data == 'QUIT_':
        bot.edit_message_text(text="Досвидули", message_id=call.message.message_id, chat_id=chat_id)

    if call.data == 'USA_BUY':
        bot.edit_message_text(text=f"Курс доллара на покупку: {main()[0]} ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'EURO_BUY':
        bot.edit_message_text(text=f"Курс евро на покупку: {main()[2]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'RUB_BUY':
        bot.edit_message_text(text=f"Курс рубля на покупку: {main()[4]} ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

    if call.data == 'TENGE_BUY':
        bot.edit_message_text(text=f"Курс тенге на покупку: {main()[6]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)


bot.polling()