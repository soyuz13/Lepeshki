import telebot
import flask
import logging
import time
import pprint
import datetime
from image_recognizing import Entera

TLG_TOKEN = '919957510:AAE06b_5cqcOATruVxCdRx0tGFeM9QNFK8U'
APP_HOST = '127.0.0.1'
APP_PORT = 8444
WEBHOOK_URL = 'https://ad93-95-154-69-12.jp.ngrok.io'

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(TLG_TOKEN)
app = flask.Flask(__name__)


def get_recognized_doc(file_path, message):
    entera = Entera()
    entera.start()
    entera.send_photo(file_path)
    text = entera.parse_doc()
    print(f'Отправлено пользователю: {message.from_user.first_name}')
    bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, message)


@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    new_filename = 'Photo ' + str(datetime.datetime.today()).split('.')[0] + '.jpg'
    with open(new_filename, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фото взято во обработку, 3-5 мин.")
    print(f'Пришло фото от {message.from_user.first_name}')
    get_recognized_doc(new_filename, message)


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, 'Ждем отправки фото для распознавания :)')
    print(f'{message.from_user.first_name} пишет')


@app.route('/', methods=['POST'])
def webhook():
    # bot.send_message('192752787', flask.request.headers.get('content-type'))
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        pprint.pprint(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


if __name__ == '__main__':
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
