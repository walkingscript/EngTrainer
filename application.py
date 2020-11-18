import sys

from PyQt5 import QtWidgets

from gui import Ui_MainWindow
from match_maker import MatchMaker
from settings import stylesheets
from stats import Statistics


class Application(Ui_MainWindow):
    """Main Class Application"""
    def __init__(self):     
        self.__match_maker = MatchMaker()
        self.__stats = Statistics()
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__MainWindow = QtWidgets.QMainWindow()
        super().__init__()   
        super().setupUi(self.__MainWindow)
        self.__init_logic()
        self.__display_round()
        self.__display_stats()

    def start(self):
        self.__MainWindow.show()
        sys.exit(self.__app.exec_())

    def __init_logic(self):
        '''Connects every button with an action.'''
        self.__answer_buttons = (self.btn_answer_1, self.btn_answer_2, 
                                 self.btn_answer_3, self.btn_answer_4,)
        for btn in self.__answer_buttons:
            btn.clicked.connect(self.__give_answer)
        self.btn_next_round.clicked.connect(self.__next_round)
        self.menu_item_change_mode.changed.connect(self.__change_mode)
        self.__can_answer = True

    def __change_mode(self):
        if self.menu_item_change_mode.isChecked():
            self.__match_maker = MatchMaker(lang='ru')
        else:
            self.__match_maker = MatchMaker(lang='en')
        self.__next_round()

    def __display_stats(self):
        data = self.__stats.get_stats()
        msg = f"Username: {self.__stats.get_username()} | " \
              f"Answers: {data['total_answers']} | " \
              f"Right: {data['right_answers']} ({data['right_percent']}%) | " \
              f"Wrong: {data['wrong_answers']}"
        self.statusbar.showMessage(msg)

    def __next_round(self):
        self.btn_next_round.setEnabled(False)
        self.__reset_answer_buttons_styles()
        self.__display_round()
        self.__can_answer = True

    def __reset_answer_buttons_styles(self):
        for btn in self.__answer_buttons:
            btn.setEnabled(True)
            btn.setStyleSheet(stylesheets['default'])

    def __display_round(self):
        self.round_data = self.__match_maker.make_set()
        self.lbl_question.setText(self.round_data.question)
        for i, btn in enumerate(self.__answer_buttons):
            btn.setText(self.round_data.guesses[i])

    def __give_answer(self):
        if not self.__can_answer:
            return
        btn = self.__MainWindow.sender()
        answer = btn.text()
        if self.__is_right_answer(answer):
            self.__stats.add_right_answer()
            btn.setStyleSheet(stylesheets['right_answer'])
        else:
            self.__stats.add_wrong_answer()
            btn.setStyleSheet(stylesheets['wrong_answer'])
            self.__answer_buttons[self.round_data.right_answer].setStyleSheet(
                stylesheets['right_answer']
            )
        self.btn_next_round.setEnabled(True)
        self.__can_answer = False
        self.__display_stats()

    def __is_right_answer(self, answer):
        if answer == self.round_data.guesses[self.round_data.right_answer]:
            return True
