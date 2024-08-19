#Dashboard jalankan di file .py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Membaca file CSV data pertanyaan 1
all_df = pd.read_csv("customers_dataset_fix.csv")

# Fungsi untuk membuat DataFrame yang dikelompokkan berdasarkan state
def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    return bystate_df

# Membuat DataFrame berdasarkan state
bystate_df = create_bystate_df(all_df)

# Membuat header dashboard
st.header('Dashboard Customer')

# Membuat plot
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count", 
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customer by States", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

# Menampilkan plot di aplikasi Streamlit
st.pyplot(fig)

# Membaca file CSV data pertanyaan 2
all_df = pd.read_csv("order_reviews_dataset_fix.csv")

# Fungsi untuk membuat DataFrame yang dikelompokkan berdasarkan kepuasan
def create_byrecomend_df(df):
    byrecomend_df = df.groupby(by="review_comment_title").order_id.nunique().reset_index()
    byrecomend_df.rename(columns={
        "order_id": "customer_count"
    }, inplace=True)
    return byrecomend_df


# Fungsi untuk membuat DataFrame yang dikelompokkan berdasarkan tahun
def create_byyear_df(df):
    byyear_df = df.groupby(by="year").order_id.nunique().reset_index()
    byyear_df.rename(columns={
        "order_id": "customer_count"
    }, inplace=True)
    return byyear_df

# Fungsi untuk membuat DataFrame yang dikelompokkan berdasarkan bulan
def create_bymonth_df(df):
    bymonth_df = df.groupby(by="month").order_id.nunique().reset_index()
    bymonth_df.rename(columns={
        "order_id": "customer_count"
    }, inplace=True)
    return bymonth_df

# Membuat DataFrame berdasarkan tahun dan bulan
byyear_df = create_byyear_df(all_df)
bymonth_df = create_bymonth_df(all_df)
byrecomend_df = create_byrecomend_df(all_df)

# Plot untuk grafik batang rekomendasi
st.subheader('Number of Customers by rekomendasi')
fig, ax = plt.subplots(figsize=(10, 6))
colors = sns.color_palette("Blues_d", len(byrecomend_df))  
sns.barplot(
    x="review_comment_title", 
    y="customer_count",
    data=byrecomend_df,
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customers by Year", loc="center", fontsize=20)
ax.set_xlabel("review_comment_title", fontsize=14)
ax.set_ylabel("Number of Customers", fontsize=14)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Plot untuk grafik batang tahunan
st.subheader('Number of Customers by Year')
fig, ax = plt.subplots(figsize=(10, 6))
colors = sns.color_palette("Blues_d", len(byyear_df)) 
sns.barplot(
    x="year", 
    y="customer_count",
    data=byyear_df,
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customers by Year", loc="center", fontsize=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Customers", fontsize=14)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Plot untuk grafik batang bulanan
st.subheader('Number of Customers by Month')
fig, ax = plt.subplots(figsize=(12, 8))
# Mengatur urutan bulan jika data bulan dalam format angka
bymonth_df['month'] = pd.Categorical(bymonth_df['month'], categories=range(1, 13), ordered=True)
bymonth_df = bymonth_df.sort_values('month')
colors = sns.color_palette("viridis", len(bymonth_df)) 
sns.barplot(
    x="month", 
    y="customer_count",
    data=bymonth_df,
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customers by Month", loc="center", fontsize=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Number of Customers", fontsize=14)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)