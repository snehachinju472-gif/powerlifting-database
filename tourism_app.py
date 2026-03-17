import streamlit as st
import pandas as pd

st.title("🇮🇳 Indian Tourism Recommendation App")

# Load dataset
df = pd.read_csv("Top Indian Places to Visit.csv")

st.write("### Tourist Places Dataset")
st.dataframe(df)

# Sidebar filters
st.sidebar.header("Filter Tourist Places")

zone = st.sidebar.selectbox("Select Zone", df["Zone"].unique())
state = st.sidebar.selectbox("Select State", df["State"].unique())
place_type = st.sidebar.selectbox("Select Type", df["Type"].unique())

filtered_df = df[
    (df["Zone"] == zone) &
    (df["State"] == state) &
    (df["Type"] == place_type)
]

st.write("### Recommended Places")
st.dataframe(filtered_df)

# Show place details
if not filtered_df.empty:
    place = st.selectbox("Select Place", filtered_df["Name"])
    place_data = filtered_df[filtered_df["Name"] == place]

    st.write("### Place Details")
    st.write(place_data)
else:
    st.warning("No places found for this selection")
