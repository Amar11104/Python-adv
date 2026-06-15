import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv("file1.csv")

st.title("Best selling Books Analysis")
st.write("This app")

st.sidebar.header("add ")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("user RAting", 0.0, 5.0,0.0,0.1)
    new_reviews = st.number_input("reviews", min_value=0,step=1)
    new_year = st.number_input("Year", min_value=2009,max_value=2022, step=1)
    new_genre = st.selectbox("genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
        new_data = {
            'Name': new_name,
            'Author': new_author,
            'User Rating': new_user_rating,
            'Reviews': new_reviews,
            'Price': new_price,
            'Year': new_year,
            'Genre': new_genre
        }

        books_df = pd.concat([pd.DataFrame(new_data,index=[0]),books_df], ignore_index=True)
        books_df.to_csv('file1.csv',index=False)
        st.sidebar.success("New Book Added successfully")

