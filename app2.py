import streamlit as st
import pandas as pd

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Powerlifting Data Analysis",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ Powerlifting Meets Data Analysis")
st.write("Interactive analysis of powerlifting competition data")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("meets.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df

df = load_data()

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔎 Filter Options")

federation = st.sidebar.multiselect(
    "Select Federation",
    options=df["Federation"].dropna().unique(),
    default=df["Federation"].dropna().unique()
)

country = st.sidebar.multiselect(
    "Select Country",
    options=df["MeetCountry"].dropna().unique(),
    default=df["MeetCountry"].dropna().unique()
)

state = st.sidebar.multiselect(
    "Select State",
    options=df["MeetState"].dropna().unique(),
    default=df["MeetState"].dropna().unique()
)

# Apply filters
filtered_df = df[
    (df["Federation"].isin(federation)) &
    (df["MeetCountry"].isin(country)) &
    (df["MeetState"].isin(state))
]

# -------------------------------
# Dataset Overview
# -------------------------------
st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Meets", filtered_df.shape[0])
col2.metric("Federations", filtered_df["Federation"].nunique())
col3.metric("Countries", filtered_df["MeetCountry"].nunique())

# -------------------------------
# Data Preview
# -------------------------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head(20), use_container_width=True)

# -------------------------------
# Meets by Year
# -------------------------------
st.subheader("📅 Meets Over Time")

yearly_meets = (
    filtered_df
    .dropna(subset=["Date"])
    .groupby(filtered_df["Date"].dt.year)
    .size()
)

st.line_chart(yearly_meets)

# -------------------------------
# Federation Distribution
# -------------------------------
st.subheader("🏆 Federation Distribution")

fed_counts = filtered_df["Federation"].value_counts()
st.bar_chart(fed_counts)

# -------------------------------
# Location Analysis
# -------------------------------
st.subheader("🌍 Top Meet Locations")

col1, col2 = st.columns(2)

with col1:
    st.write("Top Countries")
    st.dataframe(filtered_df["MeetCountry"].value_counts().head(10))

with col2:
    st.write("Top States")
    st.dataframe(filtered_df["MeetState"].value_counts().head(10))


