import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('medicine_dataset.csv')
    return df

df = load_data()

st.set_page_config(page_title="Medicine Dashboard", layout="wide")
st.title("💊 Medicine Data Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
category = st.sidebar.multiselect("Select Category", options=df['Category'].dropna().unique())
form = st.sidebar.multiselect("Select Dosage Form", options=df['Dosage Form'].dropna().unique())
classification = st.sidebar.multiselect("Select Classification", options=df['Classification'].dropna().unique())

# Apply filters
# Apply filters safely
mask = pd.Series([True] * len(df))

if category:
    mask &= df['Category'].isin(category)

if form:
    mask &= df['Dosage Form'].isin(form)

if classification:
    mask &= df['Classification'].isin(classification)

filtered_df = df[mask]

# Show filtered data
st.subheader("📋 Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# Dataset Summary
st.subheader("📊 Dataset Summary")
st.write(f"Total Records: {filtered_df.shape[0]}")
st.write(filtered_df.describe(include='all'))

# Visualizations
st.subheader("📈 Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Medicine Count by Category")
    category_counts = filtered_df['Category'].value_counts()
    fig1, ax1 = plt.subplots()
    category_counts.plot(kind='bar', ax=ax1, color='skyblue')
    st.pyplot(fig1)

with col2:
    st.markdown("### Dosage Form Distribution")
    dosage_counts = filtered_df['Dosage Form'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(dosage_counts, labels=dosage_counts.index, autopct='%1.1f%%', startangle=140)
    ax2.axis('equal')
    st.pyplot(fig2)

# Footer
st.markdown("---")

