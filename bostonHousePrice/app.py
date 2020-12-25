import matplotlib.pyplot as plt
from numpy import *
from sklearn import preprocessing
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

dataset = load_boston()
x_data = dataset.data  # 导入所有特征变量
y_data = dataset.target  # 导入目标值（房价）
name_data = dataset.feature_names  # 导入特征名

for i in range(13):
    plt.figure()
    plt.scatter(x_data[:, i], y_data, s=20)
    plt.title(name_data[i])
    plt.savefig("boston_param_" + name_data[i])

x_data = dataset.data
y_data = dataset.target

# 随机选择25%的数据构建测试样本，剩余作为训练样本
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, random_state=0, test_size=0.25)

# 数据标归一化处理
# 分别初始化对特征和目标值的标准化器
min_max_scaler = preprocessing.MinMaxScaler()
# 分别对训练和测试数据的特征以及目标值进行标准化处理
X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.fit_transform(X_test)
y_train = min_max_scaler.fit_transform(y_train.reshape(-1, 1))  # reshape(-1,1)指将它转化为1列，行自动确定
y_test = min_max_scaler.fit_transform(y_test.reshape(-1, 1))  # reshape(-1,1)指将它转化为1列，行自动确定

# 使用线性回归模型LinearRegression对波士顿房价数据进行训练及预测
lr = LinearRegression(n_jobs=4, normalize=True, fit_intercept=True)
# 使用训练数据进行参数估计
lr.fit(X_train, y_train)
# 回归预测
lr_y_predict = lr.predict(X_test)

mse_score = mean_squared_error(y_test, lr_y_predict)
print("mse: ", mse_score)

print('Coefficients:', lr.coef_)
# 查看回归方程截距
print('intercept', lr.intercept_)

plt.figure(figsize=(30, 10))
plt.plot(range(len(y_test)), y_test, color='red', label="real")
plt.plot(range(len(y_test)), lr_y_predict, color='blue', label="predict")
plt.xlabel('X')
plt.ylabel('Price')
plt.legend(loc='lower left')
plt.savefig("predict.png")

plt.figure(figsize=(30, 10))
plt.scatter(range(len(y_test)), y_test, color='red', label="real")
plt.plot(range(len(y_test)), lr_y_predict, color='blue', label="predict")
plt.xlabel('X')
plt.ylabel('Price')
plt.legend(loc='lower left')
plt.savefig("predict-scatter.png")

time = np.arange(0, 50).reshape(50, 1)
plt.figure(figsize=(20, 10))
plt.plot(time, y_test[0: 50], color='red', label="real")
plt.plot(time, lr.predict(X_test)[0: 50], color='blue', label="predict")
plt.xlabel('X')
plt.ylabel('Price')
plt.legend(loc='lower left')
plt.savefig("predict-small.png")
