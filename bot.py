import telebot
from DATA import TOKEN
from DATA import AUTH_DATA
from gigachat import GigaChat

BOT = telebot.TeleBot(TOKEN)

@BOT.message_handler(commands=['start'])
def debug(msg):
    BOT.send_message(msg.chat.id, f'''Привет, {msg.from_user.first_name}, меня зовут Дима Вакуленко, это мой бот помощник
Если вам потребуется быстро найти какую-нибудь информацию в интернете, просто спросите бота и он быстро и доступно её сформулирует для вас
Вся необходимая информация есть по команде /help
Приятного пользования!
Мой github - https://github.com/vakulenk0''')


@BOT.message_handler(content_types=['photo', 'video', 'audio', 'document', 'sticker',
                                    'location', 'contact', 'voice', 'video_note',
                                    'animation', 'game', 'poll', 'dice'])
def missing_type(msg):
    BOT.send_message(msg.chat.id, "Пока что я могу обрабатывать только текст :'( ")


@BOT.message_handler(commands=['help'])
def help(msg):
    BOT.send_message(msg.chat.id, '''Основные команды бота:
/start - основная информация
/help - помощь по командам''')


@BOT.message_handler()
def request(msg):
    BOT.send_message(msg.chat.id, "GigaChat генерирует ответ...")
    with GigaChat(credentials=AUTH_DATA, verify_ssl_certs=False) as giga:
        response = giga.chat(f"{msg.text}")
        # print(response.choices[0].message.content)
    BOT.send_message(msg.chat.id, response.choices[0].message.content)

BOT.polling()
