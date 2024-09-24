import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 设置标题
st.title('California Housing Data (1990)')

# 读取数据
df = pd.read_csv('housing.csv')

# 过滤器：最低房价
price_filter = st.slider('Minimal median Housing Price', 0, 500001, 200000)

# 过滤器：位置类型
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df['ocean_proximity'].unique(),  # 选项
    df['ocean_proximity'].unique())  # 默认值为所有选项

# 过滤器：收入水平
income_level = st.radio("Select Income level:", ('Low', 'Medium', 'High'))

# 根据收入水平过滤
if income_level == 'Low':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] >= 4.5]

# 根据房价和位置过滤数据
df = df[df['median_house_value'] >= price_filter]
df = df[df['ocean_proximity'].isin(location_filter)]

# 显示地图
st.map(df)

