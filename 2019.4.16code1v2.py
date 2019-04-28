'''
1 常用统计量
（1）随机生成1000个 [0,10000] 范围内的整数。
（2）求出数据中的中均值，众数，中位数，极差，标准差。
（3）对这些数据进行预处理，使其均值为零，方差为1。
（4）对（3）中预处理后的数据进行可视化显示（曲线形式，直方图形式等）
'''

import numpy as np
from scipy import stats
from sklearn import preprocessing
import matplotlib.pyplot as plt

data = np.random.randint(0, 10000, size=1000)
print('全部数据为：\n', data)

# 均值
average = np.mean(data)
print('均值：', average)

# 众数
counts = np.bincount(data)
argmaxcount1 = np.argmax(counts)
argmaxcount2 = stats.mode(data)[0][0]
print('方法一求出的众数：', argmaxcount1)
print('方法二求出的众数：', argmaxcount2)

# 中位数
medianumber = np.median(data)
print('中位数：', medianumber)

# 极差
ptp = np.ptp(data)
print('极差：', ptp)

# 标准差
standard = np.std(data)
print('标准差：', standard)

# 对这些数据进行预处理，使其均值为零，方差为1
data_preprocess = preprocessing.scale(data)
print(data_preprocess)
print('处理后的数据方差为：', data_preprocess.std())

# 曲线形式，直方图形式
plt.hist(data_preprocess, bins=40, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
plt.xlabel("随机数据的区间")
plt.ylabel("随机数据频数/频率")
plt.title("随机生成数据的频数直方图")
plt.show()