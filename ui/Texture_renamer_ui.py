# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Texture_renamer_ui.ui'
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
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.L_asset_name = QLabel(self.centralwidget)
        self.L_asset_name.setObjectName(u"L_asset_name")

        self.horizontalLayout.addWidget(self.L_asset_name)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.T_name = QLineEdit(self.centralwidget)
        self.T_name.setObjectName(u"T_name")

        self.horizontalLayout.addWidget(self.T_name)

        self.horizontalSpacer_6 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Directory = QHBoxLayout()
        self.Directory.setObjectName(u"Directory")
        self.L_directory = QLabel(self.centralwidget)
        self.L_directory.setObjectName(u"L_directory")

        self.Directory.addWidget(self.L_directory)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.Directory.addItem(self.horizontalSpacer_4)

        self.T_path = QLineEdit(self.centralwidget)
        self.T_path.setObjectName(u"T_path")

        self.Directory.addWidget(self.T_path)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.Directory.addItem(self.horizontalSpacer_3)

        self.B_finder = QPushButton(self.centralwidget)
        self.B_finder.setObjectName(u"B_finder")

        self.Directory.addWidget(self.B_finder)


        self.verticalLayout.addLayout(self.Directory)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.L_file = QLabel(self.centralwidget)
        self.L_file.setObjectName(u"L_file")

        self.verticalLayout.addWidget(self.L_file)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.Table = QTableWidget(self.centralwidget)
        if (self.Table.columnCount() < 3):
            self.Table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font);
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Table.setObjectName(u"Table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table.sizePolicy().hasHeightForWidth())
        self.Table.setSizePolicy(sizePolicy)
        self.Table.setAutoFillBackground(False)
        self.Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Table.setSortingEnabled(True)
        self.Table.horizontalHeader().setDefaultSectionSize(300)

        self.verticalLayout.addWidget(self.Table)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.Go = QHBoxLayout()
        self.Go.setObjectName(u"Go")
        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.Go.addItem(self.horizontalSpacer)

        self.B_go = QPushButton(self.centralwidget)
        self.B_go.setObjectName(u"B_go")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.B_go.setFont(font1)

        self.Go.addWidget(self.B_go)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.Go.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.Go)


        self.verticalLayout_2.addLayout(self.verticalLayout)

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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.L_asset_name.setText(QCoreApplication.translate("MainWindow", u"Asset Name:", None))
        self.L_directory.setText(QCoreApplication.translate("MainWindow", u"Texture Directory:", None))
        self.B_finder.setText(QCoreApplication.translate("MainWindow", u"Finder", None))
        self.L_file.setText(QCoreApplication.translate("MainWindow", u"Texture Files:", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Texture File", None));
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Resloution", None));
        self.B_go.setText(QCoreApplication.translate("MainWindow", u"Let's go!", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

