import sys
import ex
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic


# 한글 시험
class test(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("test.ui", self)
        self.value = ex.excel()

        self.kor.setText(f'{self.value[1]}')

        self.show()

    def enter(self):
        text = self.lineEdit.text()

        if text == self.value[0]:
            self.value = ex.excel()
            self.kor.setText(f'{self.value[1]}')
            self.lineEdit.clear()

    # def reset(self):
    #     self.value = ex.excel()
    #     self.kor.setText(f'{self.value[0]}')
    #     self.lineEdit.clear()

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