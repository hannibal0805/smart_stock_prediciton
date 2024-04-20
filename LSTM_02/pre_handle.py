import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 读取贵州茅台日k线数据到变量maotai
maotai = pd.read_csv('./SH600519.csv')  # 读取股票文件

# 把变量maotai中前2126天数据中的开盘价作为训练数据，后300天数据中的开盘价作为测试数据
# [0,2126)   前(2426-300=2126)天的开盘价作为训练集，表格从0开始计数（0从第一行数据开始，不是列名）
# 2:3是提取[2,3)列，前闭后开，故提取出C列开盘价
training_set = maotai.iloc[0:2426 - 300, 2:3].values
test_set = maotai.iloc[2426 - 300:, 2:3].values   # 后300天的开盘价作为测试集

# 对开盘价进行归一化，使送入神经网络的数据分布在0-1之间
sc = MinMaxScaler(feature_range=(0, 1))  # 定义归一化：归一化到(0，1)之间
'''
fit的本质是生成min和max
transform是通过接口导出结果
fit_transform是一步达成训练和导出结果
'''
training_set_scaled = sc.fit_transform(training_set)  # 求得训练集的最大值、最小值这些训练集固有属性，并在训练集上进行归一化
test_set = sc.transform(test_set)  # 利用训练集的属性对测试集进行归一化

# 建立空列表，分别用于接收训练集输入特征、训练集标签、测试集输入特征、测试集标签
x_train = []
y_train = []
x_test = []
y_test = []

# 训练集：csv表格中前2426-300=2126天数据
# 提取训练集中连续60天的开盘价作为输入特征x_train，第61天的数据作为标签y_train
# for循环共构建2426-300-60=2066组训练数据
for i in range(60, len(training_set_scaled)):   # 利用for循环，遍历整个训练集
    x_train.append(training_set_scaled[i - 60:i, 0])
    y_train.append(training_set_scaled[i, 0])

# 对训练集进行打乱
np.random.seed(7)
np.random.shuffle(x_train)
np.random.seed(7)
np.random.shuffle(y_train)
tf.random.set_seed(7)

# 将训练集由list格式变为array格式
x_train, y_train = np.array(x_train), np.array(y_train)

# 使x_train符合RNN输入要求：[送入样本数，循环核时间展开步数，每个时间步输入特征个数]
# 此处整个数据集送入，送入样本数为x_train.shape[0]即2066组数据；
# 输入60个开盘价，预测出第61天的开盘价，循环核时间展开步数为60；
# 每个时间步送入的特征是某一天的开盘价，只有1个数据，故每个时间步输入特征个数为1
x_train = np.reshape(x_train, (x_train.shape[0], 60, 1))

# 测试集：csv表格中后300天数据
# 提取测试集中连续60天的开盘价作为输入特征x_test，第61天的数据作为标签
# for循环共构建300-60=240组数据
for i in range(60, len(test_set)):   # 利用for循环，遍历整个测试集
    x_test.append(test_set[i - 60:i, 0])
    y_test.append(test_set[i, 0])

# 测试集不需要打乱顺序
# 测试集变array并reshape为符合RNN输入要求：[送入样本数，循环核时间展开步数，每个时间步输入特征个数]
x_test, y_test = np.array(x_test), np.array(y_test)
x_test = np.reshape(x_test, (x_test.shape[0], 60, 1))