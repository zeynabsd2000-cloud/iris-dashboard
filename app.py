import streamlit as st
import pandas as pd
from charts import *
from filters import apply_filters

# Page settings
st.set_page_config(
    page_title="Iris Flower Dashboard",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data/iris_dataset.csv")

# Assign column names
df.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

# Dashboard title
st.title("🌸 Iris Flower Data Analysis Dashboard")
st.write("Interactive dashboard for Iris flower dataset analysis.")

# ==========================
# SIDEBAR FILTERS
# ==========================

st.sidebar.header("Filters")

species = st.sidebar.multiselect(
    "Select Species",
    options=df["species"].unique(),
    default=df["species"].unique()
)

# Apply species filter
filtered_df = apply_filters(df, species)

# Numerical slider filter
min_length = st.sidebar.slider(
    "Minimum Sepal Length",
    min_value=float(df["sepal_length"].min()),
    max_value=float(df["sepal_length"].max()),
    value=float(df["sepal_length"].min())
)

filtered_df = filtered_df[
    filtered_df["sepal_length"] >= min_length
]

# ==========================
# KPI CARDS
# ==========================

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    len(filtered_df)
)

col2.metric(
    "Average Sepal Length",
    round(filtered_df["sepal_length"].mean(), 2)
)

col3.metric(
    "Average Petal Length",
    round(filtered_df["petal_length"].mean(), 2)
)

st.markdown("---")

# ==========================
# CHARTS
# ==========================

st.subheader("1. Pie Chart")
st.pyplot(pie_chart(filtered_df))

st.subheader("2. Histogram")
st.pyplot(histogram(filtered_df))

st.subheader("3. Scatter Plot")
st.pyplot(scatter(filtered_df))

st.subheader("4. Heatmap")
st.pyplot(heatmap(filtered_df))

st.subheader("5. Box Plot")
st.pyplot(boxplot(filtered_df))

st.subheader("6. Bar Chart")
st.pyplot(bar_chart(filtered_df))

st.subheader("7. Line Chart")
st.pyplot(line_chart(filtered_df))

st.subheader("8. Area Chart")
st.pyplot(area_chart(filtered_df))

st.subheader("9. Count Plot")
st.pyplot(count_plot(filtered_df))

st.subheader("10. Violin Plot")
st.pyplot(violin_plot(filtered_df))