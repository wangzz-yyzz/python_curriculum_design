import pandas as pd


def getProvinceData(m: bool):
    if m:
        output_name = "province.csv"
        file_name = "data.csv"
    else:
        output_name = "province_medicine.csv"
        file_name = "data_medicine.csv"
    data = pd.read_csv(file_name)
    province_data = data["省市"].value_counts()
    # 转换成DataFrame
    province_dict = {"省市": province_data.index, "上榜数量": province_data.values}
    province_data = pd.DataFrame(province_dict)

    province_data.to_csv(output_name)
