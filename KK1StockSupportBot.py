import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from multiprocessing import Value


def get_message(update: telegram.Update, context, event_handler: Value):
    update.message.reply_text(update.message.text)


# 텔레그램 봇. 주식 API 쪽에서 Sender 역활을 하고 별도로 Updater 역활을 하는 쪽 두개의 객체를 생성해서 활용 예정.
class KK1StockSupportBot:
    def __init__(self, token: str):
        self.token = token
        self.updater = Updater(token, use_context=True)
        message_handler = MessageHandler(Filters.text & (~Filters.command), get_message)
        self.updater.dispatcher.add_handler(message_handler)

    def __del__(self):
        self.updater.bot.sendMessage(456096060, '봇이 종료되었습니다. 다음 시작에 /init 을 수행해주세요.')

    def add_command_handler(self, command: str, call_back):
        # 텍스트에는 응답하지만 커맨드가 있으면 응답하지 않도록 설정한 것
        command_handler = CommandHandler(command, call_back)
        self.updater.dispatcher.add_handler(command_handler)

    def SendMessage(self, message: str):
        self.updater.bot.sendMessage(456096060, message)

    def run(self):
        print('Run KK1 Stock Support Bot')
        self.updater.start_polling(timeout=3, clean=True)
        self.updater.idle()
