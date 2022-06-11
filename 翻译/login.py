# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import fanyi
from DataB import Db_R


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)

        # 隐藏框：
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 350, 466))
        self.label.setStyleSheet("border-image: url(:/images/images/bronya.jpg);\n"
                                 "border-top-left-radius:45px;\n"
                                 "border-bottom-left-radius:45px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 10, 431, 466))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                   "stop:0 #36d1dc, \n"
                                   "stop:1 #5b86e5\n"
                                   ");\n"
                                   "border-top-right-radius:45px;\n"
                                   "border-bottom-right-radius:45px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 40, 215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
                                      "    border:none;\n"
                                      "}\n"
                                      "#pushButton:focus{\n"
                                      "    color:rgb(186, 186, 186);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "#pushButton_2:focus{\n"
                                        "    color:rgb(186, 186, 186);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(380, 100, 391, 351))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px,solid,rgb(0,0,0);\n"
                                    "border-radius:8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 160, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px,solid,rgb(0,0,0);\n"
                                      "border-radius:8px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 270, 371, 51))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
                                        "    background-color: #4b5cc4;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border:3px,solid,rgb(0,0,0);\n"
                                        "    border-radius:25px;\n"
                                        "}\n"
                                        "#pushButton_3:hover{\n"
                                        "    background-color:#2e4e7e;\n"
                                        "    color: #a1afc9;\n"
                                        "}\n"
                                        "#pushButton_3:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 230, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 30, 31, 31))
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(380, 90, 391, 351))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 40, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:1px,solid,rgb(0,0,0);\n"
                                      "border-radius:8px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 120, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:1px,solid,rgb(0,0,0);\n"
                                      "border-radius:8px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 200, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px,solid,rgb(0,0,0);\n"
                                      "border-radius:8px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 280, 371, 51))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
                                        "    background-color: #4b5cc4;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border:3px,solid,rgb(0,0,0);\n"
                                        "    border-radius:25px;\n"
                                        "}\n"
                                        "#pushButton_5:hover{\n"
                                        "    background-color:#2e4e7e;\n"
                                        "    color: #a1afc9;\n"
                                        "}\n"
                                        "#pushButton_5:pressed{\n"
                                        "    padding-top:5px;\n"
                                        "    padding-left:5px;\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # 加阴影
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.pushButton_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        # 登录跳转
        # self.pushButton_3.clicked.connect(self.Lg)
        self.widget_3.hide()
        self.pushButton.clicked.connect(self.change_widget2)
        self.pushButton_2.clicked.connect(self.change_widget3)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change_widget3(self):
        self.widget_2.hide()
        self.widget_3.show()

    def change_widget2(self):
        self.widget_3.hide()
        self.widget_2.show()

    # def Lg(self):
    #     user_1 = self.lineEdit.text()
    #     password_1 = self.lineEdit_2.text()
    #     sql = "select * from user"
    #     user = Db_R(sql)
    #     for i in range(len(user)):
    #         if user['user'][i] == user_1 and user['password'][i] == password_1:
    #             self.w = QMainWindow()
    #             self.m = fanyi.Ui_MainWindow()
    #             self.m.setupUi(self.w)
    #             self.w.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "账号："))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "密码："))
        self.pushButton_3.setText(_translate("MainWindow", "登录"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "输入账号："))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "设置密码："))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "确认密码："))
        self.pushButton_5.setText(_translate("MainWindow", "注册"))


import loginAndRegister_rc
