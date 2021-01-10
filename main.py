import telegram
from KK1StockSupportBot import KK1StockSupportBot


def callback_help_command(update: telegram.Update, context):
    reply_text = str()
    reply_text += "☆ 현재 명령어는 다음과 같이 구현되어 있습니다.\n"
    reply_text += "└ /help: 명령어 리스트를 출력한다.\n"

    update.message.reply_text(reply_text)


def run_kk1_stock_supporter():
    with open("D:/Projects/KK1StockSupporter/KK1StockSupport_bot.token") as file:
        my_token = file.readline()

    telegram_bot = KK1StockSupportBot(my_token)
    telegram_bot.add_command_handler('help', callback_help_command)
    telegram_bot.run()


if __name__ == '__main__':
    run_kk1_stock_supporter()
