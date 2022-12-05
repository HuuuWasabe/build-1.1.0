# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'junkntradeuKwEUg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 420)
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: #040f13;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#sideMenu {\n"
"	background-color:  #040f13;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 10px;\n"
"	background-color: #1f232a;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#mainMenu {\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 85, 127)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255)\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setFrameShape(QFrame.Box)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 30))
        self.menuBtn.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QCustomSlideMenu(self.frame_2)
        self.sideMenu.setObjectName(u"sideMenu")
        self.verticalLayout_2 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.frame_4 = QFrame(self.sideMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setKerning(True)
        self.frame_4.setFont(font1)
        self.frame_4.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.profileBtn = QPushButton(self.frame_4)
        self.profileBtn.setObjectName(u"profileBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon1)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.profileBtn)

        self.redeemBtn = QPushButton(self.frame_4)
        self.redeemBtn.setObjectName(u"redeemBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/shopping-bag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemBtn.setIcon(icon2)
        self.redeemBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.redeemBtn)

        self.junkBtn = QPushButton(self.frame_4)
        self.junkBtn.setObjectName(u"junkBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.junkBtn.setIcon(icon3)
        self.junkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.junkBtn)

        self.rewardBtn = QPushButton(self.frame_4)
        self.rewardBtn.setObjectName(u"rewardBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rewardBtn.setIcon(icon4)
        self.rewardBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.rewardBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideMenu)

        self.mainMenu = QFrame(self.frame_2)
        self.mainMenu.setObjectName(u"mainMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainMenu.sizePolicy().hasHeightForWidth())
        self.mainMenu.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.label_2 = QLabel(self.profile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 120, 221, 60))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.profile)
        self.redeem = QWidget()
        self.redeem.setObjectName(u"redeem")
        self.label_3 = QLabel(self.redeem)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 90, 251, 111))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.redeem)
        self.shops = QWidget()
        self.shops.setObjectName(u"shops")
        self.label_4 = QLabel(self.shops)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 90, 331, 111))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.shops)
        self.rsystem = QWidget()
        self.rsystem.setObjectName(u"rsystem")
        self.label_5 = QLabel(self.rsystem)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 90, 351, 111))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.rsystem)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainMenu)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Junk N' Trade", None))
        self.profileBtn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.redeemBtn.setText(QCoreApplication.translate("MainWindow", u"Redeem", None))
        self.junkBtn.setText(QCoreApplication.translate("MainWindow", u"Junk Shops", None))
        self.rewardBtn.setText(QCoreApplication.translate("MainWindow", u"Reward System", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REDEEM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"JUNK SHOPS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REWARD SYS", None))
    # retranslateUi

