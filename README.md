# Movie_Recommendation_Engine

Objective - Recommend movies to users based on user preferences.

Click to check the dataset : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

Click to check the website on Heroku platform : https://movies-recommendationengine.herokuapp.com/


Types of Recommendation Engines.

1. Content-based Filtering  -  This algorithm recommends products or movies that are similar to the ones that a user has liked in the past. 


2. Collaborative Filtering - In this strategy is based on the combination of the user’s behavior and comparing and contrasting that with other users’ behavior in the database. 



2 Datasets are available 

- movies (4803, 20)  / credits (4813, 4)

- Below are the features of both the tables.

- movies columns ['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime','spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count']


- Credits columns are ['movie_id','title','cast','crew']


Steps :

- Join 2 tables on basis of title - new_movies_df = movies.merge(credits,on='title')

- Here is the list of columns which are required to recommend movies 

- new_movies_df = new_movies_df[['movie_id','title','overview','genres','keywords','cast','crew']]

- Drop the remaining columns as it is not required.

- There is no duplicated values available but there are null values which we can drop the null values.

- Here , 5 features such as 'overview','genres','keywords','cast','crew' are in the form of dictionary so we have to convert that into List and have to merge it into single features such as tags where all the information of particular movie will be available such as overview , top 3 actors from every movie , generes , keywords ,director name

- import ast
def convert_string_tolist(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L    
    
    
- For generes and keywords , apply above function to extract only the name from the given dictionary.


- 




















