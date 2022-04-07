import pandas as pd
import streamlit as st
import pickle

movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies_dict = pickle.load(open('movie_list_to_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies_list['title'].values
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox('Which movie would you like to search', movies_list)
#st.text(movies)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []

    for i in movies_list:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names


if st.button('Search'):
    st.text('Recommended movies are')
    st.write(selected_movie_name)
    recommendation_movies = recommend(selected_movie_name)
    for i in recommendation_movies:
        st.write(i)
