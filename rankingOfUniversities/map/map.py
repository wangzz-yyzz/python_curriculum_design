import folium
import numpy as np
import pandas as pd
import requests
from folium.plugins import HeatMap


def get_pos(address):
    """请求数据"""
    # 高德地图API
    url = "https://restapi.amap.com/v3/geocode/geo?key=" + "1d302a8b67fc817d0b8a89052b205f37" + "&address=" + address
    try:
        req = requests.get(url).json()
    except TimeoutError:
        req = get_pos(address)
    return req


def parse_result(result):
    """提取得到的经纬度数据"""
    lat = result['geocodes'][0]["location"].split(",")[1]
    lng = result['geocodes'][0]["location"].split(",")[0]
    return [lat, lng]


def draw(m: bool):
    """绘制热力分布地图"""
    if m:
        output_name = "省市分布地图.html"
        file_name = "province.csv"
    else:
        output_name = "省市分布地图-医药科.html"
        file_name = "province_medicine.csv"
    data = pd.read_csv(file_name)
    print(data)
    lat = []
    lng = []
    num = []

    # 获取经纬度
    for index, row in data.iterrows():
        res = parse_result(get_pos(row["省市"]))
        print(res)
        lat.append(res[0])
        lng.append(res[1])
        num.append(row["上榜数量"])

    # 绘制地图
    lat = np.array(lat, dtype=float)
    lng = np.array(lng, dtype=float)
    num = np.array(num, dtype=float)
    data = [[lat[i], lng[i], num[i]] for i in range(len(num))]
    map_osm = folium.Map(location=[35, 110], zoom_start=5)
    HeatMap(data).add_to(map_osm)
    file_path = output_name
    map_osm.save(file_path)
