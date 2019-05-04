import telebot

BOT_TOKEN = '801359509:AAHjuBl_1xRdDHHTTacpT3Q1TSiXl_qQiCw'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	if message.text == 'kek':
		msg = 'dro4'
	elif message.text == 'lol':
		msg = 'kekun'
	else:
		msg = 'nitonito'

	bot.send_message(message.chat.id, msg)

bot.polling( none_stop = True)
