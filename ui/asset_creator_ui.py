# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_creator_ui.ui'
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
        MainWindow.resize(800, 450)
        font = QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionDeveloped_by_RiPPLE_in_Nanjing = QAction(MainWindow)
        self.actionDeveloped_by_RiPPLE_in_Nanjing.setObjectName(u"actionDeveloped_by_RiPPLE_in_Nanjing")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_asset = QWidget()
        self.tab_asset.setObjectName(u"tab_asset")
        self.tab_asset.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.tab_asset)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Name = QHBoxLayout()
        self.Name.setSpacing(6)
        self.Name.setObjectName(u"Name")
        self.L_name = QLabel(self.tab_asset)
        self.L_name.setObjectName(u"L_name")
        self.L_name.setFont(font)

        self.Name.addWidget(self.L_name)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.Name.addItem(self.horizontalSpacer)

        self.T_name = QLineEdit(self.tab_asset)
        self.T_name.setObjectName(u"T_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_name.sizePolicy().hasHeightForWidth())
        self.T_name.setSizePolicy(sizePolicy)

        self.Name.addWidget(self.T_name)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Name.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.Name)

        self.Path = QHBoxLayout()
        self.Path.setObjectName(u"Path")
        self.L_path = QLabel(self.tab_asset)
        self.L_path.setObjectName(u"L_path")
        self.L_path.setFont(font)

        self.Path.addWidget(self.L_path)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.Path.addItem(self.horizontalSpacer_2)

        self.T_path = QLineEdit(self.tab_asset)
        self.T_path.setObjectName(u"T_path")

        self.Path.addWidget(self.T_path)

        self.B_finder = QPushButton(self.tab_asset)
        self.B_finder.setObjectName(u"B_finder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.B_finder.sizePolicy().hasHeightForWidth())
        self.B_finder.setSizePolicy(sizePolicy1)
        self.B_finder.setFont(font)
        self.B_finder.setFlat(False)

        self.Path.addWidget(self.B_finder)


        self.verticalLayout_2.addLayout(self.Path)

        self.Steps = QHBoxLayout()
        self.Steps.setObjectName(u"Steps")
        self.label = QLabel(self.tab_asset)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.Steps.addWidget(self.label)

        self.CB_mdl = QCheckBox(self.tab_asset)
        self.CB_mdl.setObjectName(u"CB_mdl")
        self.CB_mdl.setChecked(True)

        self.Steps.addWidget(self.CB_mdl)

        self.CB_ldv = QCheckBox(self.tab_asset)
        self.CB_ldv.setObjectName(u"CB_ldv")
        self.CB_ldv.setChecked(True)

        self.Steps.addWidget(self.CB_ldv)

        self.CB_rig = QCheckBox(self.tab_asset)
        self.CB_rig.setObjectName(u"CB_rig")

        self.Steps.addWidget(self.CB_rig)

        self.CB_anim = QCheckBox(self.tab_asset)
        self.CB_anim.setObjectName(u"CB_anim")

        self.Steps.addWidget(self.CB_anim)

        self.Steps.setStretch(0, 2)
        self.Steps.setStretch(1, 3)
        self.Steps.setStretch(2, 3)
        self.Steps.setStretch(3, 3)
        self.Steps.setStretch(4, 3)

        self.verticalLayout_2.addLayout(self.Steps)

        self.tabWidget.addTab(self.tab_asset, "")
        self.tab_shot = QWidget()
        self.tab_shot.setObjectName(u"tab_shot")
        self.verticalLayout_3 = QVBoxLayout(self.tab_shot)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.tab_shot)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.lineEdit = QLineEdit(self.tab_shot)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.L_shot_name = QLabel(self.tab_shot)
        self.L_shot_name.setObjectName(u"L_shot_name")
        self.L_shot_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.L_shot_name)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.T_shot_name = QLineEdit(self.tab_shot)
        self.T_shot_name.setObjectName(u"T_shot_name")

        self.horizontalLayout_2.addWidget(self.T_shot_name)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.L_shot_path = QLabel(self.tab_shot)
        self.L_shot_path.setObjectName(u"L_shot_path")
        self.L_shot_path.setFont(font)

        self.horizontalLayout.addWidget(self.L_shot_path)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.T_shot_path = QLineEdit(self.tab_shot)
        self.T_shot_path.setObjectName(u"T_shot_path")

        self.horizontalLayout.addWidget(self.T_shot_path)

        self.B_shot_finder = QPushButton(self.tab_shot)
        self.B_shot_finder.setObjectName(u"B_shot_finder")
        self.B_shot_finder.setFont(font)

        self.horizontalLayout.addWidget(self.B_shot_finder)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.tab_shot)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.checkBox_2 = QCheckBox(self.tab_shot)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.tab_shot)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.checkBox = QCheckBox(self.tab_shot)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.tab_shot)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.tab_shot)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_3.addWidget(self.checkBox_5)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 3)
        self.horizontalLayout_3.setStretch(4, 2)
        self.horizontalLayout_3.setStretch(5, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_shot, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 31))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuAbout.addAction(self.actionDeveloped_by_RiPPLE_in_Nanjing)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Asset Tool", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionDeveloped_by_RiPPLE_in_Nanjing.setText(QCoreApplication.translate("MainWindow", u"Developed by RiPPLE in Nanjing.", None))
        self.L_name.setText(QCoreApplication.translate("MainWindow", u"Asset Name:", None))
        self.L_path.setText(QCoreApplication.translate("MainWindow", u"Asset Path:", None))
        self.B_finder.setText(QCoreApplication.translate("MainWindow", u"Finder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Steps:", None))
        self.CB_mdl.setText(QCoreApplication.translate("MainWindow", u"Modeling", None))
        self.CB_ldv.setText(QCoreApplication.translate("MainWindow", u"LookDev", None))
        self.CB_rig.setText(QCoreApplication.translate("MainWindow", u"Rigging", None))
        self.CB_anim.setText(QCoreApplication.translate("MainWindow", u"Animation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asset), QCoreApplication.translate("MainWindow", u"Asset Creator", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sequence Name:", None))
        self.L_shot_name.setText(QCoreApplication.translate("MainWindow", u"Shot Name:", None))
        self.L_shot_path.setText(QCoreApplication.translate("MainWindow", u"Shot Path:", None))
        self.B_shot_finder.setText(QCoreApplication.translate("MainWindow", u"Finder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Steps:", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Layout", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Animation", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Fx", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Comp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_shot), QCoreApplication.translate("MainWindow", u"Shot Creator", None))
        self.B_go.setText(QCoreApplication.translate("MainWindow", u"Let's go!", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

