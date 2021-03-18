from PIL import Image
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPainter, QColor, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('PIL20.ui', self)

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Отображение картинки')
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.jpg);;Все файлы (*)')[0]
        self.pixmap = QPixmap(self.fname)
        self.image = QLabel(self)
        self.image.move(140, 20)
        self.image.resize(220, 220)
        self.image.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.change_color)
        self.pushButton_5.clicked.connect(self.change_def)
        self.pushButton_6.clicked.connect(self.change_def1)
        self.mask = self.pixmap.createMaskFromColor(QColor(255, 255, 255), Qt.MaskOutColor)

    def change_color(self):
        p = QPainter(self.pixmap)
        p.setPen(QColor(0, 0, 255))
        p.drawPixmap(self.pixmap.rect(), self.mask, self.mask.rect())
        p.end()

    def change_def(self):
        pass

    def change_def1(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
