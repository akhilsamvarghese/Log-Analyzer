import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page title
st.set_page_config(page_title="Log Analyzer", layout="wide")

# Title
st.title("Log Analyzer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Preview of the data:")
    st.write(df.head())


    st.subheader("Data Summary")
    st.write(df.describe())

    


    


    






