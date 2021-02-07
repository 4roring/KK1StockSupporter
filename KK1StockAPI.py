from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from KK1StockSupportBot import KK1StockSupportBot
from multiprocessing import Value


class KK1StockAPI(QMainWindow):
    def __init__(self, token: str):
        super().__init__()
        # self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        # self.kiwoom.dynamicCall("CommConnect()")
        self.num = 0
        # if self.kiwoom.dynamicCall("CommConnect()"):
        #     print('connected')
        # else:
        #     print('not connected')
        self.bot_sender = KK1StockSupportBot(token)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("API Test")

        btn_test = QPushButton("Send Chat Bot", self)
        btn_test.move(20, 20)
        btn_test.clicked.connect(self.onClicked)

    def onClicked(self):
        QMessageBox.about(self, "message", "clicked")

    def sendMessage(self, message):
        self.bot_sender.SendMessage(message)

    def Print(self, num: int) -> None:
        self.num = num
        print(self.num)
