import telebot
import configure

client = telebot.TeleBot(configure.config['token'])

@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text.lower() == 'hello!':
        client.send.message(message.chat.id, 'hello!')
        
client.polling(none_stop = True, interval = 0)
