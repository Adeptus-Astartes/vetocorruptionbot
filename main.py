import telebot
from telebot import types

TOKEN = "1481737673:AAFBQWs3GoNm0EPxAZXbOlcN7jGEMJjnuYQ"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    how_report = types.KeyboardButton(text="Як повідомити про корупцію")
    contacts = types.KeyboardButton(text="Куди звернутись")
    keyboard.add(how_report, contacts)
    bot.send_message(
        message.chat.id,
        "Доброго дня, ви стали свідком корупції і бажаєте повідомити про неї?",
        reply_markup=keyboard
    )


@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    if text == 'Як повідомити про корупцію':
        file = open('how_to_report.md', 'r')
        data = file.read()
        bot.send_message(message.chat.id, data, parse_mode='Markdown')

    if text == "Куди звернутись":
        keyboard = types.InlineKeyboardMarkup(
            row_width=2
        )

        nazk = types.InlineKeyboardButton(text="НАЗК", callback_data="nazk")
        nabu = types.InlineKeyboardButton(text="НАБУ", callback_data="nabu")
        gpu = types.InlineKeyboardButton(text="ГПУ", callback_data="gpu")
        sbu = types.InlineKeyboardButton(text="СБУ", callback_data="sbu")
        vaks = types.InlineKeyboardButton(text="ВАКС", callback_data="vaks")
        vrp = types.InlineKeyboardButton(text="ВРП", callback_data="vrp")

        keyboard.add(nazk, nabu, gpu, sbu, vaks, vrp)
        bot.send_message(
            message.chat.id,
            "Оберіть орган у який ви хочете звернутись",
            reply_markup=keyboard
        )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'nazk':
        file = open('contacts_nazk.txt', 'r')
        bot.send_message(call.message.chat.id, file.read())
    elif call.data == 'nabu':
        file = open('contacts_nabu.txt', 'r')
        bot.send_message(call.message.chat.id, file.read())
    elif call.data == 'gpu':
        file = open('contacts_gpu.txt', 'r')
        bot.send_message(call.message.chat.id, file.read())
    elif call.data == 'sbu':
        file = open('contacts_sbu.txt', 'r')
        bot.send_message(call.message.chat.id, file.read())
    elif call.data == 'vaks':
        file = open('contacts_vaks.txt', 'r')
        bot.send_message(call.message.chat.id, file.read())
    elif call.data == 'vrp':
        file = open('contacts_vrp.txt', 'r')
        bot.send_message(call.message.chat.id, file.read())


bot.polling()
