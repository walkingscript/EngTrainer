import sys

from PyQt5 import QtWidgets

from gui import Ui_MainWindow


class Application(Ui_MainWindow):
    """Main Class Application"""
    def __init__(self):     
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = super().__init__()   
        self.ui = super().setupUi(self.MainWindow)

        self.btn_answer_1.clicked.connect(self.test)     

    def start(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def test(self):
        print(self.label.text())