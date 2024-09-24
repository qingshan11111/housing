import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Minimal median Housing Price', 0, 500001, 200000)
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df['ocean_proximity'].unique(),  # options
    df['ocean_proximity'].unique()) 

income_level = st.radio("select Income level:",('Low','Medium','High'))

if income_level == 'Low(<=2.5)':
    filtered_df=df[df['median income']<= 2.5]
elif income_level =='Medium(> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income']>2.5)& (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median income'] > 4.5]

df = df[df.median_house_value >= price_filter]
df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low(<=2.5)':
    filtered_df = df[df('median_income')<= 2.5]
elif income_level == 'Medium(>2.5 & < 4.5)':
    filtered_df = df[(df('medium_income')>2.5) & (df('medium_income')<4.5) ]
else:
    filtered_df = df[df('median_income')>4.5]
# show on map
st.map(df)

