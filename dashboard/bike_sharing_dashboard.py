import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour_df = pd.read_csv("hour.csv")

hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

st.sidebar.header("Filter Data")
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca", sorted(hour_df["weathersit"].unique()))
selected_hour = st.sidebar.slider("Pilih Jam", 0, 23, (0, 23))

st.title("Bike Sharing Dashboard")
st.write("Analisis penyewaan sepeda berdasarkan kondisi cuaca dan waktu.")

# Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
weather_table = hour_df.groupby("weathersit")["cnt"].mean()

fig, ax = plt.subplots()
sns.barplot(x=weather_table.index, y=weather_table, palette="Blues", edgecolor="black", ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# Jam Puncak Penyewaan Sepeda
st.subheader("jam Puncak Penyewaan Sepeda")
hourly_table = hour_df.groupby("hr")["cnt"].sum().reset_index()
peak_hour = hourly_table.loc[hourly_table["cnt"].idxmax(), "hr"]

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(x=hourly_table["hr"], y=hourly_table["cnt"], marker='o', color='blue', ax=ax)
ax.axvline(peak_hour, color='red', linestyle='--', label=f'Puncak: Jam {peak_hour}')
ax.set_xlabel("Jam")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Penyewaan Sepeda per Jam")
ax.legend()
st.pyplot(fig)

# Data yang Difilter
st.subheader("Data yang Dipilih")
filtered_data = hour_df[(hour_df["weathersit"] == selected_weather) & (hour_df["hr"].between(*selected_hour))]
st.write(filtered_data)

st.write("Dashboard ini dibuat dengan **Streamlit** untuk eksplorasi data penyewaan sepeda.")
