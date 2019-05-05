import telebot

bot = telebot.TeleBot("801359509:AAHjuBl_1xRdDHHTTacpT3Q1TSiXl_qQiCw")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message1):
    bot.send_message(message1.chat.id, '<strong>Приветствую!</strong>\N{Victory Hand}\nЯ первый бот <a href="https://illuhakupchenko.github.io">'
									   'Ильи Серегеевича</a>, меня зовут Botty3000\N{Clown Face}\n'
                                       'На данный момент мой фунционал\N{Gear} не очень велик, но мой создатель '
                                       'пообещал меня совершенствовать!\N{Game Die}', parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    if message.text == 'kek':
        msg = 'dro4'
    elif message.text == 'lol':
        msg = 'kekun'
    else:
        msg = 'nitonito'

    bot.send_message(message.chat.id, '<a href="https://drive.google.com/open?id=19_EeOIOKIlBpIf8h-n3-qoXaOb-3ZxS6">hello</a>', parse_mode="HTML")


bot.polling(none_stop=True)

