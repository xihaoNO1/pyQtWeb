#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
 
 
class Form(QWidget):
    def __init__(self):
        super().__init__()
        tmp = QWebEngineView()
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(tmp)
        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout1, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("JHCMS-外卖")
        tmp.load(QUrl('http://wmdemo.jhcms.cn/admin/?index-login'))
        tmp.show()
 
 
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())