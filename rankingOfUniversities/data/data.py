import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/67.0.3396.99 Safari/537.36'}
base_url = ["https://www.shanghairanking.cn/rankings/bcur/202011", "https://www.shanghairanking.cn/rankings/bcur/202021"]

# css选择器
css_sel = {"排名": "#content-box > div.rk-table-box > table > tbody > tr > td:nth-child(1)",
           "学校名称": "#content-box > div.rk-table-box > table > tbody > tr > td.align-left > a",
           "省市": "#content-box > div.rk-table-box > table > tbody > tr > td:nth-child(3)",
           "类型": "#content-box > div.rk-table-box > table > tbody > tr > td:nth-child(4)",
           "总分": "#content-box > div.rk-table-box > table > tbody > tr > td:nth-child(5)"}


def getData(m: bool):
    if m:
        url = base_url[0]
        file_name = "data.csv"
    else:
        url = base_url[1]
        file_name = "data_medicine.csv"
    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'
    res = BeautifulSoup(res.text, "lxml")
    data = {}

    for key in css_sel.keys():
        if key != "学校名称":
            ans = res.select(css_sel[key])
            for i in range(len(ans)):
                # 定位到文字内容，先替换后正则提取
                ans[i] = str(ans[i]).replace(" ", "").replace("<!---->", "").replace("\n", "")
                ans[i] = re.findall(r'<td.*?>(.*?)</td>', ans[i])
                ans[i] = ans[i][0]
        else:
            # 无需正则提取
            ans = res.select(css_sel[key])
            for i in range(len(ans)):
                ans[i] = ans[i].string
        # 将字段保存至字典
        data[key] = ans

    # 保存数据
    data = pd.DataFrame(data)
    print("Done")
    data.to_csv(file_name)