# Movie_Recommendation_Engine

Objective - User will search a particular movie , based on that movie we have to give recommendation of 
some other movie which has same attribues.

Click to check the dataset : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

Click to check the website hosted on Heroku platform : https://movies-recommendationengine.herokuapp.com/


Types of Recommendation Engines.

1. Content-based Filtering  -  This algorithm recommends products or movies that are similar to the ones that a user has liked in the past. 


2. Collaborative Filtering - In this strategy is based on the combination of the user’s behavior and comparing and contrasting that with other users’ behavior in the database. 



Below are the Datasets details 

- movies (4803, 20)  / credits (4813, 4)

- Below are the features of both the tables.

- movies columns ['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime','spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count']


- Credits columns are ['movie_id','title','cast','crew']


Steps 1 : EDA and Feature Engineering 

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


- import ast
def convert_string_tolist_cast(obj):
    L = []
    counter =0
    for i in ast.literal_eval(obj):
        if counter!=3:
            L.append(i['name'])
            counter=counter+1
        else:
            break
    return L    


- In Cast , select top 3 characters.


- In crew , check for the job = 'Director' 

import ast
def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj.replace('\r','\\r').replace('\n','\\n').replace('\n','\\n')):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
        return L 


- Now we have to remove the spaces in the value of some of the features and join all the features as informed earlier.

- new_movies_df['tags']=new_movies_df['overview'] + new_movies_df['genres'] + new_movies_df['keywords'] + new_movies_df['cast']

- The new dataset will have 3 features - movie_id,title and tags.


Step 2 : 

- Remove stopwards from the tags features and do the stemming .

- Now to have to create vector of the tags features using bag of words technique .

- Bag of Words



























