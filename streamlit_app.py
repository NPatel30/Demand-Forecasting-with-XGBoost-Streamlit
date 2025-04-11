
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load forecast results
df = pd.read_csv("xgboost_forecast_results.csv")

st.title("📈 XGBoost Forecast Viewer")

# Select volatility segment
segment = st.selectbox("Select Volatility Segment", df['Volatility_Segment'].unique())
products = df[df['Volatility_Segment'] == segment]['Product_Code'].unique()

# Select product
product = st.selectbox("Select Product", products)

# Filter and plot
data = df[(df['Volatility_Segment'] == segment) & (df['Product_Code'] == product)]

st.line_chart(data.set_index('Week_Index')['Forecasted_Sales'])
