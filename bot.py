import telebot

bot = telebot.TeleBot("801359509:AAHjuBl_1xRdDHHTTacpT3Q1TSiXl_qQiCw")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def send_welcome(message1):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Сайт Ильи Сергеевича", url="https://illuhakupchenko.github.io")
    markup.add(button)
    bot.send_message(message1.chat.id,
                     '<strong>Приветствую!</strong>\N{Victory Hand}\nЯ первый бот <a href="">'
                     'Ильи Серегеевича</a>, меня зовут <i>Botty3000</i>\N{Robot Face}\n'
                     'На данный момент мой функционал\N{Gear} не очень велик, но создатель '
                     'обещал меня совершенствовать!\N{Flexed Biceps}\n'
                     'Чем я могу вам помочь? Выберите категорию\N{Game Die}', parse_mode="HTML", reply_markup=keyboard1)
    bot.send_photo(message1.chat.id, photo='https://static-ck.okdesk.ru/okdesksite/pictures/115/content_bot.jpg',
                   reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    if message.text.lower() == 'kek':  # lower() - ф-ция для отбора верхнего и нижнего регистров
        msg = 'dro4'
        bot.send_sticker(message.chat.id, 'CAADAgAD0gEAAiUDUg-5ImyW6RwdWAI')
    elif message.text.lower() == 'lol':
        msg = 'kekun'
    else:
        msg = 'nitonito'

    bot.send_message(message.chat.id, msg)


bot.polling(none_stop=True)
