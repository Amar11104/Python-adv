import pandas as pd
import streamlit as st


df = pd.DataFrame({
    'Name': ['Alice','Bob','John'],
    'Age': [23,23,45],
    'City': ['Paris','Paris','Paris']
})

st.write(df)