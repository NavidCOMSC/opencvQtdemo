import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QObject


class Master(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 940, 880)
        self.setWindowTitle('Load a query image')
        self.targetimage = CVLabel()
        self.textlabel = QLabel('query')

        ver_frame = QVBoxLayout()
        ver_frame.addWidget(self.targetimage)

        h_frame = QHBoxLayout()
        ver_frame.addLayout(h_frame)

        h_frame.addWidget(self.textlabel)
        button1 = QPushButton('testbut')
        h_frame.addWidget(button1)
        self.setLayout(ver_frame)

        self.query_cv = cv2.imread('polecat.jpg')
        #query_qt = self.convert_cv_qt(self.query_cv)
        self.targetimage.setcvPixmap(self.query_cv)


class CVLabel(QLabel):

    def __init__(self):
        super().__init__()
        print('init')

    def _convert_cv_qt(self):
        color_image = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = color_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QtGui.QImage(color_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pic = convert_to_qt_format.scaled(self.w1, self.h1, Qt.KeepAspectRatio)
        return QPixmap.fromImage(pic)

    def setcvPixmap(self, cv_img):
        print('setcvPixmap')
        self.cv_img= cv_img
        self.resizeEvent(None)
        #qpix = self.convert_cv_qt(self.cv_img)
        #self.setPixmap(qpix)

    def resizeEvent(self, event):
        print(event)
        geo = self.geometry()
        #print(geo)
        self.w1 = geo.width()*0.90
        self.h1 = geo.height()*0.90
        #self.resize(w1, h1)
        query_qt = self._convert_cv_qt()
        self.setPixmap(query_qt)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Master()
    ex.show()
    sys.exit(app.exec_())
