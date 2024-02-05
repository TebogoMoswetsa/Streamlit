# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:35:10 2024

@author: tebog
"""
import pandas as pd
import streamlit as st


#importing the data from an csv file
data = pd.read_csv("country_data_index.csv")
df = pd.DataFrame(data)
#Displaying the data in the table format
st.dataframe(df)

#Plotting a graph using the data from the table
yAxis = df['Age']
xAxis = df['Country']


st.line_chart(df[["Age", "Country"]])
st.line_chart(df[[ "Country"]])
st.line_chart(df[["Age"]])
