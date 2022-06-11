"""
Time:     2022/6/1 22:20
Author:   LEHOSO
Version:  V 0.1
File:     test.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from LAndR import login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    loginUI = login.Ui_MainWindow()
    loginUI.setupUi(win)
    loginUI.widget_3.hide()


    def change_widget3():
        loginUI.widget_2.hide()
        loginUI.widget_3.show()


    def change_widget2():
        loginUI.widget_3.hide()
        loginUI.widget_2.show()


    loginUI.pushButton.clicked.connect(change_widget2)
    loginUI.pushButton_2.clicked.connect(change_widget3)

    win.show()
    sys.exit(app.exec_())
