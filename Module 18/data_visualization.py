import streamlit as st
import pandas as pd
import plotly.express as px

books_df = pd.read_csv('file1.csv')

#print(books_df)

st.title("Bestselling books analysis")
st.write("This app analysis the Amazon Top Selling books from 2009 tp 2022.")

st.subheader("Summary statistics")
total_books = books_df.shape[0]
unique_tittles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Title", unique_tittles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 nooks")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 autooks")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(books_df, names="Genre", title="Most Liked genre (2009-2022)",color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter Data by genre")
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]
st.write(filtered_df)