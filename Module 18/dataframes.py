import pandas as pd
import streamlit as st

st.header('Dispalying dataframes')

data = pd.DataFrame({
    'Name': ['Alice','Bob','John','David','Amar'],
    'Age':[24,27,30,34,20],
    'City': ['New York','Paris','Prishtine','Huston','Berlin']
})

st.dataframe(data)