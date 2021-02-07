import sys
import telegram
import time
from multiprocessing import Process, Value, Array
from PyQt5.QtWidgets import *
from KK1StockSupportBot import KK1StockSupportBot
from KK1StockAPI import KK1StockAPI


def callback_help_command(update: telegram.Update, context):
    reply_text = str()
    reply_text += "☆ 현재 명령어는 다음과 같이 구현되어 있습니다.\n"
    reply_text += "└ /help: 명령어 리스트를 출력한다.\n"

    # event_handler = 'help'

    update.message.reply_text(reply_text)


def run_stock_api(token: str, event_handler: Value):
    app = QApplication(sys.argv)
    stock_api = KK1StockAPI(token)
    stock_api.show()
    # app.exec_() # QT UI 이벤트를 사용할 것은 아니기 때문에 필요없음.
    count = 1
    while True:
        time.sleep(0.5)
        # stock_api.sendMessage("Test message " + str(count))
        # count += 1

        # if event_handler:
        #     print(event_handler)
        #     event_handler = None


def run_telegram_bot(token: str, event_handler: Value):
    telegram_bot = KK1StockSupportBot(token)
    telegram_bot.add_command_handler('help', callback_help_command)
    telegram_bot.run()


def run_kk1_stock_supporter():
    with open("D:/Projects/KK1StockSupporter/KK1StockSupport_bot.token") as file:
        my_token = file.readline()

    # 공유 자원을 이벤트 핸들러로 활용한다.
    # updater 에서는 들어오는 명령어를 받아 event_handler 를 통해 주식 api 에게 전달
    # 주식 api 는 받은 명령을 수행하고 수행 결과를 send
    # 주식 api 는 지속적으로 시장을 체크해서 특정 조건에 message send
    event_handler = Value('i', 0)
    stock_api_process = Process(target=run_stock_api, args=(my_token, event_handler))
    telegram_updater_process = Process(target=run_telegram_bot, args=(my_token, event_handler))

    stock_api_process.start()
    telegram_updater_process.start()

    stock_api_process.join()
    telegram_updater_process.join()


if __name__ == '__main__':
    run_kk1_stock_supporter()
