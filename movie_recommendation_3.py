#!/usr/bin/env python3
#cosine similarity in prev project
import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Get the data 
path = 'movie_metadata.csv'
df = pd.read_csv(path) 

print(list(df))

column_names= ['movie_title','genres','director_name','content_rating','imdb_score','plot_keywords','actor_2_name','actor_1_name']

movie= df[column_names].copy()
movie=movie.drop('content_rating',axis=1)

#add column index
count_row = movie.shape[0] 
cc= [x for x in range(count_row)]
movie['index']=cc


#handle missing values
column_names= list(movie)
for c in column_names:
    movie[c]=movie[c].fillna('')

#spliting genres
def split_genre(row):
    s=''
    a= row['genres'].split('|')
    for k in a:
        s+= str(k)
        s+=' '  
    return s
movie['genres']= movie.apply(split_genre,axis=1)
    
#combing all the fields
comb= 'combined'

def combining_funct(row):
    s=''
    for c in column_names:
       if c != 'content_rating' and c!= 'index' and c!= 'imdb_score':
        s+=str(row[c])
        s+=' '
    return s

movie[comb]= movie.apply(combining_funct, axis=1)

## vectorisation
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(movie[comb])

##cosine similarity
cosine_sim = cosine_similarity(count_matrix)


# movie.attributei.e. column name
def get_title_from_index(index):
    return movie[movie.index==index]['movie_title'].values[0]

def get_index_from_title(title):
   return movie[movie.movie_title==title]['index'].values[0]

#to test
print(get_title_from_index(1))
s=get_title_from_index(0)

print(get_index_from_title(s))
