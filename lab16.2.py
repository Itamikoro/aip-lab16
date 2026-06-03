import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui2 import Ui_MainWindow


class tabl(QtWidgets.QMainWindow):
    def __init__(self):
        super(tabl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sum = 1
        self.flag = False
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Таблица умножения')
        self.ui.lineEdit.setPlaceholderText('Итого')
        self.ui.btn1.clicked.connect(self.digital_button_clicked)
        self.ui.btn2.clicked.connect(self.digital_button_clicked)
        self.ui.btn3.clicked.connect(self.digital_button_clicked)
        self.ui.btn4.clicked.connect(self.digital_button_clicked)
        self.ui.btn5.clicked.connect(self.digital_button_clicked)
        self.ui.btn6.clicked.connect(self.digital_button_clicked)
        self.ui.btn7.clicked.connect(self.digital_button_clicked)
        self.ui.btn8.clicked.connect(self.digital_button_clicked)
        self.ui.btn1_9.clicked.connect(self.digital_button_clicked)
        self.ui.pushButton.clicked.connect(self.result)
        self.ui.pushButton_2.clicked.connect(self.clear_all)

    def digital_button_clicked(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        current_text = self.ui.lineEdit.text()
        self.sum *= int(button_text)
        if self.flag:
            self.ui.lineEdit.setText(current_text + "*" + button_text)
        else:
            self.ui.lineEdit.setText(current_text + button_text + '*')


    def result(self):
        self.flag = True
        self.ui.lineEdit.setText(str(self.sum))

    def clear_all(self):
        self.ui.lineEdit.clear()
        self.sum = 1
        self.flag = False
        self.ui.lineEdit.setPlaceholderText('Итого')

app = QtWidgets.QApplication([])
application =  tabl()
application.show()


sys.exit(app.exec())