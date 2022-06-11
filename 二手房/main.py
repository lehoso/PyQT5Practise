import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from DataB import Db_R
from LAndR import login
from secondHandHouse import menu


class me1(menu.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(me1, self).__init__()
        self.setupUi(self)


class loginUi1(login.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(loginUi1, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    loginUi = loginUi1()
    me = me1()
    loginUi.setupUi(win)
    loginUi.widget_3.hide()


    def login():
        user_1 = loginUi.lineEdit.text()
        password_1 = loginUi.lineEdit_2.text()
        sql = "select * from user"
        user = Db_R(sql)
        for i in range(len(user)):
            if user['user'][i] == user_1 and user['password'][i] == password_1:
                win.close()
                me.show()


    loginUi.pushButton_3.clicked.connect(login)
    win.show()
    sys.exit(app.exec_())
