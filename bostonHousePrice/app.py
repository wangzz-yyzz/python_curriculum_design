from sklearn.datasets import load_boston


def loadData():
    dataset = load_boston()
    x_data = dataset.data  # 导入所有特征变量
    y_data = dataset.target  # 导入目标值（房价）
    name_data = dataset.feature_names  # 导入特征名
    return x_data, y_data, name_data


def main():
    x_data, y_data, name_data = loadData()


if __name__ == '__main__':
    main()