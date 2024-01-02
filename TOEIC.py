import sys
import ex
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt

# 오답 노트
class No_Answer(QDialog):
    def __init__(self, No_Answer):

        super().__init__()
        self.ui = uic.loadUi("NoAnswer.ui", self)

        text_to_display = '\n'.join(map(str, No_Answer))
        self.label.setText(f'{text_to_display}')
        self.show()

# 한글 시험
class test(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("test.ui", self)
        self.value = ex.excel()
        self.score_ = 0
        self.No_Answer = []

        self.score.setText(f'{self.score_}')
        self.kor.setText(f'{self.value[1]}')


        self.show()

    def enter_eng(self):
        text = self.lineEdit.text()

        if text == self.value[0]:
            self.value = ex.excel()
            self.kor.setText(f'{self.value[1]}')
            self.label.setStyleSheet('color: blue;')
            self.label.setText(f'맞았습니다.')
            self.score_ += 1
            self.score.setText(f'{self.score_}')

            self.lineEdit.clear()
            

        else:
            self.label.setStyleSheet('color: red;')
            self.label.setText(f'틀렸습니다.')
            self.lineEdit.clear()

    def next_eng(self):
        self.No_Answer.append(self.value)
        self.value = ex.excel()
        self.kor.setText(f'{self.value[1]}')
        self.lineEdit.clear()
        self.label.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            pass

    def Answer(self):
        self.w = No_Answer(self.No_Answer)
        self.w.show()

# 연습
class train(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("train.ui", self)
        self.value = ex.excel()

        self.eng.setText(f'{self.value[0]}')
        self.kor.setText(f'{self.value[1]}')

        self.show()

    def enter(self):
        text = self.lineEdit.text()

        if text == self.value[0]:
            self.value = ex.excel()
            self.eng.setText(f'{self.value[0]}')
            self.kor.setText(f'{self.value[1]}')
            self.label.setStyleSheet('color: blue;')
            self.label.setText(f'맞았습니다.')
            self.lineEdit.clear()

        else:
            self.label.setStyleSheet('color: red;')
            self.label.setText(f'틀렸습니다.')
            self.lineEdit.clear()




# 첫번째 화면
class first(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("first.ui", self)

    def train(self):
        self.w = train()
        self.w.show()

    def test(self):
        self.w = test()
        self.w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = first()
    window.show()
    sys.exit(app.exec_())