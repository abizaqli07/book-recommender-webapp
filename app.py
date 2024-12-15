
import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System - Big Data Final Project')
popular_df = pickle.load(open('artifacts/popular.pkl','rb'))
pt = pickle.load(open('artifacts/pt.pkl','rb'))
books = pickle.load(open('artifacts/books.pkl','rb'))
similarity_scores = pickle.load(open('artifacts/similarity_scores.pkl','rb'))     

def recommend_book(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-L'].values))

        data.append(item)
        
    return data



selected_books = st.text_input(
    "Type book title",
)

if st.button('Show Recommendation'):
    data = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(data[0][1])
        st.image(data[0][2])
    with col2:
        st.text(data[1][1])
        st.image(data[1][2])
    with col3:
        st.text(data[2][1])
        st.image(data[2][2])
    with col4:
        st.text(data[3][1])
        st.image(data[3][2])








