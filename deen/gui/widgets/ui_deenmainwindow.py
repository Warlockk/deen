# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DeenMainWindow = QtWidgets.QScrollArea(self.centralwidget)
        self.DeenMainWindow.setEnabled(True)
        self.DeenMainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.DeenMainWindow.setWidgetResizable(True)
        self.DeenMainWindow.setObjectName("DeenMainWindow")
        self.encoder_widget_scrollable = QtWidgets.QWidget()
        self.encoder_widget_scrollable.setGeometry(QtCore.QRect(0, 0, 996, 696))
        self.encoder_widget_scrollable.setObjectName("encoder_widget_scrollable")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.encoder_widget_scrollable)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encoder_widget_layout = QtWidgets.QHBoxLayout()
        self.encoder_widget_layout.setObjectName("encoder_widget_layout")
        self.verticalLayout_2.addLayout(self.encoder_widget_layout)
        self.DeenMainWindow.setWidget(self.encoder_widget_scrollable)
        self.verticalLayout.addWidget(self.DeenMainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDirection = QtWidgets.QMenu(self.menubar)
        self.menuDirection.setObjectName("menuDirection")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_from_file = QtWidgets.QAction(MainWindow)
        self.actionLoad_from_file.setObjectName("actionLoad_from_file")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionStatus_console = QtWidgets.QAction(MainWindow)
        self.actionStatus_console.setObjectName("actionStatus_console")
        self.actionTop_to_bottom = QtWidgets.QAction(MainWindow)
        self.actionTop_to_bottom.setObjectName("actionTop_to_bottom")
        self.actionLeft_to_right = QtWidgets.QAction(MainWindow)
        self.actionLeft_to_right.setObjectName("actionLeft_to_right")
        self.actionCopy_to_clipboard = QtWidgets.QAction(MainWindow)
        self.actionCopy_to_clipboard.setObjectName("actionCopy_to_clipboard")
        self.actionSave_content_to_file = QtWidgets.QAction(MainWindow)
        self.actionSave_content_to_file.setObjectName("actionSave_content_to_file")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.menuFile.addAction(self.actionLoad_from_file)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionStatus_console)
        self.menuDirection.addAction(self.actionTop_to_bottom)
        self.menuDirection.addAction(self.actionLeft_to_right)
        self.menuTools.addAction(self.actionCopy_to_clipboard)
        self.menuTools.addAction(self.actionSave_content_to_file)
        self.menuTools.addAction(self.actionSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuDirection.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuDirection.setTitle(_translate("MainWindow", "&Direction"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionLoad_from_file.setText(_translate("MainWindow", "Load from file"))
        self.actionLoad_from_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionStatus_console.setText(_translate("MainWindow", "Status console"))
        self.actionStatus_console.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionTop_to_bottom.setText(_translate("MainWindow", "Top to bottom"))
        self.actionTop_to_bottom.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionLeft_to_right.setText(_translate("MainWindow", "Left to right"))
        self.actionLeft_to_right.setShortcut(_translate("MainWindow", "Ctrl+."))
        self.actionCopy_to_clipboard.setText(_translate("MainWindow", "Copy to clipboard"))
        self.actionSave_content_to_file.setText(_translate("MainWindow", "Save content to file"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))


