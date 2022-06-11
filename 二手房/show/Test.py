"""
Time:     2022/6/1 12:37
Author:   LEHOSO
Version:  V 0.1
File:     Test.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import matplotlib
from matplotlib import pyplot as plt

from chongqing.bar import Bar

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符，使用rc配置文件来自定义

data = "../chongqing/cq_pre-owned_house2.csv"


def hot_portal_barh():
    clean = Bar.get_clean(data)
    x, y = Bar.get_hot_portal(clean)

    # y = [100, 200, 50]
    # x = ['沙坪坝', '渝北', '江北']
    plt.figure()  # 图形画布
    plt.barh(x, y, alpha=0.9, color='red')  # 绘制条形图
    plt.xlabel("均价")  # 区域文字
    plt.ylabel("户型")  # 均价文字
    plt.title("title")  # 表标题文字
    # 为每一个图形加数值标签
    for y, x in enumerate(y):
        plt.text(x + 100, y, str(x) + '元/平', ha='left')
    plt.show()


hot_portal_barh()
