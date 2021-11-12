# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_tool_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 250)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 15, 30, 15)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Name = QHBoxLayout()
        self.Name.setSpacing(6)
        self.Name.setObjectName(u"Name")
        self.L_name = QLabel(self.centralwidget)
        self.L_name.setObjectName(u"L_name")
        font = QFont()
        font.setPointSize(15)
        self.L_name.setFont(font)

        self.Name.addWidget(self.L_name)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.Name.addItem(self.horizontalSpacer)

        self.T_name = QLineEdit(self.centralwidget)
        self.T_name.setObjectName(u"T_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_name.sizePolicy().hasHeightForWidth())
        self.T_name.setSizePolicy(sizePolicy)

        self.Name.addWidget(self.T_name)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Name.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.Name)

        self.Path = QHBoxLayout()
        self.Path.setObjectName(u"Path")
        self.L_path = QLabel(self.centralwidget)
        self.L_path.setObjectName(u"L_path")
        self.L_path.setFont(font)

        self.Path.addWidget(self.L_path)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.Path.addItem(self.horizontalSpacer_2)

        self.T_path = QLineEdit(self.centralwidget)
        self.T_path.setObjectName(u"T_path")

        self.Path.addWidget(self.T_path)

        self.B_finder = QPushButton(self.centralwidget)
        self.B_finder.setObjectName(u"B_finder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.B_finder.sizePolicy().hasHeightForWidth())
        self.B_finder.setSizePolicy(sizePolicy1)
        self.B_finder.setFont(font)
        self.B_finder.setFlat(False)

        self.Path.addWidget(self.B_finder)


        self.verticalLayout.addLayout(self.Path)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Go = QHBoxLayout()
        self.Go.setObjectName(u"Go")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Go.addItem(self.horizontalSpacer_4)

        self.B_go = QPushButton(self.centralwidget)
        self.B_go.setObjectName(u"B_go")
        sizePolicy.setHeightForWidth(self.B_go.sizePolicy().hasHeightForWidth())
        self.B_go.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.B_go.setFont(font1)

        self.Go.addWidget(self.B_go)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Go.addItem(self.horizontalSpacer_5)

        self.Go.setStretch(0, 1)
        self.Go.setStretch(1, 5)
        self.Go.setStretch(2, 1)

        self.verticalLayout.addLayout(self.Go)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Asset Tool", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.L_name.setText(QCoreApplication.translate("MainWindow", u"Asset Name:", None))
        self.L_path.setText(QCoreApplication.translate("MainWindow", u"Asset Path:", None))
        self.B_finder.setText(QCoreApplication.translate("MainWindow", u"Finder", None))
        self.B_go.setText(QCoreApplication.translate("MainWindow", u"Let's go!", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

