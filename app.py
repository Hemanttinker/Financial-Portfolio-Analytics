import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="Algorithmic Portfolio Intelligence Engine", layout="wide")

st.title("📊 Algorithmic Portfolio Intelligence Engine")
st.markdown("### *End-to-End Financial Portfolio Analytics & Risk Infrastructure*")
st.write("---")

# 1. Simple Data Framework (No Cache, No Lag)
np.random.seed(42)
n_records = 500  # Kept small for instant rendering

assets = {
    'Stocks': ['RELIANCE', 'TCS', 'INFY', 'HDFC'],
    'Crypto': ['BTC', 'ETH'],
    'Gold': ['GOLD_ETF'],
    'Bonds': ['GOVT_BOND_10Y']
}

data = []
start_date = datetime(2024, 1, 1)

for i in range(n_records):
    asset_type = np.random.choice(list(assets.keys()), p=[0.5, 0.2, 0.15, 0.15])
    ticker = np.random.choice(assets[asset_type])
    action = np.random.choice(['BUY', 'SELL'], p=[0.6, 0.4])
    quantity = np.random.randint(1, 50) if asset_type != 'Crypto' else round(np.random.uniform(0.01, 0.5), 4)
    price = round(np.random.uniform(100, 3000), 2) if asset_type != 'Crypto' else round(np.random.uniform(30000, 60000), 2)
    random_days = np.random.randint(0, 500)
    tx_date = start_date + timedelta(days=random_days)
    total_amount = round(quantity * price, 2)
    data.append([tx_date, asset_type, ticker, action, quantity, price, total_amount])

df = pd.DataFrame(data, columns=['Date', 'Asset_Class', 'Ticker', 'Action', 'Quantity', 'Price', 'Total_Amount'])

# 2. Sidebar Filter Framework
st.sidebar.header("📊 Filter Framework")
selected_assets = st.sidebar.multiselect("Select Asset Classes", options=df['Asset_Class'].unique(), default=df['Asset_Class'].unique())
filtered_df = df[df['Asset_Class'].isin(selected_assets)]

# 3. Aggregation Engine
buys = filtered_df[filtered_df['Action'] == 'BUY']
sells = filtered_df[filtered_df['Action'] == 'SELL']

buy_agg = buys.groupby(['Asset_Class', 'Ticker']).agg(Total_Bought_Value=('Total_Amount', 'sum'), Total_Quantity_Bought=('Quantity', 'sum')).reset_index()
sell_agg = sells.groupby(['Asset_Class', 'Ticker']).agg(Total_Sold_Value=('Total_Amount', 'sum'), Total_Quantity_Sold=('Quantity', 'sum')).reset_index()

portfolio_summary = pd.merge(buy_agg, sell_agg, on=['Asset_Class', 'Ticker'], how='left').fillna(0)
portfolio_summary['Current_Quantity'] = portfolio_summary['Total_Quantity_Bought'] - portfolio_summary['Total_Quantity_Sold']
portfolio_summary['Net_Invested_Capital'] = portfolio_summary['Total_Bought_Value'] - portfolio_summary['Total_Sold_Value']

active_portfolio = portfolio_summary[portfolio_summary['Current_Quantity'] > 0].copy()
total_portfolio_value = active_portfolio['Net_Invested_Capital'].sum()

# 4. KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Portfolio Valuation", value=f"₹{total_portfolio_value:,.2f}")
with col2:
    st.metric(label="Active Tickers", value=len(active_portfolio))
with col3:
    st.metric(label="Processed Logs", value=len(filtered_df))

st.write("---")

# 5. Visualizations
col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    st.markdown("#### **Asset Class Diversification Ratio**")
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    if not active_portfolio.empty:
        asset_allocation = active_portfolio.groupby('Asset_Class')['Net_Invested_Capital'].sum()
        ax1.pie(asset_allocation, labels=asset_allocation.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
        st.pyplot(fig1)

with col_chart2:
    st.markdown("#### **Capital Concentration Per Ticker**")
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    if not active_portfolio.empty:
        sns.barplot(x='Net_Invested_Capital', y='Ticker', hue='Asset_Class', data=active_portfolio.sort_values(by='Net_Invested_Capital', ascending=False), ax=ax2, palette="viridis")
        st.pyplot(fig2)

st.write("---")
st.markdown("#### 📂 Master Active Holdings Data")
st.dataframe(active_portfolio[['Asset_Class', 'Ticker', 'Current_Quantity', 'Net_Invested_Capital']], use_container_width=True)