import telebot

bot = telebot.TeleBot("801359509:AAHjuBl_1xRdDHHTTacpT3Q1TSiXl_qQiCw")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message1):
    bot.send_message(message1.chat.id, '<strong>Приветствую!</strong>\N{Victory Hand}\nЯ первый бот <a href="https://illuhakupchenko.github.io">'
									   'Ильи Серегеевича</a>, меня зовут Botty3000\N{Clown Face}\n'
                                       'На данный момент мой функционал\N{Gear} не очень велик, но создатель '
                                       'обещал меня совершенствовать в дальнейшем!\N{Game Die}', parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    if message.text == 'kek':
        msg = 'dro4'
    elif message.text == 'lol':
        msg = 'kekun'
    else:
        msg = 'nitonito'

    bot.send_message(message.chat.id, msg)


bot.polling(none_stop=True)

