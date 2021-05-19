import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets, QtTest
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_settings_window import Ui_SettingsWindow
from datetime import datetime
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)


        #REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        #CLOSE WINDOW
        self.ui.pushButton.clicked.connect(lambda: self.close())

        self.ui.pushButton_2.clicked.connect(self.SaveSettings)

        # SHOW WINDOW
        self.show()
        self.DownloadSettings()

    def SaveSettings(self):
        with open('Settings.txt', 'w') as File:
            File.writelines(self.ui.spinBox.text() + '\n')
            File.writelines(str(int(self.ui.checkBox.checkState())) + '\n')
            File.writelines(self.ui.dateEdit.text() + '\n')
            File.writelines(self.ui.dateEdit_2.text() + '\n')
            File.writelines(self.ui.timeEdit.text() + '\n')
            File.writelines(self.ui.timeEdit_2.text())

    def DownloadSettings(self):
        data = []
        with open('Settings.txt', 'r') as File:
            data = File.readlines()
        self.ui.spinBox.setValue(int(data[0]))
        self.ui.checkBox.setChecked(int(data[1]))
        self.ui.dateEdit.setDate(datetime.strptime(str(data[2]).rstrip('\n'), '%d.%m.%Y'))
        self.ui.dateEdit_2.setDate(datetime.strptime(str(data[3]).rstrip('\n'), '%d.%m.%Y'))
        self.ui.timeEdit.setTime(datetime.strptime(str(data[4]).rstrip('\n'), '%H:%M').time())
        self.ui.timeEdit_2.setTime(datetime.strptime(str(data[5]).rstrip('\n'), '%H:%M').time())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())