import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f704221a234666a982eda1fba5f62c44&language=en-US'.format(movie_id))
    #response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=f704221a234666a982eda1fba5f62c44&language=en-US'.format(movie_id))
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster for API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

movie_dict=pickle.load(open("MovieRecommender_dict.pkl","rb"))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open("similarity.pkl","rb"))

st.title('Movie Recommender System')


selected_movie_name= st.selectbox(
"Select/enter the movie name, on that i will recommend you",
movies['title'].values)


if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    """Recommendations = recommend(selected_movie_name)
    for i  in Recommendations:
        st.write(i)
"""
    """for name, poster in zip(names, posters):
        st.header(name)
        st.image(poster, width=200, use_column_width=True)  # Adjusted width and use_column_width parameter
"""
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0], width=200, use_column_width=True)
    with col2:
        st.text(names[1])
        st.image(posters[1], width=200, use_column_width=True)
    with col3:
        st.text(names[2])
        st.image(posters[2], width=200, use_column_width=True)
    with col4:
        st.text(names[3])
        st.image(posters[3], width=200, use_column_width=True)
    with col5:
        st.text(names[4])
        st.image(posters[4], width=200, use_column_width=True)