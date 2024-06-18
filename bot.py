import telebot
from token import TOKEN

BOT = telebot.TeleBot(TOKEN)

@BOT.message_handler(commands=['start'])
def debug(msg):
    BOT.send_message(msg.chat.id, f"{msg.from_user.first_name}, Добро пожаловать в GigaChat бота!\n"
                                       "Здесь вы можете задать любой вопрос и бот на него ответит\n"
                                       "Пока что бот способен отвечать только на текстовые запросы! Приятного использования)\n")


@BOT.message_handler(content_types=['photo', 'video', 'audio', 'document', 'sticker',
                                    'location', 'contact', 'voice', 'video_note',
                                    'animation', 'game', 'poll', 'dice'])
def missing_type(msg):
    BOT.send_message(msg.chat.id, "Пока что я могу обрабатывать только текст :'( ")


@BOT.message_handler(commands=['own'])
def start(msg):
    BOT.send_message(msg.chat.id,
                f"Привет, я Дима Вакуленко и это мой пробный телеграмм ROG_bot, "
                     "который использует API GigaChat'a для обработки запросов\n"
                     "Если заинтеросовал мой проект, можете заглянуть его реализацию на github"
                     " - https://github.com/vakulenk0")

@BOT.message_handler(commands=['debug'])
def debug(msg):
    BOT.send_message(msg.chat.id, msg)


@BOT.message_handler(commands=['help'])
def help(msg):
    BOT.send_message(msg.chat.id, "Помогай себе сам!!!")


@BOT.message_handler()
def request(msg):
    BOT.send_message(msg.chat.id, "Помогай себе сам!!!")

BOT.polling()
