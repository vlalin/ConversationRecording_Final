# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import img_usr_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.navigation_frame = QFrame(self.centralwidget)
        self.navigation_frame.setObjectName(u"navigation_frame")
        self.navigation_frame.setMaximumSize(QSize(16777215, 50))
        self.navigation_frame.setStyleSheet(u"background-color: #fb5b5b")
        self.navigation_frame.setFrameShape(QFrame.WinPanel)
        self.navigation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.navigation_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_frame = QFrame(self.navigation_frame)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.name_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(45, 5, 0, 0)
        self.lb_name_soft = QLabel(self.name_frame)
        self.lb_name_soft.setObjectName(u"lb_name_soft")
        self.lb_name_soft.setMaximumSize(QSize(100, 96))
        self.lb_name_soft.setStyleSheet(u"font: 24pt \"Pristina\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lb_name_soft)


        self.horizontalLayout.addWidget(self.name_frame)

        self.btn_frame = QFrame(self.navigation_frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setMaximumSize(QSize(100, 16777215))
        self.btn_frame.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 92, 157);\n"
"}")
        self.btn_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.btn_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_minimized = QPushButton(self.btn_frame)
        self.btn_minimized.setObjectName(u"btn_minimized")
        self.btn_minimized.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/newPrefix/img/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimized.setIcon(icon)
        self.btn_minimized.setIconSize(QSize(20, 30))

        self.horizontalLayout_2.addWidget(self.btn_minimized)

        self.btn_close = QPushButton(self.btn_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/img/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(20, 30))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.btn_frame)


        self.verticalLayout.addWidget(self.navigation_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: #22222e")
        self.main_frame.setFrameShape(QFrame.WinPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.main_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(26, 9, 351, 311))
        self.btn_verticalLayout = QVBoxLayout(self.layoutWidget)
        self.btn_verticalLayout.setSpacing(0)
        self.btn_verticalLayout.setObjectName(u"btn_verticalLayout")
        self.btn_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_start = QPushButton(self.layoutWidget)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Microsoft JhengHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #fb5b5d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButtom:pressed {\n"
"	background-color: #fa4244\n"
"}")

        self.btn_verticalLayout.addWidget(self.btn_start)

        self.btn_stop = QPushButton(self.layoutWidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(0, 40))
        self.btn_stop.setFont(font)
        self.btn_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #fb5b5d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButtom:pressed {\n"
"	background-color: #fa4244\n"
"}")

        self.btn_verticalLayout.addWidget(self.btn_stop)

        self.btn_settings = QPushButton(self.layoutWidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 40))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #fb5b5d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButtom:pressed {\n"
"	background-color: #fa4244\n"
"}")

        self.btn_verticalLayout.addWidget(self.btn_settings)

        self.btn_ninja = QPushButton(self.layoutWidget)
        self.btn_ninja.setObjectName(u"btn_ninja")
        self.btn_ninja.setMinimumSize(QSize(0, 40))
        self.btn_ninja.setFont(font)
        self.btn_ninja.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ninja.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #fb5b5d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButtom:pressed {\n"
"	background-color: #fa4244\n"
"}")

        self.btn_verticalLayout.addWidget(self.btn_ninja)

        self.lb_status = QLabel(self.layoutWidget)
        self.lb_status.setObjectName(u"lb_status")
        sizePolicy.setHeightForWidth(self.lb_status.sizePolicy().hasHeightForWidth())
        self.lb_status.setSizePolicy(sizePolicy)
        self.lb_status.setFont(font)
        self.lb_status.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.btn_verticalLayout.addWidget(self.lb_status, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_name_soft.setText(QCoreApplication.translate("MainWindow", u"U.S.R", None))
        self.btn_minimized.setText("")
        self.btn_close.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c \u0417\u0410\u041f\u0418\u0421\u042c!", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u0422\u0410\u041d\u041e\u0412\u0418\u0422\u042c \u0417\u0410\u041f\u0418\u0421\u042c!", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0418!", None))
        self.btn_ninja.setText(QCoreApplication.translate("MainWindow", u"\u0424\u041e\u041d\u041e\u0412\u042b\u0419 \u0420\u0415\u0416\u0418\u041c!", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c =)", None))
    # retranslateUi

