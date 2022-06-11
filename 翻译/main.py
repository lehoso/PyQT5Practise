"""
Time:     2022/6/1 22:40
Author:   LEHOSO
Version:  V 0.1
File:     main.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import fanyi
import login
from DataB import Db_R


class fanyi1(fanyi.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(fanyi1, self).__init__()
        self.setupUi(self)


class loginUi1(login.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(loginUi1, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    # loginUI = login.Ui_MainWindow()
    loginUi = loginUi1()
    fanyi = fanyi1()
    loginUi.setupUi(win)


    def Lg():
        user_1 = loginUi.lineEdit.text()
        password_1 = loginUi.lineEdit_2.text()
        sql = "select * from user"
        user = Db_R(sql)
        for i in range(len(user)):
            if user['user'][i] == user_1 and user['password'][i] == password_1:
                win.close()
                fanyi.show()


    loginUi.pushButton_3.clicked.connect(Lg)

    win.show()
    sys.exit(app.exec_())
