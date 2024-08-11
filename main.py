import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Flight Log Analysis")


uploaded_file = st.file_uploader("Choose a CSV file ",type=['csv', 'xls'] )

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # st.write("File Uploaded....")


    st.subheader("Data Preview")
    st.write(df.head())


    st.subheader("Data Summary")
    st.write(df.describe())

    


    


    






