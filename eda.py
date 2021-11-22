#Import Libraries/Packages
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Remove warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

#Write title and subheader for the App
st.title("Exploratory Data Analysis App")
st.subheader("Exploratory Data Analysis with Streamlit")

with st.sidebar.header('Upload CSV File'):
    uploaded_file = st.sidebar.file_uploader("Upload your CSV data")

#Improve speed and cache data
if uploaded_file is not None:
    @st.cache(persist=True)
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    data = load_csv()

    #Display Dataset
    if st.checkbox("Preview Data"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
    else:
        st.write(data.head(3))

    #Show entire dataset
    if st.checkbox("Show All DataFrame"):
        st.dataframe(data)

    #Show description
    if st.checkbox("Show Summary of Dataset"):
        if st.button("Duplicate Rows"):
            duplicate = data.duplicated()
            st.write(data[duplicate])
        if st.button("All Column"):
            st.text("Columns:")
            st.write(data.columns)
        if st.button("Description of the Dataset"):
            st.write(data.describe())
        if st.button("Description for Categorical Column"):
            st.text(data.describe(include=['object']))
            
        if st.button("Missing Values"):
            st.text("Number of Missing Value:")
            st.write((data.isna().sum()).sum())

    #Check Correlation
    if st.checkbox("Correlation"):
        plt.figure(figsize=(15,10))
        st.write(sns.heatmap(data.corr(), annot=True))
        st.pyplot()
        st.write(sns.pairplot(data.iloc[:,0:5], corner=True))
        st.pyplot()

    #Check Outliers
    if st.checkbox("Boxplot"):
        st.text("Check Outlier with Boxplot")
        plt.figure(figsize=(15,10))
        st.write(data.iloc[:,0:5].boxplot())
        st.pyplot()