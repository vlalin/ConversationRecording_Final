# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import img_usr_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(539, 357)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 45))
        self.frame_2.setStyleSheet(u"background-color: #fb5b5b")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 92, 157);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/newPrefix/img/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 40))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 270, 75, 23))
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(20, 50, 131, 21))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 311, 31))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 141, 16))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 120, 151, 16))
        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 150, 121, 22))
        self.dateEdit_2 = QDateEdit(self.frame)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(190, 150, 111, 22))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 190, 151, 16))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 190, 141, 16))
        self.timeEdit = QTimeEdit(self.frame)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(20, 220, 118, 22))
        self.timeEdit_2 = QTimeEdit(self.frame)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setGeometry(QRect(190, 220, 118, 22))
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 90, 481, 17))

        self.verticalLayout.addWidget(self.frame)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("SettingsWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0435\u043f\u0440\u0438\u0440\u044b\u0432\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438 (\u0441\u0435\u043a.)", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"\u0421 \u043a\u0430\u043a\u043e\u0433\u043e \u0447\u0438\u0441\u043b\u0430 \u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u043e \u043a\u0430\u043e\u043a\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"\u0421 \u043a\u0430\u043a\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u043e \u043a\u0430\u043a\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("SettingsWindow", u"\u0417\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c \u0437\u0432\u0443\u043a \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0432\u0441\u0435\u0433\u043e \u0441\u0435\u0430\u043d\u0441\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0432 Windows, \u0431\u0435\u0437 \u0430\u0432\u0442\u043e\u0437\u0430\u043f\u0438\u0441\u0438", None))
    # retranslateUi

