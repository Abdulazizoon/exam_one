import telebot

TOKEN = "2134765912:AAFXwtrnu9Pr3TMQFiVnMzQHb-fOFKEVUcU"

bot = telebot.TeleBot(TOKEN)

lst = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(content_types=['text'])
def send_text(message):
    count = 0
    for i in message.text:
        if i in lst:
            count += 1

    bot.send_message(message.chat.id, count)


bot.polling(none_stop=True)
