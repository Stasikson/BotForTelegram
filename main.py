import telebot
from telebot import types

TOKEN = '6513379605:AAF8GcAIkoXD0wFKfxNwJfQrvh_ITddhdhk'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)




