import streamlit as st
import pickle
import pandas as pd
import requests

# Load the movies dictionary and similarity matrix
movies_list = pickle.load(open('movies-dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# api key of tmbd= 6a1d1f27bce9b7aa5f3f9dd4b0a723c1



# Function to recommend movies
def recommend(movie):

    movieindex = movies[movies['title'] == movie].index[0]
    distance = similarity[movieindex]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    for i in movies_list:

        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Set the page title
st.title("Movie Recommender System")

# Add background color, name at the bottom, and "Ujala Gupta" at the absolute top-right corner
st.markdown(
    """
    <style>
    /* Apply a pleasant teal background to the entire app */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0c0b0c; /* Muted teal background */
    }

    /* Adjust text color for contrast */
    [data-testid="stAppViewContainer"] {
        color: white;
    }

    /* Style the dropdown and text input */
    label {
        color: black !important; /* Make "Select a movie" and "Or type a movie" text white */
    }

    input {
        color: black !important; /* Text input color */
    }

    /* Style the recommend button */
    div.stButton > button {
        background-color: white; /* Purple button color */
        color: white; /* White text */
        border: none;
        padding: 6px 6px;
        border-radius: 8px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color:#fae4fa ; /* Lighter purple on hover */
    }

    /* Add your name at the bottom center */

    div:has(> footer) {
        position: relative;
        padding-top: 50px;
    }
     .footer-name {
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 12px;
        color: white;
        font-weight: lighter;
        z-index: 1000;
    }


    </style>
      <div class="footer-name">Created by Ujala Gupta</div>
    """,
    unsafe_allow_html=True
)

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values,
    index=0
)

# Optional text input for typing the movie name
typed_movie_name = st.text_input(
    'Or type a movie name here:',
    placeholder='Enter the movie title'
)

# Determine which input to use (dropdown has priority)
movie_to_search = typed_movie_name.strip() if typed_movie_name.strip() else selected_movie_name

# Recommend movies when the button is clicked
if st.button('Recommend'):
    try:
        recommendations = recommend(movie_to_search)
        st.subheader("Recommended Movies:")
        for i in recommendations:
            st.write(i)
    except IndexError:
        st.error("Movie not found. Please check the spelling or try a different movie.")