import telebot
import os
import random

TOKEN = os.environ.get('TOKEN', 'значение не найдено')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id
    response = "Hello, World!"
    bot.send_message(chat_id, response)

@bot.message_handler(commands=['who'])
def made_by(message):
    chat_id = message.chat.id
    response = 'Авторы: команда "Аферисты в облаках"! '
    bot.send_message(chat_id, response)

@bot.message_handler(commands=['meme'])
def send_mem(message):
    memes = ['https://clck.ru/36V82B', 'https://clck.ru/36V885', 'https://clck.ru/36V8Dp']
    numbMeme = random.randint(0, 2)
    chat_id = message.chat.id
    response = f'Держи мемчик {memes[numbMeme]}'
    bot.send_message(chat_id, response)

@bot.message_handler(commands=['info'])
def send_info(message):
    chat_id = message.chat.id
    response = ('/who - авторы \n'
                '/meme - мемы \n')
    bot.send_message(chat_id, response)


if __name__ == "__main__":
    bot.polling(none_stop=True)