from PyQt6.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QPushButton


class MyWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setGeometry(1400, 300, 600, 160)
        self.btn_dialog = QPushButton(self)
        self.btn_dialog.setText("Диалог")
        self.btn_dialog.setToolTip("Эта кнопка вызывает диалоговое окно")
        self.btn_dialog.setGeometry(100, 10, 100, 30)

        self.btn_massage = QPushButton("Текстовая", self)
        self.btn_massage.setGeometry(100, 40, 100, 40)


if __name__ == "__main__":
    app = QApplication([])
    my_win = MyWindow()
    my_win.show()
    app.exec()