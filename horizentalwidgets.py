import sys
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor, QPalette
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QObject


class Master(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 440, 380)
        self.setWindowTitle('Load a query image')

        self.targetimage = ResWidget()
        #self.textlabel = QLabel('query')

        #self.resultimage = CVLabel()
        #self.resulttext = QLabel('person1')
        self.result_image = ResWidget()

        ver_frame = QVBoxLayout()
        ver_frame.addWidget(self.targetimage)

        res_layout = QHBoxLayout()
        #res_layout.setContentsMargins(0, 0, 0, 0)
        res_layout.setSpacing(10)
        ver_frame.addLayout(res_layout)

        res_layout.addWidget(self.result_image)


        #h_frame = QHBoxLayout()
        #ver_frame.addLayout(h_frame)

        #h_frame.addWidget(self.textlabel)
        #h_frame.addWidget(self.resulttext)

        #button1 = QPushButton('testbut')
        #h_frame.addWidget(button1)
        self.setLayout(ver_frame)

        self.query_cv = cv2.imread('polecat.jpg')
        self.person1_cv = cv2.imread('query1.jpg')
        #query_qt = self.convert_cv_qt(self.query_cv)
        self.targetimage.setcvPixmap(self.query_cv)
        self.targetimage.setText('Query')
        self.result_image.setcvPixmap(self.person1_cv)
        self.result_image.setText('Result')

        self.results = []
        for n in range(10):
            tmp = ResWidget()
            res_layout.addWidget(tmp)
            #res_layout.setSpacing(0.5)
            self.results.append(tmp)

        #res_layout.addWidget(self.result2)

class ResWidget(QWidget):

    def __init__(self, img=None, text=None):
        super().__init__()
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor('red'))
        self.setPalette(pal)
        self._qvLabel()
        self.setMaximumWidth(200)
        if img:
            self.setcvPixmap(img)
        else:
            tmp = np.ones((100, 100, 3), np.uint8)*128
            self.setcvPixmap(tmp)
        if text:
            self.setText(text)

    def _qvLabel(self):

        self._perimage = CVLabel()
        self._textperimage = QLabel()

        ver_frame = QVBoxLayout()
        ver_frame.addWidget(self._perimage)

        #h_frame = QHBoxLayout()
        #ver_frame.addLayout(h_frame)
        ver_frame.addWidget(self._textperimage)

        self.setLayout(ver_frame)

    def setcvPixmap(self, cv_img):
        self._perimage.setcvPixmap(cv_img)

    def setText(self, text):
        self._textperimage.setText(text)



class CVLabel(QLabel):

    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor('blue'))
        self.setPalette(pal)
        #print('init')

    def _convert_cv_qt(self):
        color_image = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = color_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QtGui.QImage(color_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pic = convert_to_qt_format.scaled(self.w1, self.h1, Qt.KeepAspectRatio)
        return QPixmap.fromImage(pic)

    def setcvPixmap(self, cv_img):
        #print('setcvPixmap')
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

