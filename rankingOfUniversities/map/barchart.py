import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def draw(m: bool):
    if m:
        file_name = "province.csv"
        output_name = "前10名.png"
    else:
        file_name = "province_medicine.csv"
        output_name = "前10名-医药类.png"
    data = pd.read_csv(file_name)
    # 取前10条数据
    data = data.head(10)

    # 绘制柱状图
    plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig = sns.barplot(data=data, x="省市", y="上榜数量").get_figure()
    plt.show()
    # 保存图片
    fig.savefig(output_name)
    print("bar chart Done")
