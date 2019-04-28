'''
1 常用统计量
（1）随机生成1000个 [0,10000] 范围内的整数。
（2）求出数据中的中均值，众数，中位数，极差，标准差。
（3）对这些数据进行预处理，使其均值为零，方差为1。
（4）对（3）中预处理后的数据进行可视化显示（曲线形式，直方图形式等）
'''

from sklearn import preprocessing
import matplotlib.pyplot as plt
import random
import math

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False

data = []
for i in range(1, 1000):
    x = random.randrange(1, 10000, 1)
    data.append(x)

print(data)

sum = 0
for i in range(len(data)):
    sum += data[i]
average = sum/len(data)
print('均值：', average)

# 计算众数
num = {}
for i in range(len(data)):
    if data[i] in num.keys():
        num[data[i]] += 1
    else:
        num.setdefault(data[i], 1)
maxnum = 0
maxkey = 0
for k, v in num.items():
    if v > maxnum:
        maxnum = v
        maxkey = k
publicnum = maxkey
print('众数： ', publicnum)

# 计算中位数
listnum = [data[i] for i in range(len(data))]
listnum.sort()
lnum = len(data)
if lnum % 2 == 1:
    i = int((lnum + 1) / 2) - 1
    print('中位数为：', listnum[i])
else:
    i = int(lnum / 2) - 1
    print('中位数为：', (listnum[i] + listnum[i + 1]) / 2 )

# 极差
rangenumber = max(data) - min(data)
print('极差：', rangenumber)

# 标准差
ssum = 0
for i in range(len(data)):
    x = data[i]
    ssum += (x - average) ** 2
variance = ssum / len(data)
standard_deviation = math.sqrt(variance)
print('标准差为：', standard_deviation)

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

