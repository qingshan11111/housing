import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('housing.csv')

# 创建一个直方图，bins 参数设置为30
plt.figure(figsize=(10, 6))
plt.hist(data['median_house_value'], bins=30, range=(200000, 500001),edgecolor='black')
plt.style.use('seaborn-v0_8')
# 添加标题和标签
plt.title('Histogram of Median House Values')
plt.xlabel('Median House Value ($)')
plt.ylabel('Frequency')

# 显示图形
plt.show()