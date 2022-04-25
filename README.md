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

![image](https://user-images.githubusercontent.com/91243691/165027743-e2f82f3c-019a-49c8-9b94-af0438a2f04c.png)


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

-  This method turns text into fixed-length vectors by simply counting the number of times a word appears in a document, a process referred to as vectorization.

- from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
vectors = cv.fit_transform(new_movies_df['tags']).toarray()


- Now to we have the vector representation for every movie , we have to calculate the distance between every movies so that we can get the similarity of the movies , but we apply cosine similarity formula to calcluate the distances.


- from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)


- Recommend function is to fetch the index of movie that has user has entered and fetch particular movie vector values and we have to sorted the vector values to get the top 5 movies which are similar to the user mentioned movies and then print it .   

def recommend(movie):
    movie_index = new_movies_df[new_movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        print(new_movies_df.iloc[i[0]].title)


- Output

![image](https://user-images.githubusercontent.com/91243691/165027610-fe6efbd4-eebc-4050-927a-1d0d61fa241f.png)


- Create website on pycharm using streamlit .























