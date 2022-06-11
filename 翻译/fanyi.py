# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fanyi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import pc_fanyi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 754)
        MainWindow.setStyleSheet("background-image: url(:/背景/images/980.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(381, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-image: url();")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 1, 2, 3)
        self.pb_fanyi_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_fanyi_1.setMinimumSize(QtCore.QSize(131, 131))
        self.pb_fanyi_1.setStyleSheet("border-image: url(:/fy/images/右箭头.png);\n"
                                      "background-image: url();")
        self.pb_fanyi_1.setText("")
        self.pb_fanyi_1.setObjectName("pb_fanyi_1")
        self.gridLayout.addWidget(self.pb_fanyi_1, 1, 5, 2, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setMinimumSize(QtCore.QSize(361, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-image: url();")
        self.textEdit_2.setPlaceholderText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 7, 2, 3)
        spacerItem3 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 10, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 8, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 2)
        self.pb_fanyi_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_fanyi_2.setMinimumSize(QtCore.QSize(71, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_fanyi_2.setFont(font)
        self.pb_fanyi_2.setStyleSheet("font: 14pt \"Adobe Devanagari\";\n"
                                      "background-image: url();\n"
                                      "color: rgb(43, 255, 174);")
        self.pb_fanyi_2.setObjectName("pb_fanyi_2")
        self.gridLayout.addWidget(self.pb_fanyi_2, 4, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(476, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 3, 1, 5)
        self.pb_fanyi_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_fanyi_3.setMinimumSize(QtCore.QSize(71, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_fanyi_3.setFont(font)
        self.pb_fanyi_3.setStyleSheet("font: 14pt \"Adobe Devanagari\";\n"
                                      "background-image: url();\n"
                                      "color: rgb(43, 255, 174);")
        self.pb_fanyi_3.setObjectName("pb_fanyi_3")
        self.gridLayout.addWidget(self.pb_fanyi_3, 4, 8, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 9, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 5, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 5, 8, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.ac_open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/fy/images/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ac_open.setIcon(icon)
        self.ac_open.setObjectName("ac_open")
        self.ac_save = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/fy/images/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ac_save.setIcon(icon1)
        self.ac_save.setObjectName("ac_save")
        self.ac_close = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/fy/images/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ac_close.setIcon(icon2)
        self.ac_close.setObjectName("ac_close")
        self.ac_start = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/fy/images/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ac_start.setIcon(icon3)
        self.ac_start.setObjectName("ac_start")
        self.ac_z = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/fy/images/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ac_z.setIcon(icon4)
        self.ac_z.setObjectName("ac_z")
        self.menu.addAction(self.ac_open)
        self.menu.addAction(self.ac_save)
        self.menu.addAction(self.ac_close)
        self.menu_2.addAction(self.ac_start)
        self.menu_2.addAction(self.ac_z)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.ac_open)
        self.toolBar.addAction(self.ac_save)
        self.toolBar.addAction(self.ac_close)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ac_start)
        self.toolBar.addAction(self.ac_z)

        self.retranslateUi(MainWindow)
        self.ac_close.triggered.connect(MainWindow.close)
        self.pb_fanyi_3.clicked.connect(MainWindow.close)
        self.pb_fanyi_2.clicked.connect(self.textEdit.clear)
        self.pb_fanyi_2.clicked.connect(self.textEdit_2.clear)

        # 翻译
        self.pb_fanyi_1.clicked.connect(self.Tr)
        self.ac_start.triggered.connect(self.Tr)

        self.pb_fanyi_2.clicked.connect(self.textEdit.clear)
        self.pb_fanyi_2.clicked.connect(self.textEdit_2.clear)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Tr(self):
        if self.textEdit.toPlainText() == "":
            content = "请输入翻译内容"
            st = pc_fanyi.transatle(content)
            self.textEdit_2.setText(st)
        else:
            content = self.textEdit.toPlainText()
            st = pc_fanyi.transatle(content)
            print(st)
            self.textEdit_2.setText(st)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请输入翻译内容..."))
        self.pb_fanyi_2.setText(_translate("MainWindow", "清空"))
        self.pb_fanyi_3.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "翻译"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.ac_open.setText(_translate("MainWindow", "打开"))
        self.ac_open.setToolTip(_translate("MainWindow", "打开(O)"))
        self.ac_save.setText(_translate("MainWindow", "保存"))
        self.ac_close.setText(_translate("MainWindow", "关闭"))
        self.ac_start.setText(_translate("MainWindow", "开始翻译"))
        self.ac_z.setText(_translate("MainWindow", "暂停翻译"))


import loginAndRegister_rc
