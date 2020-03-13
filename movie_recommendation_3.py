#!/usr/bin/env python3
#cosine similarity in prev project
import pandas as pd
import numpy as np 
# Get the data 
path = 'movie_metadata.csv'
df = pd.read_csv(path) 

print(list(df))

column_names= ['movie_title','genres','director_name','content_rating','imdb_score','plot_keywords','actor_2_name','actor_1_name']

movie= df[column_names].copy()
movie=movie.drop('content_rating',axis=1)

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
       if c != 'content_rating':
        s+=str(row[c])
        s+=' '
    return s

movie[comb]= movie.apply(combining_funct, axis=1)