import telebot

bot = telebot.TeleBot('541655424:AAGUWiMN3X7iduYNBZVBQ6KQtzb2m0suU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello</b>', parse_mode='html')
    
bot.polling(none_stop=True)
    