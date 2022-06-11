"""
Time:     2022/5/29 19:12
Author:   LEHOSO
Version:  V 0.1
File:     Menu.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from secondHandHouse import menu
from show import chart


def m_main():
    app = QApplication(sys.argv)
    win = QMainWindow()  # 创建一个窗口
    menuUI = menu.Ui_MainWindow()  # 创建一个窗口的具体样式
    menuUI.setupUi(win)
    menuUI.groupBox.show()
    menuUI.groupBox_2.hide()
    menuUI.price_bar()

    def charge_1():
        menuUI.groupBox.show()
        menuUI.groupBox_2.hide()

    def charge_2():
        menuUI.groupBox.hide()
        menuUI.groupBox_2.show()
        menuUI.price_chart()

    menuUI.pushButton.clicked.connect(charge_1)
    menuUI.pushButton_2.clicked.connect(charge_2)

    win.show()
