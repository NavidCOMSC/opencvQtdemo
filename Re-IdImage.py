import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QObject


class ImageLoad(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def resizeEvent(self, event):
        geo = self.geometry()
        w1 = geo.width()*0.90
        h1 = geo.height()*0.90
        self.targetimage.resize(w1, h1)
        query_qt = self.convert_cv_qt(self.query_cv)
        self.targetimage.setPixmap(query_qt)
        print(geo)


    def initUI(self):
        print('init')
        self.setGeometry(500, 500, 940, 880)
        self.setWindowTitle('Load a query image')
        self.targetimage = QLabel(self)
        self.textlabel = QLabel('query')
        #pixmap = QPixmap('polecat.jpg')
        #self.targetimage.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())

        ver_frame = QVBoxLayout()
        ver_frame.addWidget(self.targetimage)

        h_frame = QHBoxLayout()
        ver_frame.addLayout(h_frame)

        h_frame.addWidget(self.textlabel)
        button1 = QPushButton('hi')
        h_frame.addWidget(button1)
        self.setLayout(ver_frame)

        self.query_cv = cv2.imread('polecat.jpg')
        query_qt = self.convert_cv_qt(self.query_cv)
        self.targetimage.setPixmap(query_qt)

    def convert_cv_qt(self, query_cv):
        color_image = cv2.cvtColor(query_cv, cv2.COLOR_BGR2RGB)
        h, w, ch = color_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QtGui.QImage(color_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pic = convert_to_qt_format.scaled(self.targetimage.width(), self.targetimage.height(), Qt.KeepAspectRatio)
        return QPixmap.fromImage(pic)

        #self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ImageLoad()
    ex.show()
    sys.exit(app.exec_())







