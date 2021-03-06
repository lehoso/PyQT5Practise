# 导入模块
import pandas as pd  # 导入数据统计模块
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt  # 导入绘图模块


# 避免中文乱码
class pie:
    def get_clean(data):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
        matplotlib.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符，使用rc配置文件来自定义
        # 简单清洗
        data = pd.read_csv(data)  # 读取csv数据
        # del data['Unnamed: 0']  # 将索引列删除
        data.dropna(axis=0, how='any', inplace=True)  # 删除data数据中的所有空值
        data['单价每平'] = data['单价每平'].map(lambda d: d.replace('元/平', ''))  # 将单价每平“元/平米”去掉
        data['单价每平'] = data['单价每平'].map(lambda d: d.replace(',', ''))  # 将单价每”平“元/平米去掉
        data['单价每平'] = data['单价每平'].astype(float)  # 将房子单价每平转换为浮点类型，float（data['',单价每平]）
        data['面积'] = data['面积'].map(lambda p: p.replace('平米', ''))  # 将面积“平米去掉”
        data['面积'] = data['面积'].astype(float)  # 将将面积转换为浮点类型
        return data

    # 获取各区二手房各区比例数量，进一步处理数据，如果要写相应算法，需要根据算法所需求的数据处理
    def get_proportional_quantity(data):
        area = data['区域'].groupby(data['区域']).count()  # 将房子区域分组比例数量
        areaName = (area).index.values  # 将房子区域分组比例取名
        return area, areaName

    # 显示均价条形图
    def proportional_quantity_pie(area, areaName, title):
        plt.figure()  # 图形画布
        plt.pie(area, labels=areaName, labeldistance=1.1, autopct='%.1f%%',
                shadow=True, startangle=90, pctdistance=0.7)
        plt.title(title, fontsize=24)  # 表标题文字
        plt.legend(bbox_to_anchor=(-0.1, 1))  # 作者标题
        plt.show()

    def transfer(data):
        data = pie.get_clean(data)
        area, areaName = pie.get_proportional_quantity(data)
        title = '各区二手房数量所占比比例'
        pie.proportional_quantity_pie(area, areaName, title)

# if __name__ == '__main__':
#     # 对应x，y
#     area, areaName =pie.get_proportional_quantity()
#     title = '各区二手房数量所占比比例'
#     pie.proportional_quantity_pie(area, areaName, title)
