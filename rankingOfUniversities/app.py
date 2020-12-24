import rankingOfUniversities.province.province as province
import rankingOfUniversities.map.map as my_map
import rankingOfUniversities.map.barchart as chart
import rankingOfUniversities.data.data as data

if __name__ == '__main__':
    # # 主榜单分析
    # # 获取数据
    # data.getData(m=True)
    # # 获取各省份上榜数量数据
    # province.getProvinceData(m=True)
    # # 绘制热力分布地图
    # my_map.draw(m=True)
    #
    # # 医药类榜单分析
    # data.getData(m=False)
    # province.getProvinceData(m=False)
    # my_map.draw(m=False)
    #
    # # 绘制前10名的柱状图
    # chart.draw(m=True)
    # chart.draw(m=False)
    my_map.draw(m=False)