#!/usr/bin/env python3

import sys
# import json
from PyQt5 import QtWidgets
import ui
# from datetime import date
# import time

class BrowserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.btnFinish.setStyleSheet("background: green; border: 1px solid black")
        # self.ui.btnFinish.clicked.connect(self.Finish)
        # self.ui.btnExit.clicked.connect(lambda:self.close()) # Remove this line when finished testing


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    # window.showFullScreen()
    sys.exit(app.exec())
