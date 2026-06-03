import streamlit as st
import pandas as pd
import plotly.express as px

books_df = pd.read_csv('file1.csv')

#print(books_df)

st.title("Bestselling books analysis")
st.write("This app analysis the Amazon Top Selling books from 2009 tp 2022.")

st.subheader("Summary statistics")
total_books = booksof.shape[0]
unique_tittles = books_df['Name'].nunique()