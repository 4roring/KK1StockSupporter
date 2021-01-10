import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters


def get_message(update: telegram.Update, context):
    update.message.reply_text(update.message.text)


class KK1StockSupportBot:
    def __init__(self, token: str):
        self.token = token
        self.updater = Updater(token, use_context=True)
        message_handler = MessageHandler(Filters.text & (~Filters.command), get_message)
        self.updater.dispatcher.add_handler(message_handler)

    def add_command_handler(self, command: str, call_back):
        # 텍스트에는 응답하지만 커맨드가 있으면 응답하지 않도록 설정한 것
        command_handler = CommandHandler(command, call_back)
        self.updater.dispatcher.add_handler(command_handler)

    def run(self):
        self.updater.start_polling(timeout=3, clean=True)
        self.updater.idle()
