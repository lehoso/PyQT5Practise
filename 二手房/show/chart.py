"""
Time:     2022/6/1 14:23
Author:   LEHOSO
Version:  V 0.1
File:     chart.py
Describe: Write during the junior at CQUCC, Github link: https://github.com/lehoso
"""
import matplotlib

from chongqing.bar import Bar
from chongqing.forecast import forecast
from chongqing.pie import pie
from chongqing.plots import plots
from chongqing.plots_2 import plots2

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
matplotlib.rcParams['font.size'] = 14  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符，使用rc配置文件来自定义

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# 绘制图形
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height),
                          dpi=dpi, facecolor="none", edgecolor='none')
        # self.fig = Figure(figsize=(width, height),
        #                   dpi=dpi, facecolor="#87CEFA", edgecolor='#87CEFA')
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形


data = "D:\Developer\JetBrains\www.jetbrains.com\JetBrainsDemo\PycharmP\Visualization\DataVisualization\chongqing\cq_pre-owned_house2.csv"

def forecast_plots():
    clean = forecast.get_clean(data)
    y, y_pred = forecast.get_price_forecast(clean)

    F = MyFigure(3, 3, 100)
    axes = F.fig.add_subplot(1, 1, 1)
    axes.plot(y, alpha=0.9, color='red')
    axes.plot(y_pred, alpha=0.9, color='blue')
    # 设置坐标名称
    axes.set_xlabel("房子数量", color='b', rotation=0, fontsize=14)
    axes.set_ylabel("房子总价", color='b', fontsize=14)
    axes.patch.set_facecolor('#87CEFA')
    axes.patch.set_facecolor('none')
    F.fig.suptitle("房价预测分析", color='b', fontsize=20)
    return F


def buildyears_averagePractice_plots():
    clean = plots.get_clean(data)
    x, y = plots.get_buildyears_averagePractice(clean)

    F = MyFigure(3, 3, 100)
    axes = F.fig.add_subplot(1, 1, 1)
    axes.plot(x, y, alpha=0.9, color='red')
    # 设置坐标名称
    axes.set_xlabel("房屋建成时间", color='b', rotation=0, fontsize=14)
    axes.set_ylabel("当年平均价 / 万", color='b', fontsize=14)
    axes.patch.set_facecolor('#87CEFA')
    axes.patch.set_facecolor('none')
    F.fig.suptitle("重庆近几十年建成均价走势图", color='b', fontsize=20)
    return F

def district_averagePractice_plots():
    clean = plots2.get_clean(data)
    x, y = plots2.get_district_averagePractice(clean)

    F = MyFigure(3, 3, 100)
    axes = F.fig.add_subplot(1, 1, 1)
    axes.plot(x, y, alpha=0.9, color='red')
    # 设置坐标名称
    axes.set_xlabel("区域", color='b', rotation=0, fontsize=14)
    axes.set_ylabel("均价", color='b', fontsize=14)
    axes.patch.set_facecolor('#87CEFA')
    axes.patch.set_facecolor('none')
    F.fig.suptitle("二手房均价分析", color='b', fontsize=20)
    return F


# 热门房型
def hot_portal_barh():
    clean = Bar.get_clean(data)
    x, y = Bar.get_hot_portal(clean)

    F = MyFigure(3, 3, 100)
    axes = F.fig.add_subplot(1, 1, 1)
    axes.barh(x, y, alpha=0.9, color='red')
    # 设置坐标名称
    axes.set_xlabel("均价", color='b', rotation=0, fontsize=14)
    axes.set_ylabel("户型", color='b', fontsize=14)
    axes.patch.set_facecolor('#87CEFA')
    axes.patch.set_facecolor('none')
    for y, x in enumerate(y):
        axes.text(x + 100, y, str(x) + '元/平', ha='left')
    F.fig.suptitle("二手房热门户型", color='b', fontsize=20)
    return F
    # plt.show()


# 显示均价条形图
def proportional_quantity_pie():
    clean = pie.get_clean(data)
    x, y = pie.get_proportional_quantity(clean)

    F = MyFigure(3, 3, 100)
    axes = F.fig.add_subplot(1, 1, 1)
    axes.pie(x, labels=y, labeldistance=1.1, autopct='%.1f%%',
             shadow=True, startangle=90, pctdistance=0.7)
    axes.patch.set_facecolor('#87CEFA')
    F.fig.suptitle("各地区销售数量", color='b', fontsize=20)
    return F
